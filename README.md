# LearnBot

## ❓ About

```text
Learnbot is A Discord Bot scripted in Python that is designed to assist learning the Japanese Character system.
It can generate simple multiple choice exercise cards that can simply be solved by reacting with the right emoji.

The Bot can track a users progress and generates exercises designed to work on the learners weaknesses.
Exercise generation has changing parameters that allow it to generate Exercises that are often answerd wrong more regularly.

This Bot will not be updated as I am curently working on a new Version that has more organized Datastructures,
makes better use of the Discord.py functionality and runs with more efficient memory.
```

---

## ⚙️ Bot Setup

To use this bot yourself yourself you need a Discord Bot and it's Token

```text
- create a file named 'Keys.txt' in the project's directory
- open it and paste your token as the first line
- save changes
```
To host the Bot on your local machine just run 'Bot.py'.
The Bot will work on all Servers on which it has required permissions and in DMs.

---

## ▶️ How to use

How to practice Japanese with Schneckbot

The command prefix for the Bot is '!'

**Commands:**

```text
- !tutorial: Shows a Guide. Alternatvely use '!guide', '!intro'
- !practice: Generates an Exercise Card of the given Type.
- !profile: Shows the given users Profile. Shows your Profile if no user is specified.
```

## !practice

Alternative commands: !japanese, !learn

Generates an Exercise Card. You can specify the type of exercise you want to do by including the type after the command e.g. '!learn hiragana'.
Valid types are:

```text
- hiragana
- katakana
- kana
- kanji
```

**Solve Exercise**

```text
You can solve the card by reacting to the card with the corresponding Number Emoji.
Reacting with ❓ will solve the Card without affecting your Userstats.
After resolving a card you can generate a new Card of the same Type by reacting with 🔁 to the resolve Notification.
```

**Practice Kanji**

```text
If you are practicing Kanji you will have the option to react with 🔎 to recive information on the Kanji's different readings.
```

**Report Exercise**

```text
If a Exercise seems like it has an Error of any kind, you can report it by reacting with ❗ on the resolve Notification so you can take a look at it.
All this does is save the message ID to Cache/Reported/. This doesn't work anymore if you already generated a new Card.
```


## !profile

Alternative commands: !user, !stats

```text
Shows the given users Profile. Shows your Profile if no user is specified.
A users profile contains statistics for their learning progress like the amount of learned characters and finished exercises.
```

---


 
