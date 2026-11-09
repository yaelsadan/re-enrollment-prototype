# Re-enrollment prototype · Citizen Hub

גרסה 25 של הפרוטוטייפ, כפי שפורסמה ב-claude.ai (Alternative A, חלונית אחת מעל Home, דסקטופ 1440×900).
כל הנתונים בפרוטוטייפ הם נתוני דמה.

## הרצה

האתר סטטי. קובץ הכניסה הוא `index.html` בשורש ה־repo, והוא פותח ישר את הפרוטוטייפ הלחיץ ב־`project/Reenroll.dc.html`. כל הקישורים יחסיים: רכיבים, פונטים ואייקונים נטענים בלי שרת מיוחד ובלי הפניות.

### GitHub Pages

מפרסמים את הענף `main` מתיקיית השורש (`/`). אחרי ההפעלה הכתובת היא:

**`https://<user>.github.io/re-enrollment-prototype/`**

הלינק הזה מגיש את `index.html`, שנפתח אל `project/Reenroll.dc.html`. הקובץ `.nojekyll` מונע מ־GitHub Pages להריץ Jekyll, כדי שכל הקבצים (כולל פונטים ו־`.dc.html`) יוגשו כמו שהם.

### הרצה מקומית

דרוש Python 3 בלבד (ספרייה סטנדרטית, בלי התקנות ובלי אינטרנט). מריצים מתיקיית השורש, כמו ב־GitHub Pages:

```bash
cd re-enrollment-prototype
python3 serve.py
```

ואז לפתוח בדפדפן: **http://localhost:8799/**

אותו דבר עם השרת המובנה של Python: `python3 -m http.server 8799`.

- קובץ הכניסה: `index.html` (פותח את `project/Reenroll.dc.html`).
- פורט אחר: `PORT=8800 python3 serve.py`
- לעצירה: Ctrl+C.
- אין לפתוח את הקובץ ישירות מהדיסק (`file://`): הדפדפן חוסם טעינת רכיבים עם `fetch`.

## מבנה

| נתיב | מה יש בו |
| --- | --- |
| `index.html` | כניסת האתר. פותח את הפרוטוטייפ הלחיץ |
| `.nojekyll` | מורה ל־GitHub Pages להגיש את התיקייה כמו שהיא |
| `serve.py` | שרת סטטי אופציונלי של שורש ה־repo. בלי הפניות ובלי מיפוי כתובות |
| `project/Reenroll.dc.html` | הפרוטוטייפ הלחיץ המלא, כולל כלי הבדיקה |
| `project/enroll.css` | כל העיצוב של התהליך |
| `project/ClassPicker.dc.html`, `EnrollmentSummary.dc.html`, `EnrollmentDetails.dc.html` | רכיבים לשימוש חוזר |
| `project/MA-*.dc.html`, `NC-*.dc.html`, `RP-Consent.dc.html` | פריימים סטטיים של Alternative A (כל אחד פותח את הפרוטוטייפ בשלב מסוים) |
| `project/MB-*`, `NC-B-Class`, `A1–A4`, `B1–B3`, `Structure`, `Main` | ארכיון: חלופה B, השוואת מבנים במסך מלא והבנייה הראשונה |
| `project/canvas.json` | סידור הקנבס של ה-Design artifact (לא נדרש להרצה מקומית) |
| `project/ds/citizen-hub/` | הדיזיין סיסטם Citizen Hub: `tokens.css`, `tokens.json` ופונט Assistant. כותרות סריפיות משתמשות בפונט סריפי של מערכת ההפעלה |
| `runtime/support.js` | ה-runtime של רכיבי `.dc.html` (כולל React, רישיון MIT בכותרת הקובץ) |
| `assets/` | אייקוני הרמות Light Blue, Blue, Green, Dark Green, והמונוגרמה של Citizen Café |
| `project/assets/` | רקעי הצילום של החלונית ואייקון ה־V בחגיגה |

את ה-runtime ואת הנכסים לקחתי מהגרסה שפורסמה ב-claude.ai, ולא מקבצים זמניים.

## כלי הבדיקה (לא חלק מהמוצר)

הפס הכהה בראש העמוד:
- **תרחישים:** 1 Credit · 2 Choice, no credit · 3A Repeat, credit · 3B Repeat, no credit, וגם Back to start.
- **מתגים:** Existing class time available · Manual discount in deal.
- **readout:** המסך הנוכחי, מצב העסקה, הכיתה, החבילה, הקרדיטים, וגם מונים של ניסיונות תשלום, חיובים והרשמות.
- **FLOW:** תוצאת ספק התשלום (הצלחה, כישלון, ביטול) ותוצאת האימות. יש גם Replay celebration, מתג Confetti stroke ו-Simulate refresh / return again.
- **TEAM NOTES:** הערות צוות לכל שלב: תוכן חסר, הצעות UX, נתוני דמה והנחיות חדשות.
- Hide tool מסתיר את הפס.

## מסלולים ומצבים

**מסלול עם קרדיט (תרחישים 1, 3A):**
המלצה (שעה קיימת) או שעות וסמסטרים אחרים → (3A: אישור חזרה על סוג קורס) → Review and confirm → אימות אוטומטי קצר → Manage My Enrollment עם חגיגה.

**מסלול רכישה (תרחישים 2, 3B):**
בחירת קורס (Dark Green או Fluency Accelerator) → כיתה וסמסטר → (3B: אישור חזרה, רק בסמסטר עם Type A) → חבילה (Classic נבחרת בכניסה) → סיכום לפני תשלום → עמוד ספק חיצוני מדומה → חזרה ואימות:
- **Confirming your enrollment…**: אימות בתהליך.
- **Payment cancelled / didn't go through**: Try payment again או Back to package, והבחירות נשמרות.
- **Payment received**: התשלום אושר אבל ההרשמה עוד בתהליך, בלי הזמנה לשלם שוב.
- **Enrollment created**: מעבר ל-Manage My Enrollment.

**סיום (בשני המסלולים):**
1. חגיגה במרכז החלונית (V בעיגול צהוב, "You're in, Yael!", קונפטי בצבעי הרמות), כ-2.6 שניות.
2. מעבר לרצועה קומפקטית, וחשיפת Manage: הלשוניות Current Course ו-Upcoming Course (נפתחת על Upcoming), פרטי ההרשמה, ספירה לאחור לשיעור הראשון, Change class ו-Change semester.

החגיגה מופיעה פעם אחת לכל הרשמה. בפתיחה מחדש, בחזרה נוספת מהתשלום או ב-Simulate refresh מוצג Manage בלי חגיגה.

**לאורך כל התהליך:** אזור זמן ניתן לשינוי (popover), Still need help? בפוטר, וסגירה ופתיחה מחדש שומרות את הבחירות.

## הנחות והחלטות פתוחות

**סתירות ופערים באפיון שלא הוכרעו:**
- Profile B, Window 2: החלפה עצמית של כיתה נוכחית, מול §6–7 שבהם שינוי נוכחי עובר רק דרך Community.
- כלל חמשת החודשים: "and/or" מול תנאי מצטבר.
- מתי נפתחת ההרשמה מחדש: אחרי הערכות או ביצירת העסקה.
- מקור המחיר: העסקה או שער הדולר, ונעילת מחיר מול עדכון של איש מכירות.
- Pro מול Professional בשם החבילה.
- שמות סוגי הקורס ותיאורי הקורסים (מוצגים Type A–D ותיאורים זמניים).
- בדיקת השעה הקיימת (כאן: בסמסטר הקרוב בלבד), עיתוי ההסכמה לחזרה, שמירת כיתה ושריון מקום בבחירה.
- קרדיטים אחרי חבילה רב-סמסטרית, כתיבה חוזרת של אזור הזמן, מייל אישור, תנאי ביטול (אין נוסח מאושר, ולכן לא מוצג).
- הרשמה עתידית קיימת בזמן הרשמה מחדש.

**הנחות UX שדורשות אישור:**
- אזור זמן ואישור חזרה על סוג קורס בתוך החלונית, אף שבאפיון כתוב pop-up.
- Classic נבחרת בכניסה, לפי בקשה ולא לפי כלל באפיון.
- שמירת הבחירות בסגירה היא הנחת פרוטוטייפ.
- הבית (Home) הוא רקע להמחשה בלבד.

**הנחיות חדשות מהסבבים האחרונים (לא מהאפיון):**
- מספר תשלומים לכל חבילה: Drop-in עד 3, Classic עד 5, Professional עד 8. סכום לתשלום, תשלומים שווים וריבית לא הוגדרו ולכן לא מוצגים.
- הזנת אשראי ובחירת מספר התשלומים מתבצעות אצל ספק תשלום חיצוני, בלי טופס אשראי ב-HUB.
- הסיום פותח את Manage My Enrollment עם חגיגה חד-פעמית.

**מה הודגם ב-Manage:**
Profile C (פעיל/ה עם הרשמה עתידית), Window 1 (יותר משבוע לפני תחילת הסמסטר). ב-Upcoming מותר לשנות כיתה וסמסטר, וב-Current השינוי עובר דרך Community. תהליכי Change class ו-Change semester עצמם לא נבנו.

## מה לא כלול ומגבלות

- **עורך הקנבס של ה-Design artifact** (סידור הפריימים, ההערות וכלי העריכה): הוא חלק מפלטפורמת claude.ai ולא ניתן להרצה מקומית. `canvas.json` כלול לתיעוד בלבד. כאן כל פריים נפתח כעמוד נפרד.
- **פרטי קשר של Community:** כתובת המייל `community@example.com` וקישור ה-WhatsApp הם פיקטיביים.
- **רענון אמיתי של הדפדפן:** מאפס את הפרוטוטייפ, כי המצב נשמר רק בזיכרון. לבדיקת חזרה נוספת יש להשתמש ב-Simulate refresh.
- **שם הספק:** עמוד ספק התשלום הוא הדמיה (`pay.provider.example`), ואין חיבור לספק אמיתי.
- **פונט סריפי:** עותק הפרסום לא כולל את Fedra Serif PRO. הכותרות משתמשות ב־`ui-serif`, ואחר כך Georgia ו־Times New Roman. Assistant נשאר.
- **רישוי:** לפני דחיפה פומבית צריך לאשר את נכסי המותג ואת צילומי הרקע. פירוט בסוף הקובץ.

## רישוי לפני העלאה

Fedra Serif PRO ו־`package-dialog.jpg` לא נכללים בעותק הזה. הקבצים שנשארים ועדיין דורשים אישור לפני repo פומבי:

| קבצים | מה לבדוק |
| --- | --- |
| `project/ds/citizen-hub/fonts/Assistant-*.ttf` (שישה קבצים) | Assistant, רישיון SIL Open Font License 1.1. זכויות היוצרים וטקסט הרישיון נמצאים במטא־דאטה של כל קובץ. |
| `assets/23051ef855b3ca31817b26661f68a94d.png` | מונוגרמה של Citizen Café. נכס מותג; לאשר זכות פרסום. |
| `assets/b3d5711e927ffc5317f5819cfeb63b29.svg`, `62b41bc62b543592ffa178e29ca23bfe.svg`, `bf6f7fa43a419f17955ba55b936f9a96.svg`, `cfc9454d80929285bbf7c392d4358703.svg` | אייקוני הרמות Light Blue, Blue, Green, Dark Green. נכסי מותג; לאשר זכות פרסום. |
| `project/assets/offer-dialog.jpg`, `review-dialog.jpg`, `celebrate-dialog.jpg` | רקעי צילום שבשימוש, מוקטנים מ־4096px. לאשר שמותר לפרסם את התמונות. |
| `runtime/support.js` | כולל את React ו־ReactDOM 18.3.1. בכותרת הקובץ יש הודעת MIT, אבל קובץ `LICENSE` מלא לא נמצא ב־repo. |
