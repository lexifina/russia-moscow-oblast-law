# Moscow Oblast: law history in git

The law of Moscow Oblast (Московская область), a federal subject of the Russian Federation, as a git history: one file per article, one commit per law, dated the day it took effect. `git log` lists every law; checking out a date gives the texts in force that day.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `ru-mos/`. The federal law of Russia is in [lexifina/russia-law](https://github.com/lexifina/russia-law).

The text is in Russian, in Cyrillic, exactly as the Moscow Oblast Duma publishes it.

## What this repository holds

One folder per law of Moscow Oblast (`zakon-<year>-<number>/`, for Закон Московской области № <number>/<year>-ОЗ), each in its text as enacted. A law is included only when

- it is a law in its own right: laws that only amend, suspend or repeal other laws are left out;
- no other law in the Duma's bank cites its number, so that, as far as the bank shows, it has never been amended, suspended or repealed and its text as enacted is still its whole text;
- its in-force clause gives one day for the whole law (see Dates);
- its text holds no tables.

The Charter of Moscow Oblast (Устав Московской области) and every amended law are not included yet: no official consolidated text was reachable from the publishers' sites when this was built. The history therefore starts with the earliest included law and is not the whole law of the region.

## Source

The Moscow Oblast Duma (Московская областная Дума), <https://www.mosoblduma.ru/Zakoni/Zakoni_Moskovskoj_oblasti>: its bank of laws of Moscow Oblast, which gives each law's text as enacted, its number, the day the governor signed it, the Duma resolution that adopted it and where it was officially published.

## Dates

- The official publication day is the earliest day in the publication line the Duma gives for the law (the Government's Internet portal www.mosreg.ru, the Official Internet Portal of Legal Information www.pravo.gov.ru, or the newspaper "Ежедневные Новости. Подмосковье").
- The in-force day follows the law's own clause: the publication day ("со дня его официального опубликования"), the next day ("на следующий день после дня его официального опубликования"), the eleventh day after it ("по истечении десяти дней после дня его официального опубликования"), the tenth day after it ("через десять дней после его официального опубликования", and likewise for another number of days), or the date the law names. Laws that say they lapse on a date are left out.
- Each commit is dated at noon, Europe/Moscow, on that day, and credited to the law itself.

## Files

`<law>/statya-001.md` is Статья 1, `statya-002-1.md` Статья 2.1. `vvedenie.md` holds the heading, the title and any preamble; `podpis.md` the governor's signature, the date and number, the Duma resolution that adopted the law, and any appendix. Chapter headings stay in the file of the first article after them. One paragraph per line.

## How it is checked

- Every version is read back from git on the day it took effect and on the day before; both must match `corpus.json`.
- Every law's letters and digits, in order, equal those of the Duma's text as read by a second, independent HTML reader.
- Health checks: no merge commits, commit dates never go backwards, nothing dated in the future, and every commit's trailers parse.

## Limits

This is not an official publication. The binding text is the one officially published. Only the laws listed in `data/versions.json` are included, each in its text as enacted; a law cited by a later law is left out even if that law did not change it. The Duma's bank starts in 2012 and lacks a few numbers in some years; an amendment made by a law missing from the bank would not be seen.

---

# Московская область: история права в git

Законы Московской области как история git: один файл на статью, один коммит на закон в день его вступления в силу. Тексты на русском языке, в редакции, в которой их публикует Московская областная Дума.

Включены только самостоятельные законы в первоначальной редакции, на номера которых не ссылается ни один другой закон банка законов Думы (то есть не изменявшиеся, не приостанавливавшиеся и не признававшиеся утратившими силу), с одним днём вступления в силу для всего закона и без таблиц. Устав Московской области и законы с изменениями пока не включены. Это не официальное опубликование.
