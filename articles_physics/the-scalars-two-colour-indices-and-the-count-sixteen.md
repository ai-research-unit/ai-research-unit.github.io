# __The Scalar's Two Indices: Two Colour, One Trace, and the Count Sixteen__

## Introduction

**The question.** How many real components does the scalar have, and which of its labels does the group act on?

**The answer.**

$$
\boxed{\;\Phi:\ \underbrace{4\times4}_{\text{colour pair, Hermitian}}\ \Longrightarrow\ 16\ \text{real}=\underbrace{15}_{\mathbf{15}}+\underbrace{1}_{\mathbf1};\qquad \dim\mathrm{SU}(4)=15 .\;}
$$

**The fifteen is the algebra's, and it is where the count starts.** A traceless Hermitian $4\times4$ has $16-1=15$ real parameters, which is $\dim\mathrm{SU}(4)$. The trace is one more real parameter, and $\Phi$ may carry it. **$15+1=16$, and there is nowhere else for the count to go.**

**What this article does.** It counts the components, names the two labels, says why Hermiticity is forced, and states what the counting does not fix.

**What it does not do.** It writes no potential and no mass. [The Primordial Potential](the-primordial-potential-one-symmetric-minimum-above-m-c.html) writes the potential; [The Lagrangian and the Scalar Matrix](the-lagrangian-and-the-scalar-matrix-one-field-one-commutator-two-quartics.html) writes the kinetic term.

## The Representation, Read Off the Indices

**A $4\times4$ matrix carries one lower and one upper colour index, and that product is reducible.**

$$
\mathbf4\otimes\bar{\mathbf4}=\mathbf{15}\oplus\mathbf1,
\qquad
15+1=16 .
$$

**The sixteen is the number of real parameters of a Hermitian matrix**, and the split says what the group does to them. The $\mathbf1$ is the trace, $\operatorname{tr}\Phi$; the $\mathbf{15}$ is the traceless part, which is the adjoint. **Both pieces are carried by the same field**, and the mass operator uses only the singlet.

**Why this and not the $\mathbf4$.** The mass operator decides it, and the argument is two lines:

$$
\bar\xi\Phi\xi\to\mathbf1
\quad\Longleftrightarrow\quad
\bar{\mathbf4}\otimes\Phi\otimes\mathbf4\supset\mathbf1
\quad\Longleftrightarrow\quad
\Phi\in\bar{\mathbf4}\otimes\mathbf4 .
$$

**And $\mathbf4\otimes\mathbf4=\mathbf6\oplus\mathbf{10}$ contains no $\bar{\mathbf4}$**, so a scalar in the fundamental forms no mass operator with one $\bar\xi$ and one $\xi$. **The scalar's colour structure is not a choice; it is the existence of the Yukawa sector.** [The Scalar Content](the-scalar-content-one-matrix-and-ten-survivors.html) records the census.

**Three counts that must not be confused.**

| count | number | what it is |
| --- | --- | --- |
| real components of the Hermitian matrix | $\mathbf{16}$ | the field's degrees of freedom |
| complex entries of a general $4\times4$ | $16$ | *not* this field: Hermiticity halves it to $16$ real, not $32$ |
| generators of $\mathrm{SU}(4)$ | $15$ | the traceless part |

**The middle row is the trap.** Sixteen complex entries is a general matrix with $32$ real parameters; a Hermitian matrix has sixteen real. **A count of $32$ has forgotten the dagger, and any count larger than that has multiplied by an index that no generator acts on.**

## The Two Labels

**What a component carries, and what acts on it.**

| label | range | acted on by the group |
| --- | --- | --- |
| the colour row | $1,\dots,4$ | yes, $\Phi\mapsto U\Phi U^{\dagger}$ |
| the colour column | $1,\dots,4$ | yes, the same transformation |

**Two labels, both gauged, and that is the whole list.** There is no third index on $\Phi$: not a copy, not a family, not a colour–anticolour pair beyond the two already named. **A third index would multiply the count and nothing in the algebra would act on it**, which is the definition of a label that costs components and buys nothing.

**Why the group cannot act on a third index.** A generator acting on it would be a sixteenth generator, and the algebra has fifteen. **The group is fixed by the algebra's dimension**, so any further label is necessarily ungauged, and an ungauged label on a Hermitian matrix is not a degree of freedom: it is a bookkeeping device, and the corpus does not use one here.

**The colour pair does double duty, and that is why the matrix is not extravagant.** The same two indices give the gauge–scalar vertex its commutator and the Yukawa operator its singlet. **One structure, two jobs**, and the sixteen is the smallest count that does both.

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

- *The potential.* One quadratic and two quartics, with three free coefficients. **The representation fixes how many terms there are and not what they are**; the counting is silent on signs.
- *The mass.* $\mu^{2}$ is a parameter. Whether the origin is a minimum is a statement about its sign, not about the count.
- *The vacuum's shape.* Any traceless diagonal form is available to a Hermitian matrix. **The count does not choose**, and [The Primordial Potential](the-primordial-potential-one-symmetric-minimum-above-m-c.html) shows that the choice is what decides how many directions the transition eats.
- *The Yukawa matrix.* Its entries are free, and the representation fixes only that the operator exists.

**What the counting does fix, and it is worth stating positively.** The number of eaten directions is six: one per broken generator, and never more than the six the stabiliser leaves. **A scalar with sixteen components can feed six Goldstones and cannot feed seven**, because six is the number of generators that do not commute with the vacuum.

## The Checks

| claim | check | result |
| --- | --- | --- |
| the dimension of $\mathbf4\otimes\bar{\mathbf4}$ | $4\times4$ | $16$ |
| its decomposition | $\mathbf{15}\oplus\mathbf1$ | $15+1=16$ |
| the real parameters of a Hermitian $4\times4$ | $4+6\times2$ | $16$ |
| the real parameters of a general $4\times4$ | $16$ complex | $32$, **not this field** |
| the generators | $4^{2}-1$ | $15$ |
| the mass operator's requirement | $\bar{\mathbf4}\otimes\Phi\otimes\mathbf4\supset\mathbf1$ | $\Phi\in\bar{\mathbf4}\otimes\mathbf4$ |
| the quartet's exclusion | $\mathbf4\otimes\mathbf4$ | $\mathbf6\oplus\mathbf{10}$, no $\bar{\mathbf4}$ |
| the eaten count | $15-9$ | $6$ |

## Summary

**Sixteen real components: fifteen from the algebra and one from the trace.** The representation is $\mathbf{15}\oplus\mathbf1=\mathbf4\otimes\bar{\mathbf4}$ in the colour indices, forced by the existence of the mass operator and not chosen for convenience.

**Two labels, both gauged.** No copy index, no family index on $\Phi$: a third label would multiply the count and no generator would act on it.

**Thirty-two is the number to avoid, and it is the one that looks right.** It is the count of a general complex $4\times4$, which is a different field from a Hermitian one, and it is the first step on a ladder that ends in a negative $b_0$.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\Phi$ | the scalar, a Hermitian $4\times4$ |
| $\mathbf{15}\oplus\mathbf1$ | $\mathbf4\otimes\bar{\mathbf4}$, the adjoint plus the trace |
| $\bar{\mathbf4}$ | the conjugate fundamental, the index carried by $\bar\xi$ |
| $U$ | the $\mathrm{SU}(4)$ element acting as $\Phi\mapsto U\Phi U^{\dagger}$ |

## Further Reading

- [The Scalar Content](the-scalar-content-one-matrix-and-ten-survivors.html). The same field counted with the eating, and the ten that survive.
- [The Primordial Potential](the-primordial-potential-one-symmetric-minimum-above-m-c.html). The potential this count leaves undetermined, written.
- [The Lagrangian and the Scalar Matrix](the-lagrangian-and-the-scalar-matrix-one-field-one-commutator-two-quartics.html). The kinetic term for this field, and the commutator its two colour indices force.
- [The $\mathrm{SU}(4)$ Model: Four Colours, Fifteen Generators, One Declaration](the-su4-model-four-colours-fifteen-generators-one-declaration.html). The fifteen the count starts from.
