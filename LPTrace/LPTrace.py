from LilithPyBezier.LilithPyBezier import LPBezier
from matplotlib import pyplot as plt
import json
import random
import os


class LPTrace(object):
    def __init__(self, config_path="generation_config.json"):
        self.config_path = config_path

        self.shape_name = None
        self.anchor_goto_xs = None
        self.anchor_goto_ys = None
        self.anchor_spy_xs = None
        self.anchor_spy_ys = None

        self.width = None
        self.height = None
        self.number = None

        self._load_config()

    @staticmethod
    def _load_json_data(json_path):
        with open(json_path, 'r') as json_file:
            return json.load(json_file)

    def _load_config(self):
        config_json = self._load_json_data(self.config_path)
        shape_json = self._load_json_data(config_json["shape_file"])

        self.width = config_json["width"]
        self.height = config_json["height"]
        self.number = config_json["number"]

        self.shape_name = shape_json["shape_name"]
        self.anchor_goto_xs = shape_json["anchor_goto_xs"]
        self.anchor_goto_ys = shape_json["anchor_goto_ys"]
        self.anchor_spy_xs = shape_json["anchor_spy_xs"]
        self.anchor_spy_ys = shape_json["anchor_spy_ys"]

    def _parse_trace(self, xs, ys, bezier):
        pre_point = None
        post_point = None

        for index, value in enumerate(xs):
            if pre_point is None:
                pre_point = dict(x=value, y=ys[index])
            else:
                post_point = dict(x=value, y=ys[index])

            if pre_point is not None and post_point is not None:
                self._add_anchor(pre_point, post_point, bezier)
                pre_point = None
                post_point = None

    @staticmethod
    def _add_anchor(pre_point, post_point, bezier):
        if pre_point['x'] == post_point['x'] and pre_point['y'] == post_point['y']:
            bezier.add_anchor(pre_point['x'], pre_point['y'])
        else:
            new_x = random.uniform(pre_point['x'], post_point['x'])
            new_y = random.uniform(pre_point['y'], post_point['y'])
            bezier.add_anchor(new_x, new_y)

    def generate_trace(self):
        for x in range(self.number):
            total_bezier_point = dict(xs=list(), ys=list())

            goto_bezier = LPBezier(self.width / 100, self.height / 100)
            self._parse_trace(self.anchor_goto_xs, self.anchor_goto_ys, goto_bezier)
            goto_bezier_point = goto_bezier.get_bezier_points()

            total_bezier_point['xs'].extend(goto_bezier_point['xs'])
            total_bezier_point['ys'].extend(goto_bezier_point['ys'])

            spy_bezier = LPBezier(self.width / 100, self.height / 100)
            self._parse_trace(self.anchor_spy_xs, self.anchor_spy_ys, spy_bezier)
            spy_bezier_point = spy_bezier.get_bezier_points()
            total_bezier_point['xs'].extend(spy_bezier_point['xs'][1:])
            total_bezier_point['ys'].extend(spy_bezier_point['ys'][1:])

            max_x = max(spy_bezier_point['xs'])
            max_y = max(spy_bezier_point['ys'])
            min_x = min(spy_bezier_point['xs'])
            min_y = min(spy_bezier_point['ys'])

            focus_region = dict(max_x=max_x, max_y=max_y, min_x=min_x, min_y=min_y)

            return_bezier = LPBezier(self.width / 100, self.height / 100)
            self._parse_trace(self.anchor_goto_xs, self.anchor_goto_ys, return_bezier)
            return_bezier_point = return_bezier.get_bezier_points()
            reverse_bezier_xs = return_bezier_point['xs'][::-1][1:]
            reverse_bezier_ys = return_bezier_point['ys'][::-1][1:]

            total_bezier_point['xs'].extend(reverse_bezier_xs)
            total_bezier_point['ys'].extend(reverse_bezier_ys)
            print("Creating ", x, " trace\n")

            if not os.path.exists("metadata"):
                os.makedirs("metadata")
            if not os.path.exists("generate"):
                os.makedirs("generate")

            self._save_trace_to_json(total_bezier_point, focus_region, "metadata/" + str(x) + ".json")
            self._save_to_image(total_bezier_point, "generate/" + str(x) + ".png")

    def _save_trace_to_json(self, bezier_point, focus_region, file_path):
        time = list()
        time_tag = 0
        for value in bezier_point['xs']:
            time.append(time_tag)
            time_tag = time_tag + 1
        meta_data = dict(file_path=file_path,
                         focus_region=focus_region,
                         trace=bezier_point,
                         time=time,
                         shape_name=self.shape_name)
        with open(file_path, 'w') as json_file:
            json.dump(meta_data, json_file, indent=2)


    def _save_to_image(self, bezier_points, file_path):
        fig = plt.figure("Bezier", dpi=100, figsize=(self.width / 100, self.height / 100), frameon=False)
        canvas = fig.add_subplot(111)

        canvas.clear()
        canvas.axis([1, self.width, 1, self.height])
        canvas.set_frame_on(False)
        canvas.set_axis_off()
        canvas.set_position([0, 0, 1, 1])

        canvas.plot(bezier_points['xs'], bezier_points['ys'], linewidth=3)

        with open(file_path, mode='wb') as image_file:
            fig.savefig(image_file, format='png')


