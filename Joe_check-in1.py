def available_questions(self, subject):
        place = self.dictionary.get(subject)
        keys = place.keys()
        l = []
        for i in keys:
            l.append(i)
        return f'{subject} Questions Available: {l}'