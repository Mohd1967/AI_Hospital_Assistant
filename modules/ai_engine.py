"""
ai_engine.py
واجهة بسيطة لمحرك الاستشارات باستخدام نموذج AI (مثال).
في المرحلة الأولى سنحاكي الاستجابة ثم نربطها بالـ API الفعلي لاحقًا.
"""

from typing import Dict

def generate_consultation(question: str, language: str = "arabic") -> Dict:
    """
    استقبال سؤال طبي وإرجاع إجابة مبدئية (محاكاة).
    لاحقًا تستبدل هذه الدالة بنموذج حقيقي مثل OpenAI أو محرك داخلي.
    """
    # مثال محاكى
    answer = f"هذه إجابة مبدئية للسؤال: '{question[:200]}' (اللغة: {language})"
    recommended_action = "راجع طبيب مختص إذا استمرت الأعراض أو كانت حادة."
    return {
        "answer": answer,
        "recommended_action": recommended_action,
        "confidence": 0.6  # مؤقت
    }

if __name__ == "__main__":
    # اختبار سريع محلي
    print(generate_consultation("ما علاج الحمى؟"))
