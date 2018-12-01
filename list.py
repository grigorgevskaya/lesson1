school_list = [
    {'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
    {'school_class': '4b', 'scores': [4, 4, 4, 5, 5]},
    {'school_class': '4c', 'scores': [1, 3, 5, 2, 2]},
    {'school_class': '4d', 'scores': [5, 4, 5, 5, 5]}
]


def main(school_list):
    classes_average_scores = dict()
    all_cls_av_score = list()

    for item in school_list:
        cls_av_score = sum(item["scores"])/len(item["scores"])
        classes_average_scores[item["school_class"]] = cls_av_score
        all_cls_av_score.append(cls_av_score)

    for cls in classes_average_scores.items():
        print(f"В классе {cls[0]} средняя оценка {cls[1]:.2f}")

    print(f"Средний балл во всех классах {sum(all_cls_av_score):.2f}")


if __name__ == "__main__":
    main(school_list)
