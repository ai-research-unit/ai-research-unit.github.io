# __The Up and Low Proportions of the Physics Corpus__

The corpus is the 403 Markdown files of `articles_physics`. The count reads only the mathematics regions, inline and display: 105,583 regions holding 3,188,809 characters. One mark is one caret or one underscore.

| Mark | Count | Share |
|---|---:|---:|
| Raised | 40,554 | 25.3% |
| Low | 119,741 | 74.7% |
| All | 160,295 | 100% |

The count was re-taken after the repair of the abbreviated derivatives. That repair moved 458 low marks off $\partial$ onto the variable and added 30 power carets. The gradient pass then added 56 explicit sums, each contributing one low mark, and the convention text accounts for the rest. The pre-repair figures were 40,524 raised and 119,756 low. The validated tables below are the pre-repair split; the open classes are read again, form by form, on the present corpus.

The rest of the article sorts the marks into what the convention validates and what it leaves open. The validation is about the job of the mark, not about its height alone.

## Non-Validated

The three open classes are open for different reasons, and the reason matters more than the count.

| Class | Count | Share of its height | The question |
|---|---:|---:|---|
| Raised name | 4,238 | 10.5% of the 40,554 carets | does the caret carry a grade, a parameter or a label, or a frame slot? |
| Upright role name | 5,784 | 4.9% of the 119,741 lows | is a role a name, which rises, or a label of a slot, which stays low? |
| Operator or derivative index | 4,316 | 3.7% of the lows | it is neither a slot nor a name, and the rule does not name it |
| All three | 14,338 | 8.9% of the 160,295 marks | |

### Upper: the name

The name is a residual class: every caret that is not a numeric power and not a mark falls into it. The count is therefore a ceiling on names, not a count of them. On the raw class the raise-to-low ratio is 42.2% to 57.8%. A second pass reads 4,215 of the 4,238 and sorts them by the form of the raised argument.

| Form of the raised argument | Count | Share | Examples |
|---|---:|---:|---|
| Parenthesised label | 617 | 14.6% | ${}^{(r)}$, ${}^{(\mathrm{adj})}$, ${}^{(l)}$, ${}^{(k)}$ |
| Upright label | 486 | 11.5% | $S^{\mathrm{c}}$, $\Phi^{\mathrm{deph}}$, $F^{\mathrm{dual}}$, $g^{\mathrm{J}}$ |
| Greek argument | 257 | 6.1% | $e^{i\alpha}$, $\tau^{l\bar l}$, $\xi^{\alpha}$ |
| Multi-letter ASCII | 198 | 4.7% | $A^{abc}$, $C^{ab}$, $H^{sl}$ |
| Single letter | 1,550 | 36.8% | $T^a$, $L^T$, $M_4^R$, $\mathrm{Cl}^i$ |
| Compound expression | 1,107 | 26.3% | $x^{2n}$, $\delta^{rs}$, $e^{-\psi/2}$, $(-1)^{\lvert a\rvert\lvert b\rvert}$ |
| All | 4,215 | 100% | |

The first two rows are labels in the intended sense, and a label is a name: it names the representation, the sector or the order. The remaining four rows are mixed. The Greek argument is sometimes a power, $e^{i\alpha}$, and sometimes an index pair, $\tau^{l\bar l}$. The multi-letter argument is a label when it is $H^{sl}$ and a colour index when it is $A^{abc}$. The compound expression is mostly a power. The single letter carries no job of its own, which is why it needs the second table.

| Single-letter argument | Count | Examples |
|---|---:|---|
| Symbolic exponent $n,m,k,N,K,F,x,y,z,t,i,j$ | 528 | $2^n$, $(-1)^F$, $\Delta^{it'}$ |
| Remaining letters $a,b,c,\ldots$ | 601 | $T^a$, $G^a$, $\sigma^z$, $\psi^c$ |
| Structural label $L,R,A,E,H,B$ | 227 | $M_4^L$, $M_4^R$, $\Pi_1^A$ |
| Transpose $T$ | 194 | $L^T$, $\psi^T$ |
| All | 1,550 | |

Four parts of the class are not names. The transpose is a mark of the same kind as ${}^{*}$ and ${}^{\dagger}$: $T$, $\mathsf T$ and $\mathsf{T}$ together give 317 carets that belong with the marks, not with the names, and the mark screen found them because it did not read $T$. The symbolic exponents, 528 carets, are powers: the power screen tested the exponent for digits, so a letter or a composite expression fell through. About 250 more are powers written with a space or a compound exponent, $x^{\,2}$, $x^{2n}$, $e^{-\psi/2}$. The colour, gauge and spin indices, about 300, are the debt of the strict reading, the ten forms named in the earlier pass.

| Raised name case | Count |
|---|---:|
| Colour, gauge or spin index | about 300 |
| Transpose mark | 317 |
| Power with a space or a compound exponent | about 250 |
| Grade, parameter or label | about 3,370 |
| All raised names | 4,238 |

The corrections lower the count of names but not the height of any mark. What they change is the ratio: the names are about 3,370 raised against 5,784 low, or 36.8% up and 63.2% low, not the 42.2% that the raw class reports.

The corpus average hides a wide spread.

| Measure | Value |
|---|---|
| Lowest article | 2.9% raised (6 up, 201 low), *Torsion, Contorsion and the Spin Connection* |
| Median article | 24.9% raised |
| Highest article | 82.5% raised (301 up, 64 low), *The Relativistic Central Force Problem* |
| Articles above 50% raised | 21 of 403 |
| Largest article by marks | 562 up and 668 low, *Exercise: The Relativistic Kinematics of a Two-Body Decay* |

The raised names are not spread evenly. 310 of the 403 articles carry at least one; the ten that carry most hold 775 (18%), the twenty 1,269 (30%), and sixteen articles are more than half raised names. The concentration is in the particle-physics articles, where the colour and spin indices live, and the top of the list is the same population that the strict reading calls debt.

| Article | Raised names | Marks | Share |
|---|---:|---:|---:|
| *The Gluon: An Octet Outside the Biquaternion Algebra* | 109 | 168 | 64.9% |
| *Integer-Spin Quantization and the Adjoint Action on the Material Sector* | 102 | 145 | 70.3% |
| *The Jordan–Wigner Transformation* | 99 | 171 | 57.9% |
| *The Schwinger–Keldysh Formalism* | 77 | 141 | 54.6% |
| *Electromagnetism in Media: The Local Complex Structure at Work* | 75 | 264 | 28.4% |
| *The W and Z Bosons* | 68 | 175 | 38.9% |
| *The Spin Mass Formula and the Particle Spectrum* | 64 | 90 | 71.1% |
| *The Neutrino and Majorana Fermions* | 63 | 181 | 34.8% |

Four forms decide most of the borderline cases. The colour and spin index, $T^a$, $G^a$, $\sigma^z$, is a frame slot under the strict reading and a name under the census: the letter names the generator and the caret names the component. The structural label, $M_4^L$, $M_4^R$, $\Pi_1^A$, is a parameter and the caret rule admits it; 134 of the 4,238 are of this form. The label in parentheses, ${}^{(l)}$, ${}^{(\mathrm{adj})}$, and the upright label, $S^{\mathrm{c}}$, $F^{\mathrm{dual}}$, are names in every reading. The compound exponent, $x^{2n}$, is a power that the power screen missed. One case is not a caret question at all: $G^{\mathrm L}$ and $G^{\mathrm R}$ raise a role, which belongs to the next section.

*The Upper-Index Problem* reports 0 raised frame slots in physics: 8 carets on the Greek letters, all legitimate. That screen keeps only the carets on $i,j,k,l$ and on the Greek letters, and it discards every power, grade, coframe and dual. The census here keeps all of them. The two figures measure different populations: the 72 carets that the earlier screen counted on those letters are 0.18% of 40,554, and the rewritten screen keeps 8. The screen does not read $x$, $y$, $z$ or $a$, so a raised $\sigma^z$ or $T^a$ falls outside it and is recorded here as a raised name.

### Lower

Two classes of low mark are open.

| Class | What it carries | Count | Share |
|---|---|---:|---:|
| Upright role name | $\mathrm{tot}$, $\mathrm b$, $\mathrm L$, $\mathrm r$ | 5,784 | 4.9% |
| Operator or derivative index | $\sum_\mu$, $\partial/\partial Q_\mu$ | 4,316 | 3.7% |

#### The upright role name

The upright role names are the low counterparts of the names above. The census counts the pure form, a subscript whose whole content is a word; a further 1,269 subscripts put a role beside a frame slot, $s_{\mathrm{tot},z}$ or $T_{\mathrm b,1}$, and those are counted in the grouped class. The pure forms use 194 distinct words, and eight of them carry 58.7% of the 5,784.

| Role | Count | Share | Typical use |
|---|---:|---:|---|
| $\mathrm b$ | 946 | 15.9% | boost |
| $\mathrm L$ | 748 | 12.6% | Lorentz, or left |
| $\mathrm r$ | 504 | 8.5% | rotation, or real |
| $\mathrm{tot}$ | 472 | 7.9% | the total |
| $\mathrm{mod}$ | 277 | 4.7% | a modified quantity |
| $\mathrm f$ | 270 | 4.5% | flavour, or final |
| $\mathrm{cl}$ | 168 | 2.8% | the classical sector |
| $\mathrm{kin}$ | 111 | 1.9% | the kinematic sector |

The open question is whether a role such as $\mathrm{tot}$ or $\mathrm L$ is a name, which the rule would raise, or a label of a slot, which the rule keeps low. The convention gives both readings. It says that a subscript is "a label, as in $\tilde U_{\mathrm r}$", which keeps the role low, and it also says that a caret marks "a name", which a word such as $\mathrm{tot}$ plainly is. The corpus has chosen the low reading almost everywhere: 5,784 low against 9 raised, the raised ones being $G^{\mathrm L}$ and $G^{\mathrm R}$ (four each) and $T_{\mu\nu}^{\mathrm{tot}}$ (one) in two articles. So the practice is settled but the rule is not, and a reader who applies the caret rule to a role will produce $s^{\mathrm{tot}}$ where the corpus writes $s_{\mathrm{tot}}$.

#### The operator or derivative index

The operator indices are the indices of a sum or a derivative. They are not frame slots, because no object carries them; they are not names, because they range over a set; and the rule does not name them. The corpus writes them low without exception, and the heights are uniform enough that the class is stable across articles.

| Context | Count | Example |
|---|---:|---|
| Sum subscript | 2,654 | $\sum_{\mu,\nu}$, $\sum_{i=1}^{n}$ |
| — of which a range | 197 | $\sum_{i=1}^{n}$ |
| Derivative denominator | 2,163 | $\partial/\partial Q_\mu$ |
| Evaluation bar | 204 | $\big|_{t=0}$ |

The census puts the class at 4,316; the two families alone give 4,817, or 4,620 once the 197 ranges are set aside, which is 7% above it. The operator-label carve-out does not reach them: $\partial_n$ names a degree and $\partial_v$ a place, while $\sum_\mu$ and $\partial/\partial Q_\mu$ range over a set. A third kind of low mark is the honest description.

### What a decision would change

| Decision | Marks moved | Raised share |
|---|---|---:|
| The census as it stands | 0 | 25.3% |
| A role is a name, so it rises | 5,784 low to raised | 28.9% |
| A colour, gauge or spin index is a frame slot, so it falls | about 300 raised to low | 25.1% |
| Both of the last two | 5,484 net to raised | 28.7% |
| An operator index is a third kind of low mark | 0 | 25.3% |

Two of the corrections to the name class, the transpose and the missed powers, move no mark between the heights: they reclassify a caret without changing it, so the corpus share stays at 25.3% and the open count falls from 4,238 to about 3,370. The colour correction is different: it would lower the 300 carets it names, which is the one change that pulls against the role question.

## Validated

### Upper

The rule validates two jobs of the caret: the power and the mark.

| Class | What it carries | Count | Share |
|---|---|---:|---:|
| Power | an exponent: ${}^{2}$, ${}^{k}$, ${}^{-1}$, $e^{i\alpha}$ | 23,850 | 59.4% |
| Mark | a conjugation or a sign: ${}^{*}$, ${}^{\natural}$, ${}^{\dagger}$, $^{\mathrm{fop}}$, ${}^{\pm}$ | 12,065 | 30.0% |
| Both | | 35,915 | 89.4% |

The single power ${}^{2}$ accounts for 18,001 carets: 45% of all carets and 75% of the powers. The next powers are ${}^{3}$ (1,244), ${}^{-1}$ (880) and ${}^{4}$ (818).

The five commonest marks carry 86% of that class.

| Mark | Count |
|---|---:|
| ${}^{*}$ | 5,405 |
| ${}^{\natural}$ | 2,524 |
| ${}^{\dagger}$ | 1,095 |
| $^{\mathrm{fop}}$ | 1,006 |
| $^{\mathrm{fop}\dagger}$ | 407 |

| Validated caret | Meaning |
|---|---|
| $e^\lambda$, $2^k$, $(-1)^k$ | powers |
| ${}^{*}$, ${}^{\natural}$, ${}^{\dagger}$ | conjugation marks |
| $^{\mathrm{fop}}$, ${}^{\pm}$ | an operator label and a sign |

### Lower

The rule validates five jobs of the low mark.

| Class | What it carries | Count | Share |
|---|---|---:|---:|
| Frame slot, Latin | $e_t$, $e_x$, $x_k$, $\gamma_i$ | 42,805 | 36.2% |
| Numeric count | $Q_1$, $Q_2$, $M_2$ | 26,901 | 22.8% |
| Grouped or compound | $F_{\mu\nu}$, $g_{\mu\nu}$, $s_{\mathrm{tot},z}$ | 13,591 | 11.5% |
| Sign or mark | $M_+$, $M_-$ | 13,075 | 11.1% |
| Frame slot, Greek | $\mu$, $\nu$, $\rho$, $\lambda$ | 11,628 | 9.8% |
| All five | | 108,000 | 91.4% |

The frame slots are the largest class. Latin and Greek slots together are 54,433 marks, or 46% of the low marks.

| Validated form | Meaning |
|---|---|
| $x_\mu$, $A_\mu$, $\vec e_i$, $\gamma_i$ | a coordinate, a component, a basis vector, a gamma |
| $\varepsilon_{ijk}$, $\delta_{ij}$ | a sign symbol, with the indices low |
| $\sum_i$, $\sum_{\mu,\nu}$ | a contraction, written as an explicit sum |

## Further Reading

- [The Upper-Index Problem: The Caret Rule and the Corpus](the-upper-indexes-problem.html) — the rule, the screens, and what still fails.
- [Operator and Calculus Conventions](../articles_physics/conventions-of-the-operators-and-the-calculus.html) — the rule in its original wording.
- [Index, Notation and Corpus Conventions](../articles_maths/conventions-of-the-indices-the-notation-and-the-corpus.html) — the same rule for the mathematical corpus.
- [Matrix Representations: The Restructuring Table](matrix-representations-restructuring-table.html) — the naming pass that gave $M_4^L$ and $M_4^R$ their carets.
