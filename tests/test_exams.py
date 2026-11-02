import unittest
from collections import Counter

from app import app
from data.exames import EXAMS


class ExamTests(unittest.TestCase):
    def test_each_level_has_objective_listening_and_speaking_activities(self):
        self.assertEqual(list(EXAMS), ["A1", "A2", "B1", "B2"])
        for level, exam in EXAMS.items():
            with self.subTest(level=level):
                self.assertEqual(Counter(q["section"] for q in exam["questions"]),
                                 {"reading": 4, "grammar": 4, "usage": 4})
                self.assertTrue(exam["reading"])
                self.assertTrue(exam["writing_pt"])
                self.assertTrue(exam["writing_fr"])
                self.assertEqual(len(exam["listening"]), 4)
                self.assertEqual(len(exam["speaking"]), 4)
                self.assertTrue(all(phrase.strip() for phrase in exam["speaking"]))
                for question in exam["questions"] + exam["listening"]:
                    self.assertEqual(len(question["options"]), 3)
                    self.assertIn(question["answer"], range(3))
                    self.assertTrue(question["explanation"])
                self.assertTrue(all(question["audio"] for question in exam["listening"]))

    def test_exam_pages_render_in_both_interface_languages(self):
        client = app.test_client()
        for language in ("pt", "fr"):
            with client.session_transaction() as session:
                session["lang"] = language
            for level in EXAMS:
                with self.subTest(language=language, level=level):
                    response = client.get(f"/exames/{level.lower()}")
                    self.assertEqual(response.status_code, 200)
                    self.assertEqual(response.data.count(b'class="exam-question"'), 16)
                    self.assertEqual(response.data.count(b'data-speech-item="'), 4)
                    self.assertEqual(response.data.count(b'data-listen="'), 4)
                    self.assertIn(b'id="exam-data"', response.data)
        self.assertEqual(client.get("/exames/c1").status_code, 404)


if __name__ == "__main__":
    unittest.main()
