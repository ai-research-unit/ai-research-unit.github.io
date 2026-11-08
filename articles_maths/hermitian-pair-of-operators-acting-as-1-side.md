# __Hermitian pair of operators acting as 1 side__

## Introduction: One Operator and Its Adjoint, on One Side

**The pair.** An operator is read together with its adjoint, and the reading is a pair. The biquaternion algebra carries four forms, so it carries four adjoints of a linear map, and each of the four lands somewhere: the associate $(F)^{\approx}$ exchanges the two sides, the adjoint of the quaternionic form $(F)^{\natural}$ keeps the side and carries each parameter through $\natural$. A Hermitian pair is therefore written in two placements. Either both members multiply on the left, and the pair acts as **1 side**; or one member multiplies on the left and the other on the right, and the pair acts as **2 sides**. This article is the first placement. The second is *Hermitian pair of operators acting as 2 side*, and the bridge between the two is one identity of *The Transposition of the Two Sides*.

**The two actors.** The whole subject is built from two maps of $\mathbb{B}$ into itself, the left multiplication $L_{\tilde Q}(\tilde X)=\tilde Q\tilde X$ and the right multiplication $R_{\tilde Q}(\tilde X)=\tilde X\tilde Q$. They are the two regular families of *Operators Acting 1 Side*. Both are $\mathbb{C}$-linear and injective, both are units when $\tilde Q$ is a unit, and they commute with each other, $L_{\tilde Q}R_{\tilde P}=R_{\tilde P}L_{\tilde Q}$. In a pair the two actors play the two roles: one acts on the argument, the other on the other side of it, and the tie between their parameters is what makes the pair Hermitian.

**What the article does.** Five steps. First the two actors and their laws, because every later display is a word in them. Second the pair of equations that a two-side Hermitian pair writes: one equation with the factor on the left, one with the factor on the right, both on the same unknown. Third the transposition, which replaces the right member by a left one and turns that pair of equations into a pair of equations whose two members both multiply on the left; the price is one reversal, applied to the unknown and to the data together. Fourth the one-side pair proper, $(L_{\tilde Q},L_{\tilde Q^{\natural}})$, whose product is a scalar; that product is the passage from two first-order conditions to one second-order operator, and the scalar is the mass. Fifth what the placement does not give: the one-side pair does not preserve the two Hermitian halves, so the stability of the halves is the warrant of the two-side placement and of no other.

The notation is that of *Operator Family Conventions*: $L_{\tilde Q}$ and $R_{\tilde Q}$ the two regular actors, $L_{\tilde Q}R_{\tilde Q_2}$ the two-sided operator, $\mathrm{Sd}_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{\ast}}$ the member of *Hermitian pair of operators acting as 2 side*, $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{\Phi}$ the Hermitian and anti-Hermitian halves, and $\langle\tilde Q\rangle_{\natural}$ the quaternionic norm. The frame is $e_t,\vec e_x,\vec e_y,\vec e_z$, with the products $\vec e_x\vec e_y=\vec e_z$, $\vec e_y\vec e_z=\vec e_x$, $\vec e_z\vec e_x=\vec e_y$ and $\vec e_x^2=\vec e_y^2=\vec e_z^2=-e_t$. The article is pure algebra. No step uses a topology, a distance or a limit.

## The Two Actors

**Definition.** For $\tilde Q\in\mathbb{B}$,

$$
L_{\tilde Q}(\tilde X)=\tilde Q\,\tilde X,\qquad R_{\tilde Q}(\tilde X)=\tilde X\,\tilde Q .
$$

The letter names the action and the subscript names its element: $L_{\tilde Q}$ multiplies on the left and $R_{\tilde Q}$ on the right. Both maps are $\mathbb{C}$-linear in $\tilde X$ and additive in $\tilde Q$, and both are injective, because the unit probes the parameter: $L_{\tilde Q}(e_t)=\tilde Q$ and $R_{\tilde Q}(e_t)=\tilde Q$.

**The two laws.** $L_{\tilde Q}L_{\tilde P}=L_{\tilde Q\tilde P}$ and $R_{\tilde Q}R_{\tilde P}=R_{\tilde P\tilde Q}$. The first is a representation of the algebra, the second an anti-representation, and the asymmetry is the whole content of the difference between the two sides. The two families commute across the sides,

$$
L_{\tilde Q}R_{\tilde P}=R_{\tilde P}L_{\tilde Q},
$$

because both composites send $\tilde X$ to $\tilde Q\tilde X\tilde P$; associativity is the only input. A pair made of one member of each family is therefore unordered, while a pair made of two members of one family is ordered.

**The two adjoints that stay on one side, and the one that does not.** Every form carries its adjoint (*Adjoint Pair of $L$ and $R$ Operators*), and on the regular actors the rule is short:

$$
(L_{\tilde Q})^{\approx}=R_{\tilde Q},\qquad (L_{\tilde Q})^{\natural}=L_{\tilde Q^{\natural}},\qquad (L_{\tilde Q})^{\natural\ast}=R_{\bar{\tilde Q}} .
$$

Read the three: the associate moves the parameter across the argument and exchanges the two sides, the adjoint of the quaternionic form keeps the side and replaces the parameter by $\tilde Q^{\natural}$, and the adjoint of the quaternionic sesquilinear form moves the side and conjugates. The plain sesquilinear form completes the list in the same pattern, $(L_{\tilde Q})^{\ast}=L_{\tilde Q^{\ast}}$.

**The consequence for a pair.** A Hermitian pair is the pair of an actor with its adjoint, and the adjoint can be chosen to stay on the same side or to move to the other. Those are exactly the two placements. The tie is the involution of the form; the placement is the side on which the adjoint is asked to land.

## The Pair of Equations

**The system.** Let $\tilde Q\in\mathbb{B}$ be given, together with two data $\tilde Y,\tilde Z\in\mathbb{B}$, and let $\tilde X$ be the unknown. A Hermitian pair acting as 2 sides writes the two equations

$$
L_{\tilde Q}\tilde X=\tilde Y,\qquad
R_{\tilde Q^{\ast}}\tilde X=\tilde Z,
$$

that is, in the multiplication of the algebra,

$$
\tilde Q\,\tilde X=\tilde Y,\qquad \tilde X\,\tilde Q^{\ast}=\tilde Z .
$$

The first equation uses the left actor, the second the right actor, and the second parameter is tied to the first: it is $\tilde Q^{\ast}$ and not an independent element. That tie is what makes the pair a pair and not a general two-sided operator, and the product of the two members is the member of the companion article, $L_{\tilde Q}R_{\tilde Q^{\ast}}=\mathrm{Sd}_{\tilde Q}$.

**Why it is one system and not two.** The two equations are imposed on one unknown, so they are consistent only on a condition, and the condition is read off at once. Multiplying the first equation on the right by $\tilde Q^{\ast}$ gives $\tilde Q\tilde X\tilde Q^{\ast}=\tilde Y\tilde Q^{\ast}$, and multiplying the second on the left by $\tilde Q$ gives the same left side, $\tilde Q\tilde X\tilde Q^{\ast}=\tilde Q\tilde Z$. The pair therefore has a solution only when

$$
\tilde Y\,\tilde Q^{\ast}=\tilde Q\,\tilde Z .
$$

The condition is also sufficient. For a unit $\tilde Q$ the first equation gives $\tilde X=\tilde Q^{-1}\tilde Y$, and this element satisfies the second exactly when $\tilde Q^{-1}\tilde Y\tilde Q^{\ast}=\tilde Z$, which is the display above; the solution is then unique. For a $\tilde Q$ that is not a unit the display is still necessary and no longer sufficient, because neither multiplication is surjective: the pair has either no solution at all, or a solution set that is one solution plus the left annihilator of $\tilde Q$, and that set is a copy of the annihilator and not a point.

**The order of the two.** The two members commute, so the pair of equations may be written in either order and the system is unchanged. This is not a detail: it is what allows the second equation to be replaced by an equivalent one without disturbing the first, which is the operation of the next section.

## Replacing the Right Actor by Its Transpose

**Theorem (the right actor is a left one in another frame).** For every $\tilde Q$,

$$
R_{\tilde Q^{\ast}}=\ast^{-1}L_{\tilde Q}\,\ast
\qquad\text{and}\qquad
R_{\tilde Q^{\ast}}=\natural^{-1}L_{\bar{\tilde Q}}\,\natural .
$$

*Proof.* A reversal satisfies $\tau(xy)=\tau(y)\tau(x)$ and $\tau L_{\tilde P}\tau^{-1}=R_{\tau(\tilde P)}$ (*The Transposition of the Two Sides*). Take $\tau=\ast$. The map $\ast$ is an involution and $\ast(\tilde Q^{\ast})=\tilde Q$, so the theorem gives $R_{\tilde Q^{\ast}}=\ast L_{\tilde Q}\ast^{-1}=\ast^{-1}L_{\tilde Q}\ast$. Take $\tau=\natural$. Then $\natural^{-1}=\natural$ and $\natural(\bar{\tilde Q})=\natural(\natural(\tilde Q^{\ast}))=\tilde Q^{\ast}$, so $R_{\tilde Q^{\ast}}=\natural L_{\bar{\tilde Q}}\natural^{-1}$.

**The pair of equations, rewritten.** Substituting the first identity in the second equation of the system gives

$$
\tilde Q\,\tilde X=\tilde Y,\qquad
\tilde Q\,\tilde X^{\ast}=\tilde Z^{\ast}.
$$

Both members now multiply on the left, by the **same** element $\tilde Q$. That is the rewriting: the right actor is gone, its parameter has been absorbed by the reversal, and what remains is two left multiplications separated by one application of $\ast$. In the other frame, with $\natural$, the second equation reads $\bar{\tilde Q}\,\natural(\tilde X)=\natural(\tilde Z)$.

**What the rewriting costs.** Two things, and both are visible in the display. The reversal falls on the unknown as well as on the data: the second equation constrains $\tilde X^{\ast}$ and not $\tilde X$, so it is **antilinear** in the unknown, while the first is linear. A pair of equations that was complex-linear in $\tilde X$ as a two-side pair has become one linear equation and one antilinear equation as a one-side pair. And the reversal falls on the data too: $\tilde Z$ is replaced by $\tilde Z^{\ast}$, so a solution of the rewritten pair is a solution of the original only when the data are carried along. Dropping either reversal gives an equation that is false for every noncentral parameter, which is the standing trap of *The Transposition of the Two Sides*, §*The Parameter*.

**The product of the rewritten pair.** Composing the two members in the order of the display returns the two-side operator,

$$
L_{\tilde Q}\bigl(\ast^{-1}L_{\tilde Q}\ast\bigr)=L_{\tilde Q}R_{\tilde Q^{\ast}}=\mathrm{Sd}_{\tilde Q},
$$

so the rewriting changes the reading and not the operator. This is the exact sense in which the two placements are one pair: the same composite, written once with one actor of each family and once with two actors of the left family and one reversal between them.

## The One-Side Pair

**Definition.** The pair

$$
\bigl(L_{\tilde Q},\,L_{\tilde Q^{\natural}}\bigr)
$$

is the Hermitian pair acting as 1 side. Both members multiply on the left, and the second is the adjoint of the first in the quaternionic form, $(L_{\tilde Q})^{\natural}=L_{\tilde Q^{\natural}}$. Since $\natural$ is $\mathbb{C}$-linear, the assignment $\tilde Q\mapsto(L_{\tilde Q},L_{\tilde Q^{\natural}})$ is complex-linear, and the family of pairs is a complex space of complex dimension four.

**Its pair of equations.** With the same unknown and two data,

$$
L_{\tilde Q}\tilde X=\tilde Y,\qquad L_{\tilde Q^{\natural}}\tilde X=\tilde Z,
\qquad\text{that is}\qquad
\tilde Q\,\tilde X=\tilde Y,\quad \tilde Q^{\natural}\tilde X=\tilde Z .
$$

Both equations are linear in $\tilde X$ and both multiply on the left. This is the placement in which the pair is a pair of first-order conditions of the same kind: no reversal, no conjugate-linear member, no data carried.

**Theorem (the pair composes to a scalar).** For every $\tilde Q$,

$$
L_{\tilde Q}L_{\tilde Q^{\natural}}=L_{\tilde Q\tilde Q^{\natural}}
=L_{\langle\tilde Q\rangle_{\natural}}=\langle\tilde Q\rangle_{\natural}\,\mathrm{id},
\qquad \langle\tilde Q\rangle_{\natural}=\sum_{\mu}Q_\mu^{2},
$$

and the scalar is central.

*Proof.* The first equality is the representation law, the second is the definition of the quaternionic norm as the product of an element with its natural conjugate, and the third reads the left multiplication by a central element as a scalar operator. The centre of $\mathbb{B}$ is $\mathbb{C}e_t$, so the composite is central for every parameter.

**The second order, and the mass.** A single left multiplication is a first-order operator: one factor, one action. The composite of the pair is a scalar operator, so the pair of two first-order conditions is one second-order operator whose value on every argument is a multiple of that argument. That is the algebraic shape of a second-order equation with a mass, and the mass is $\langle\tilde Q\rangle_{\natural}$. The norm is invariant under $\natural$, $\langle\tilde Q^{\natural}\rangle_{\natural}=\langle\tilde Q\rangle_{\natural}$, so the two members compose to the same scalar in either order and the pair is symmetric in its two members.

**When the composite vanishes.** $\langle\tilde Q\rangle_{\natural}=0$ exactly when $\tilde Q$ is a zero divisor, since the determinant of $L_{\tilde Q}$ is $\langle\tilde Q\rangle_{\natural}^{2}$, and the composite of the pair is then the zero operator. Composing the two equations gives nothing at that parameter: the pair is a pair of conditions whose product carries no information, and the two equations are then solved or not solved one at a time. The pair is non-degenerate exactly on the units, which is the complement of the zero-divisor cone.

**The $\ast$-tied pair, and why it is not this one.** The same construction with the other involution gives $(L_{\tilde Q},L_{\tilde Q^{\ast}})$, and its composite is $L_{\tilde Q\tilde Q^{\ast}}$. That element is Hermitian, $\ast(\tilde Q\tilde Q^{\ast})=\tilde Q\tilde Q^{\ast}$, so the composite lies in the half $\mathbb{B}_{\Psi}$ and not in the centre. The two pairs are therefore different objects: the $\natural$-pair composes to a scalar, and the $\ast$-pair composes to a Hermitian element. The corpus writes the $\natural$-pair for the one-side work and the $\ast$-pair inside the two-side operator, and the difference of the two composites is the reason.

## The Two-Component Reading

**A second reading of the same pair.** The pair of the preceding section was imposed on one unknown. It is imposed just as naturally on two, and the second reading is the one the physics corpus takes. On the sum $\mathbb{B}\oplus\mathbb{B}$ define

$$
\mathbb{D}_{\tilde Q}(\tilde X_1,\tilde X_2)=\bigl(L_{\tilde Q}\tilde X_2,\;L_{\tilde Q^{\natural}}\tilde X_1\bigr),
$$

so that the first component of the output is the first member of the pair applied to the second component of the input, and the second component of the output is the second member applied to the first. In blocks, with respect to the two summands,

$$
\mathbb{D}_{\tilde Q}=
\begin{pmatrix}0 & L_{\tilde Q}\\[2pt] L_{\tilde Q^{\natural}}&0\end{pmatrix}.
$$

The operator is $\mathbb{C}$-linear, it exchanges the two summands, and it is symmetric as a two-component operator: its two off-diagonal blocks are the adjoints of one another in the quaternionic form, so the matrix is its own transpose under the pairing that couples the components.

**Theorem (the pair squares to the norm).** For every $\tilde Q$,

$$
\mathbb{D}_{\tilde Q}^{2}
=\begin{pmatrix}L_{\tilde Q}L_{\tilde Q^{\natural}}&0\\[2pt]0&L_{\tilde Q^{\natural}}L_{\tilde Q}\end{pmatrix}
=\langle\tilde Q\rangle_{\natural}\,\mathrm{id}_{\mathbb{B}\oplus\mathbb{B}} .
$$

*Proof.* The square of an off-diagonal block matrix is the diagonal matrix of the two products, and each product is $L_{\langle\tilde Q\rangle_{\natural}}$ by the closure theorem of the preceding section. The scalar is central, so it acts on both summands in the same way.

**The pair of equations, as an eigenvalue problem.** With a scalar $\lambda$ the pair becomes

$$
\mathbb{D}_{\tilde Q}\Xi=\lambda\,\Xi,\qquad \Xi=(\tilde X_1,\tilde X_2),
$$

which entrywise is $L_{\tilde Q}\tilde X_2=\lambda\tilde X_1$ and $L_{\tilde Q^{\natural}}\tilde X_1=\lambda\tilde X_2$: each member of the pair acts on one component and returns a multiple of the other. The tie is the same in both readings; what changes is that the unknown is now a pair of elements and the two equations are no longer imposed on one of them.

**The second order, read off.** Applying the theorem to the eigenvalue problem gives $\langle\tilde Q\rangle_{\natural}\Xi=\lambda^{2}\Xi$, that is

$$
\bigl(\langle\tilde Q\rangle_{\natural}-\lambda^{2}\bigr)\tilde X_1=0,
\qquad
\bigl(\langle\tilde Q\rangle_{\natural}-\lambda^{2}\bigr)\tilde X_2=0 .
$$

The second-order equation for each component is therefore a **consequence** of the first-order pair, and it is obtained by squaring the pair and not by squaring any matrix or by introducing a second metric. Two first-order conditions, one second-order consequence, one central scalar: that is the whole of the mechanism, and it is the reason the pair is written at all.

**The instance of the physics corpus.** When the parameter of the pair is the biquaternionic gradient and $\langle\tilde Q\rangle_{\natural}$ is therefore the d'Alembertian, the eigenvalue problem above is the chiral pair of *The Dirac Equation in Biquaternionic Form*, and the squared display is the Klein–Gordon equation that article derives from it. The identification is exact and it needs nothing of this article but the two theorems: the closure of the pair and the square of the two-component operator. The physics article writes the same two blocks and the same square; what it adds is the meaning of the parameter, and the two letters it puts on the components.

**A limit of the identification, stated once.** The tie $\natural$ is the adjoint in the quaternionic form **on the algebra**, and that is a statement about elements. It is not by itself a statement about an adjoint on a space of fields: an adjoint there carries the sign of whatever the parameter carries, so a pair tied by $\natural$ at the element level may be skew in that reading and Hermitian only after a multiplication by $i$. The eigenvalue problem above is written at the element level and makes no claim about the space.

## What the Placement Does Not Give

**Proposition (the one-side pair does not preserve the halves).** $L_{\tilde A}$ maps $\mathbb{B}_{\Phi}$ into itself exactly when $\tilde A$ is a real scalar, and the same holds for $R_{\tilde A}$.

*Proof.* Immediate from *Hermitian pair of operators acting as 2 side*, §*The One-Sided Contrast*: for $\tilde X\in\mathbb{B}_{\Phi}$ one has $(\tilde A\tilde X)^{\ast}=-\tilde X\tilde A^{\ast}$, so the condition is $R_{\tilde A^{\ast}}=L_{\tilde A}$, whose solutions are the real scalars.

**The reading.** Neither member of the one-side pair preserves the halves except at a real scalar parameter, so the pair as a whole does not preserve them either. Sector stability is a property of the two-side placement: there the conjugate-linearity occurs once in each slot and cancels, and by the rigidity theorem of the companion article the operator that preserves both halves is exactly a real multiple of $\mathrm{Sd}_{\tilde Q}$. A reader who carries the word *stable* from one placement to the other asserts something false, and this section exists to prevent it.

**What the placement does give.** Three things, and they are the reason the placement is written at all. The pair is complex-linear in its parameter, so it lives in a complex four-dimensional family and its parameters can be superposed. Its composite is central, so the pair of two conditions is a scalar operator, and the scalar is the quaternionic norm. And both members act on the left, so a computation in the one-side placement uses one reversal at most, where the two-side placement uses the reversal in the parameter and the exchange of the sides.

## Summary

A Hermitian pair is an actor together with its adjoint, and the adjoint of a regular actor may be asked to stay on its side or to move to the other. Stay: the adjoint of the quaternionic form, $(L_{\tilde Q})^{\natural}=L_{\tilde Q^{\natural}}$, and the pair $(L_{\tilde Q},L_{\tilde Q^{\natural}})$ acts as 1 side. Move: the associate, $(L_{\tilde Q})^{\approx}=R_{\tilde Q}$, and with the adjoint of the sesquilinear form inside, the pair $(L_{\tilde Q},R_{\tilde Q^{\ast}})$ acts as 2 sides.

The two-side pair writes a pair of equations, one with the factor on the left and one with the factor on the right, both on the same unknown, consistent exactly when $\tilde Y\tilde Q^{\ast}=\tilde Q\tilde Z$ and then solving uniquely for a unit $\tilde Q$. The transposition $R_{\tilde Q^{\ast}}=\ast^{-1}L_{\tilde Q}\ast$ replaces the right member by a left one, so the pair of equations becomes

$$
\tilde Q\,\tilde X=\tilde Y,\qquad \tilde Q\,\tilde X^{\ast}=\tilde Z^{\ast},
$$

two left multiplications by the same element, at the price of one reversal on the unknown and one on the data. The product of the rewritten pair is the two-side operator again, $L_{\tilde Q}\ast^{-1}L_{\tilde Q}\ast=\mathrm{Sd}_{\tilde Q}$, so the two placements differ in the reading and not in the composite.

The one-side pair proper composes to a scalar, $L_{\tilde Q}L_{\tilde Q^{\natural}}=\langle\tilde Q\rangle_{\natural}\mathrm{id}$, and that scalar is the passage from two first-order conditions to one second-order operator: the mass. Read on two components rather than on one unknown, the pair is the off-diagonal operator $\mathbb{D}_{\tilde Q}$ with blocks $L_{\tilde Q}$ and $L_{\tilde Q^{\natural}}$, and $\mathbb{D}_{\tilde Q}^{2}=\langle\tilde Q\rangle_{\natural}\mathrm{id}$: the first-order pair squares to a central scalar, the second-order equation for each component follows, and with the gradient as the parameter the display is the chiral pair of the physics corpus and the squared display is the Klein–Gordon equation. The same construction with $\ast$ instead of $\natural$ composes to the Hermitian element $\tilde Q\tilde Q^{\ast}$ and not to a scalar, which is why the corpus keeps the two pairs apart. And neither member of the one-side pair preserves the two halves beyond a real scalar parameter, so sector stability belongs to the two-side placement alone.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_{\tilde Q}(\tilde X)=\tilde Q\tilde X$ | the left actor |
| $R_{\tilde Q}(\tilde X)=\tilde X\tilde Q$ | the right actor |
| $(F)^{\approx}$ | the associate, the adjoint of the plain form; it exchanges the sides |
| $(F)^{\natural}$ | the adjoint of the quaternionic form; it keeps the side |
| $(F)^{\ast}$ | the adjoint of the plain sesquilinear form |
| $\natural$, $\ast$, $\bar{\cdot}$ | the natural conjugation, the Hermitian conjugation, the coefficient conjugation |
| $\langle\tilde Q\rangle_{\natural}$ | the quaternionic norm, $\sum_\mu Q_\mu^{2}$, central |
| $\mathbb{B}_{\Psi}$, $\mathbb{B}_{\Phi}$ | the Hermitian and anti-Hermitian halves |
| $\mathrm{Sd}_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{\ast}}$ | the two-side member, the subject of the companion article |
| $\mathbb{D}_{\tilde Q}$ | the off-diagonal two-component operator with blocks $L_{\tilde Q}$ and $L_{\tilde Q^{\natural}}$, of square $\langle\tilde Q\rangle_{\natural}\mathrm{id}$ |

## Further Reading

- [Operators Acting 1 Side](operators-acting-1-side.html), for the two regular families, their laws, their injectivity, their commutants and the line on which they meet.
- [Hermitian pair of operators acting as 2 side](hermitian-pair-of-operators-acting-as-2-side.html), for the other placement: the operator $L_{\tilde Q}R_{\tilde Q^{\ast}}$, its multiplicativity, its real cone, the rigidity theorem and the one-sided contrast quoted above.
- [The Transposition of the Two Sides](the-transposition-of-the-two-sides.html), for $R_{\tilde Q}=\tau^{-1}L_{\tau(\tilde Q)}\tau$, for the reversals and their two linearity grades, and for the two errors that the transport of the parameter prevents.
- [Adjoint Pair of $L$ and $R$ Operators](adjoint-pair-of-l-and-r-operators.html), for the four adjoints, their association with the four forms, and the table from which the three adjoint identities above are read.
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the forms, their Gram matrices and their signatures.
- [Operator Chirality on the Biquaternion Algebra](operator-chirality-on-the-biquaternion-algebra.html), for the exchange of the two sides by a reversal, $\natural L_{\tilde Q}\natural=R_{\tilde Q^{\natural}}$, and for the labels the two actors carry.
- [The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure](the-enveloping-operator-algebra-of-the-biquaternion-algebra-and-the-bi-module-structure.html), for the generation of every operator by the left family together with one reversal.
- [The Dirac Equation in Biquaternionic Form](../articles_physics/the-dirac-equation-in-biquaternionic-form.html), for the instance of the two-component reading in which the parameter is the gradient, the scalar is the d'Alembertian, and the squared display is the Klein–Gordon equation.
- [Operator Family Conventions](operator-family-conventions.html), for the letters, the slots and the names of the sets.
