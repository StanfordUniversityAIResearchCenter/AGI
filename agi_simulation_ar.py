"""
محاكاة مبسطة للذكاء الاصطناعي العام (AGI)

النموذج يحتوي على:
- قاعدة معرفة عامة يمكن توسيعها.
- التعلم من أمثلة جديدة.
- حل مشكلات متنوعة.
- معالجة مهام متعددة.

ملاحظة: هذا نموذج تعليمي رمزي وليس ذكاء اصطناعي عام حقيقي.
"""

import random

class AGI:
    def __init__(self):
        # قاعدة المعرفة
        self.knowledge = {}
        # ذاكرة تجارب التعلم (سؤال - جواب)
        self.experiences = []

    def learn_fact(self, fact, explanation):
        """تعلم حقيقة جديدة مع شرح"""
        self.knowledge[fact.lower()] = explanation
        print(f"تعلمت حقيقة جديدة: '{fact}'")

    def learn_from_example(self, example_input, example_output):
        """تعلم من مثال جديد"""
        self.experiences.append((example_input.lower(), example_output))
        print(f"تعلمت من المثال: '{example_input}' -> '{example_output}'")

    def answer_question(self, question):
        """الإجابة على سؤال باستخدام المعرفة والتجارب"""
        question = question.lower()

        # محاولة جواب مباشر من المعرفة
        if question in self.knowledge:
            print("تم العثور على إجابة في قاعدة المعرفة.")
            return self.knowledge[question]

        # محاولة مطابقة جزئية في المعرفة
        for fact, explanation in self.knowledge.items():
            if fact in question or question in fact:
                print("تم العثور على تطابق جزئي في المعرفة.")
                return explanation
        
        # محاولة استخدام خبرات التعلم من الأمثلة
        for inp, outp in self.experiences:
            if inp in question:
                print("تم العثور على تطابق في خبرات التعلم.")
                return outp

        # التخمين بذكاء مبسط (مثلاً إجابة عامة)
        print("لا توجد معرفة كافية، التخمين.")
        return "لا أعلم الإجابة بدقة، سأحتاج لتعلم المزيد."

    def do_math(self, expr):
        """محاولة حل التعبيرات الحسابية البسيطة"""
        try:
            result = eval(expr)
            print(f"تم حل العملية الحسابية: {expr} = {result}")
            return result
        except Exception:
            return "لا يمكن حل التعبير الرياضي."

    def multitask(self, task_type, data):
        """تنفيذ مهام مختلفة حسب النوع"""
        if task_type == 'سؤال':
            return self.answer_question(data)
        elif task_type == 'حساب':
            return self.do_math(data)
        else:
            return "المهام الأخرى غير مدعومة حالياً."

if __name__ == "__main__":
    agi = AGI()

    # تعلم حقائق عامة
    agi.learn_fact("ما هو لون السماء؟", "السماء تكون زرقاء في النهار وغالباً سوداء في الليل.")
    agi.learn_fact("ما هو عاصمة مصر؟", "عاصمة مصر هي القاهرة.")
    
    # تعلم من أمثلة
    agi.learn_from_example("ما هو 2 + 2؟", 4)
    agi.learn_from_example("كم يساوي خمس ناقص اثنين؟", 3)

    # اختبارات

    # سؤال مباشر
    print("سؤال:", "ما هو لون السماء؟")
    print("إجابة:", agi.multitask('سؤال', "ما هو لون السماء؟"))

    print()

    # سؤال جزئي
    print("سؤال:", "أين تقع القاهرة؟")
    print("إجابة:", agi.multitask('سؤال', "أين تقع القاهرة؟"))

    print()

    # سؤال من الخبرة
    print("سؤال:", "ما هو 2 + 2؟")
    print("إجابة:", agi.multitask('سؤال', "ما هو 2 + 2؟"))

    print()

    # حساب
    print("حساب:", "5 * (3 + 2)")
    print("نتيجة:", agi.multitask('حساب', "5 * (3 + 2)"))

    print()

    # سؤال غير معروف
    print("سؤال:", "من هو أول رائد فضاء؟")
    print("إجابة:", agi.multitask('سؤال', "من هو أول رائد فضاء؟"))
