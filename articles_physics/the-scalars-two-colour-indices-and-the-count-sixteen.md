# __The Scalar's Two Indices: Two Colour, One Trace, and the Count Sixteen__

## Introduction

**The question.** How many real components does the scalar have, and which of its labels does the group act on?

**The answer.**

$$
\boxed{\;Ξ:\ \underbrace{4\times4}_{\text{colour pair, Hermitian}}\ \Longrightarrow\ 16\ \text{real}=\underbrace{15}_{\mathbf{15}}+\underbrace{1}_{\mathbf1};\qquad \dim\mathrm{SU}(4)=15 .\;}
$$

**The fifteen is the algebra's, and it is where the count starts.** A traceless Hermitian $4\times4$ has $16-1=15$ real parameters, which is $\dim\mathrm{SU}(4)$ — **the Hermitian matrices are $i\mathfrak{su}(4)$ and the algebra is its anti-Hermitian partner, so what matches is the dimension and not the space.** The trace is one more real parameter, and $Ξ$ may carry it. **$15+1=16$, and there is nowhere else for the count to go.**

**What this article does.** It counts the components, names the two labels, says why Hermiticity is forced, and states what the counting does not fix.

**What it does not do.** It writes no potential and no mass. [The Primordial Potential](the-primordial-potential-one-symmetric-minimum-above-m-c.html) writes the potential; [The Lagrangian and the Scalar Matrix](the-lagrangian-and-the-scalar-matrix-one-field-one-commutator-four-quartics.html) writes the kinetic term.

## The Representation, Read Off the Indices

**A $4\times4$ matrix carries one lower and one upper colour index, and that product is reducible.**

$$
\mathbf4\otimes\bar{\mathbf4}=\mathbf{15}\oplus\mathbf1,
\qquad
15+1=16 .
$$

**The sixteen is the number of real parameters of a Hermitian matrix**, and the split says what the group does to them. The $\mathbf1$ is the trace, $\operatorname{tr}Ξ$; the $\mathbf{15}$ is the traceless part, which is the adjoint. **Both pieces are carried by the same field, and the reason the field is a matrix and not a vector is one line**: the contraction $\bar\xi Ξ\xi$ is a singlet of $\bar{\mathbf4}\otimes\mathbf4$, and the singlet of that product is the matrix itself.

**Why this and not the $\mathbf4$.** The mass operator decides it, and the argument is two lines:

$$
\bar\xiΞ\xi\to\mathbf1
\quad\Longleftrightarrow\quad
\bar{\mathbf4}\otimesΞ\otimes\mathbf4\supset\mathbf1
\quad\Longleftrightarrow\quad
Ξ\in\bar{\mathbf4}\otimes\mathbf4 .
$$

**And $\mathbf4\otimes\mathbf4=\mathbf6\oplus\mathbf{10}$ contains no $\bar{\mathbf4}$** — the $\mathbf{10}$ is the symmetric part and the $\mathbf6$ the antisymmetric, $10+6=16$, and neither is the $\bar{\mathbf4}$ — so a scalar in the fundamental forms no mass operator with one $\bar\xi$ and one $\xi$. **The scalar's colour structure is not a choice; it is the existence of the Yukawa sector.** [The Scalar Content](the-scalar-content-one-matrix-and-ten-survivors.html) records the census.

**Three counts that must not be confused.**

| count | number | what it is |
| --- | --- | --- |
| real components of the Hermitian matrix | $\mathbf{16}$ | the field's degrees of freedom |
| complex entries of a general $4\times4$ | $16$ | *not* this field: Hermiticity halves it to $16$ real, not $32$ |
| generators of $\mathrm{SU}(4)$ | $15$ | the traceless part |

**The middle row is the trap.** Sixteen complex entries is a general matrix with $32$ real parameters; a Hermitian matrix has sixteen real. **A count of $32$ has forgotten the dagger, and any count larger than that has multiplied by an index that no generator acts on.**

## Why Hermitian, Three Ways

**The count of sixteen is a statement about a Hermitian matrix, so Hermiticity is not decoration and the article owes the argument.**

**First, from the mass operator.** Write the Yukawa term as $X+y^{*}X^{†}$ with $X=y\,\bar\xi Ξ\xi$. **The conjugate term carries $Ξ^{†}$ where the first carries $Ξ$, so the sum depends on the two only through**

$$
\tfrac12\bigl(Ξ+Ξ^{†}\bigr),
$$

**and an anti-Hermitian part cancels between the halves.** So the field the fermions couple to is the Hermitian part, and an anti-Hermitian matrix would be a field with no Yukawa coupling and therefore no mass. **The ledger does not carry a field it cannot mass.**

**Second, from the potential.** $\operatorname{tr}Ξ^{2}$ and $\operatorname{tr}Ξ^{4}$ are real only for Hermitian $Ξ$. For a general complex matrix the invariant of degree two is $\operatorname{tr}Ξ^{†}Ξ$, which is not $\operatorname{tr}Ξ^{2}$, and every quartic would have to carry its own dagger. **The corpus's potential is written in the traces without daggers, and that writing is a statement that the field is Hermitian.**

**And the count of equations follows the count of components.** Varying a Hermitian $Ξ$ and varying $Ξ^{†}$ give the same equation, not a conjugate pair, so the sixteen components give sixteen equations and not half of thirty-two. **That is [The Lagrangian and the Scalar Matrix](the-lagrangian-and-the-scalar-matrix-one-field-one-commutator-four-quartics.html)'s observation, and it is the third reason the same sixteen appears in every count of this field.**

## The Two Labels

**What a component carries, and what acts on it.**

| label | range | acted on by the group |
| --- | --- | --- |
| the colour row | $1,\dots,4$ | yes, $Ξ\mapsto UΞ U^{\dagger}$ |
| the colour column | $1,\dots,4$ | yes, the same transformation |

**Two labels, both gauged, and that is the whole list.** There is no third index on $Ξ$: not a copy, not a family, not a colour–anticolour pair beyond the two already named.

**Why no generator acts on a third index, stated as the declaration it is.** The symmetry group of the model is $\mathrm{SU}(4)$, and its fifteen generators act on the two colour indices and on nothing else. **The reason is not that a third index would need a sixteenth generator**: a $\mathrm{U}(1)$ acting on a new label would not have to enlarge $\mathrm{SU}(4)$ at all, and "fifteen is all the room there is" is a statement about the dimension of one factor, not about how many factors a model may have. **The reason is that the declaration names one factor.** A second factor acting on a new label is a different model, and this article counts this one.

**And the copy index is the case that shows the choice is a ledger entry and not a theorem.** The model does carry an ungauged two-valued label, $α=1,2$, and **it sits on the fermion and on the Yukawa matrix, not on $Ξ$**: $\mathcal L_Y=y_{αβ}\,\bar\xi^{α†}Ξ\xi^{β}$, with $Ξ$ a singlet under $α$. **A copy index on $Ξ$ would make the count sixty-four rather than sixteen, and that is a different model** — one with a scalar matrix per copy instead of one shared matrix. [The Yukawa Sector](the-yukawa-sector-of-the-su4-model-one-matrix-and-its-diagonalisation.html) says why the index sits where it does. **Sixteen is the count of the declared field, and the declaration is what fixes it.**

**The colour pair does double duty, and that is why the matrix is not extravagant.** The same two indices give the gauge–scalar vertex its commutator and the Yukawa operator its singlet. **The group acts by conjugation, $Ξ\mapsto UΞU^{†}$, so the covariant derivative is a commutator and not a multiplication**:

$$
D_μΞ=\partial_μΞ-ig_4[A_μ,Ξ],
$$

**and the bracket is forced by the two-index structure rather than assumed.** **One structure, two jobs**, and the sixteen is the smallest count that does both.

## The Count, Twice

**Once as entries, once as a decomposition.**

| bookkeeping | count |
| --- | --- |
| diagonal entries, real | $4$ |
| off-diagonal entries, one complex pair per unordered pair | $6\times2=12$ |
| **total** | $\mathbf{16}$ |

| block | real |
| --- | --- |
| the trace $\mathbf1$ | $1$ |
| the traceless $\mathbf{15}$ | $15$ |
| **total** | $\mathbf{16}$ |

**The two tables agree, and the agreement is the check.** Six pairs above the diagonal give twelve real, plus four real diagonal entries: sixteen. **No component is double-counted and none is missing.**

**Degrees of freedom and components are the same number here.** A real scalar has one degree of freedom per component, unlike a fermion, so sixteen components are sixteen degrees of freedom before any eating. **The vector case is where the two differ**, and [The Sixteen Above $M_C$](the-sixteen-above-m-c-massless-vector-like-and-what-that-costs.html) works that difference out for the fermions.

## What the Counting Does Not Fix

**Four things the representation leaves open, stated so no later article has to assume them.**

- *The potential.* Two quadratics and four quartics, with six free coefficients: the traceless pair, and the trace's own quadratic and two quartics. **The representation fixes how many terms there are and not what they are**; the counting is silent on signs.
- *The mass.* $\mu^{2}$ is a parameter. Whether the origin is a minimum is a statement about its sign, not about the count.
- *The vacuum's shape.* Any traceless diagonal form is available to a Hermitian matrix. **The count does not choose**, and [The Primordial Potential](the-primordial-potential-one-symmetric-minimum-above-m-c.html) shows that the choice is what decides how many directions the transition eats.
- *The Yukawa matrix.* Its entries are free, and the representation fixes only that the operator exists.

**What the counting does fix, and it is worth stating positively.** One Goldstone boson per broken generator and no more, so **the count that matters is a ceiling: sixteen components can feed up to twelve generators**, and twelve is the most any traceless vacuum in this field can break — every traceless Hermitian matrix is conjugate to a diagonal one, and four distinct eigenvalues leave $\mathrm{U}(1)^{3}$, so $15-3=12$. **So whatever shape the potential chooses, the multiplet is large enough to feed it**, and a smaller multiplet might not have been.

**The six is the potential's number and not the representation's.** For the declared vacuum the stabiliser is nine-dimensional and the count is $15-9=6$; [The Primordial Potential](the-primordial-potential-one-symmetric-minimum-above-m-c.html) derives the shape and [The Breaking of the Primordial Force](the-breaking-of-the-primordial-force-and-the-mass-of-the-six-leptoquarks.html) reads the spectrum. **A reader who carries $6$ away from this article should carry the vacuum with it.** The ten components that survive the eating are counted in [The Scalar Content](the-scalar-content-one-matrix-and-ten-survivors.html).

## The Checks

| claim | check | result |
| --- | --- | --- |
| the dimension of $\mathbf4\otimes\bar{\mathbf4}$ | $4\times4$ | $16$ |
| its decomposition | $\mathbf{15}\oplus\mathbf1$ | $15+1=16$ |
| the real parameters of a Hermitian $4\times4$ | $4+6\times2$ | $16$ |
| the real parameters of a general $4\times4$ | $16$ complex | $32$, **not this field** |
| the generators | $4^{2}-1$ | $15$ |
| the mass operator's requirement | $\bar{\mathbf4}\otimesΞ\otimes\mathbf4\supset\mathbf1$ | $Ξ\in\bar{\mathbf4}\otimes\mathbf4$ |
| the quartet's exclusion | $\mathbf4\otimes\mathbf4$ | $\mathbf{10}$ symmetric $+\,\mathbf6$ antisymmetric, no $\bar{\mathbf4}$ |
| the anti-Hermitian part | cancels in $X+X^{†}$ | no Yukawa coupling, no mass |
| the largest eaten count any vacuum demands | $15-3$, four distinct eigenvalues | $12$, and $12\le16$ |
| the eaten count, declared vacuum | $15-9$ | $6$, the potential's |

**The last two rows differ on purpose.** The representation supplies the ceiling, twelve; the vacuum supplies the actual count, six. **Reading the second as a consequence of the counting is the one mistake this table is built to prevent**, and the section above states the same thing in words.

## Summary

**Sixteen real components: fifteen from the algebra and one from the trace.** The representation is $\mathbf{15}\oplus\mathbf1=\mathbf4\otimes\bar{\mathbf4}$ in the colour indices, forced by the existence of the mass operator and not chosen for convenience.

**Two labels, both gauged.** No copy index, no family index on $Ξ$: the model's one ungauged label sits on the fermion and on the Yukawa matrix, and a copy index on $Ξ$ would be a different model with sixty-four components.

**Thirty-two is the number to avoid, and it is the one that looks right.** It is the count of a general complex $4\times4$, a different field from a Hermitian one, and **the coupling article reads the count straight off the beta coefficient**: sixteen real components give $b_0=\tfrac{26}{3}$, thirty-two give $8$, and a two-valued label on the matrix gives $\tfrac{20}{3}$ — **each rung of that ladder moves $b_0$ by more than the two-loop term the running omits**, which is why the count has to be this one and not one step up.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $Ξ$ | the scalar, a Hermitian $4\times4$ |
| $\mathbf{15}\oplus\mathbf1$ | $\mathbf4\otimes\bar{\mathbf4}$, the adjoint plus the trace |
| $\bar{\mathbf4}$ | the conjugate fundamental, the index carried by $\bar\xi$ |
| $U$ | the $\mathrm{SU}(4)$ element acting as $Ξ\mapsto UΞ U^{\dagger}$ |

## Further Reading

- [The Scalar Content](the-scalar-content-one-matrix-and-ten-survivors.html). The same field counted with the eating, and the ten that survive.
- [The Primordial Potential](the-primordial-potential-one-symmetric-minimum-above-m-c.html). The potential this count leaves undetermined, written.
- [The Lagrangian and the Scalar Matrix](the-lagrangian-and-the-scalar-matrix-one-field-one-commutator-four-quartics.html). The kinetic term for this field, and the commutator its two colour indices force.
- [The $\mathrm{SU}(4)$ Model: Four Colours, Fifteen Generators, One Declaration](the-su4-model-four-colours-fifteen-generators-one-declaration.html). The fifteen the count starts from.
