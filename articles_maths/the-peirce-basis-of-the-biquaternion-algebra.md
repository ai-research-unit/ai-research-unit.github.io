# __The Peirce Basis of the Biquaternion Algebra__

## Introduction

A complete orthogonal family of two idempotents $\tilde\Pi_{+},\tilde\Pi_{-}$ cuts the biquaternion algebra into four complex lines $\mathbb{B}_{st}=\tilde\Pi_{s}\mathbb{B}\tilde\Pi_{t}$. The diagonal lines are spanned by the idempotents, and those vectors are canonical. The mixed lines have no canonical nonzero element.

A **Peirce basis** is a choice of one nonzero element in each mixed line, normalized so that the two elements multiply to the two idempotents. The diagonal elements are then forced. The choice of one mixed element determines the other: for every nonzero $u\in\mathbb{B}_{+-}$ there is a unique $v\in\mathbb{B}_{-+}$ with $uv=\tilde\Pi_{+}$, and then $vu=\tilde\Pi_{-}$. The remaining freedom is a nonzero complex scale, the **gauge**. A basis is therefore a family together with a point of the gauge torsor.

The article defines the basis, proves existence by the nilpotent route, computes the gauge, the coordinates, the product and the determinant, states the torsor and its stabilizer, gives the matrix-unit reading, counts the real dimensions, treats the Hermitian gauge, and gives the standard family as an example.

## Definition

Let $\tilde\Pi_{+},\tilde\Pi_{-}$ be a nondegenerate complete family, with corners $\mathbb{B}_{st}=\tilde\Pi_{s}\mathbb{B}\tilde\Pi_{t}$.

**Definition.** A **Peirce basis** of the family is a pair of nonzero elements

$$
\vec\Upsilon_{+-}\in\mathbb{B}_{+-},\qquad
\vec\Upsilon_{-+}\in\mathbb{B}_{-+}
$$

with

$$
\vec\Upsilon_{+-}\vec\Upsilon_{-+}=\tilde\Pi_{+},\qquad
\vec\Upsilon_{-+}\vec\Upsilon_{+-}=\tilde\Pi_{-}.
$$

The four elements of the basis are $\tilde\Pi_{+},\vec\Upsilon_{+-},\vec\Upsilon_{-+},\tilde\Pi_{-}$. The corner rule gives

$$
\tilde\Pi_{+}\vec\Upsilon_{+-}=\vec\Upsilon_{+-}=\vec\Upsilon_{+-}\tilde\Pi_{-},\qquad
\tilde\Pi_{-}\vec\Upsilon_{-+}=\vec\Upsilon_{-+}=\vec\Upsilon_{-+}\tilde\Pi_{+},
$$

and the products in the other directions vanish. In particular,

$$
\vec\Upsilon_{+-}^{2}=\vec\Upsilon_{-+}^{2}=0,
$$

so both mixed elements are nilpotents. The four elements satisfy the multiplication table of the four $2\times2$ matrix units, with $\tilde\Pi_{\pm}$ on the diagonal.

**The diagonal is forced.** If a nonzero diagonal element is written $c\tilde\Pi_{s}$, then idempotence gives $c^{2}=c$, hence $c=1$. The diagonal elements of a Peirce basis are therefore the idempotents themselves; they are not a choice.

**The mixed elements are a choice.** A nonzero $\vec\Upsilon_{+-}$ can be rescaled, and the product normalization forces the reciprocal rescaling of $\vec\Upsilon_{-+}$. That freedom is the gauge of §*The Gauge*.

## Existence: The Nilpotent Route

**Theorem.** Every nondegenerate complete family of two idempotents of $\mathbb{B}$ admits a Peirce basis. More precisely, for every nonzero $u\in\mathbb{B}_{+-}$ there is a unique $v\in\mathbb{B}_{-+}$ with $uv=\tilde\Pi_{+}$, and then $vu=\tilde\Pi_{-}$. The Peirce bases of the family are in bijection with the nonzero elements of $\mathbb{B}_{+-}$, and also with the nonzero elements of $\mathbb{B}_{-+}$.

**Proof.** Let $u\in\mathbb{B}_{+-}$ be nonzero. By the corner rule, left multiplication by $u$ maps $\mathbb{B}_{-+}$ into $\mathbb{B}_{++}$ and annihilates $\mathbb{B}_{++}$. The product $\mathbb{B}_{+-}\mathbb{B}_{-+}$ is nonzero by the lemma of *The Peirce Decomposition of the Biquaternion Algebra*, §*The Peirce Decompositions*; since $\mathbb{B}_{-+}$ is a line, $u\mathbb{B}_{-+}\ne0$. A nonzero linear map between two lines is an isomorphism, so there is a unique $v\in\mathbb{B}_{-+}$ with $uv=\tilde\Pi_{+}$.

Now $vu\in\mathbb{B}_{--}=\mathbb{C}\tilde\Pi_{-}$. It is nonzero: if $vu=0$, then $u(vu)=0$, but $(uv)u=\tilde\Pi_{+}u=u\ne0$. Write $vu=\lambda\tilde\Pi_{-}$ with $\lambda\ne0$. Then

$$
u=uvu=\lambda u,
$$

so $\lambda=1$ and $vu=\tilde\Pi_{-}$. Thus $(u,v)$ is a basis.

Conversely, a basis gives its first element $u=\vec\Upsilon_{+-}$, and the partner is unique by the argument above. The map from bases to nonzero elements of $\mathbb{B}_{+-}$ is therefore bijective. The same argument with the signs exchanged gives the bijection with the nonzero elements of $\mathbb{B}_{-+}$.

**The idempotents are products of the two nilpotents.** The theorem gives

$$
\tilde\Pi_{+}=\vec\Upsilon_{+-}\vec\Upsilon_{-+},\qquad
\tilde\Pi_{-}=\vec\Upsilon_{-+}\vec\Upsilon_{+-}.
$$

The mixed elements are nilpotents, and each idempotent is the product of the two in the appropriate order.

**The gauge is the reciprocal scaling.** If $u$ is replaced by $\lambda u$, then $v$ is replaced by $\lambda^{-1}v$, and the pair remains a basis. Every $\lambda\in\mathbb{C}^{\times}$ gives a basis. This one-parameter scaling is the whole freedom of the construction; it is computed in §*The Gauge*.

## Coordinates

Every element has a unique expansion

$$
\tilde Q=Q_{++}\tilde\Pi_{+}+Q_{+-}\vec\Upsilon_{+-}+Q_{-+}\vec\Upsilon_{-+}+Q_{--}\tilde\Pi_{-},
$$

with $Q_{st}\in\mathbb{C}$. The numbers $Q_{st}$ are the **Peirce coordinates** of $\tilde Q$ in the basis.

**The product.** If $\tilde Q'$ has coordinates $Q'_{st}$, then

$$
Q''_{++}=Q_{++}Q'_{++}+Q_{+-}Q'_{-+},\qquad
Q''_{+-}=Q_{++}Q'_{+-}+Q_{+-}Q'_{--},
$$

$$
Q''_{-+}=Q_{-+}Q'_{++}+Q_{--}Q'_{-+},\qquad
Q''_{--}=Q_{-+}Q'_{+-}+Q_{--}Q'_{--}.
$$

The coordinates multiply as $2\times2$ matrices. This is the product rule of the four lines written in the basis.

**The determinant.** The four basis elements satisfy the multiplication table of the matrix units, so the coordinate map

$$
\tilde\Pi_{+}\mapsto E_{11},\quad
\vec\Upsilon_{+-}\mapsto E_{12},\quad
\vec\Upsilon_{-+}\mapsto E_{21},\quad
\tilde\Pi_{-}\mapsto E_{22}
$$

is an algebra isomorphism from $\mathbb{B}$ onto $M_{2}(\mathbb{C})$. The determinant of the coordinate matrix is therefore the determinant of the element in the matrix model, that is the quaternionic norm:

$$
Q_{++}Q_{--}-Q_{+-}Q_{-+}=\langle\tilde Q\rangle_{\natural}
=Q_{t}^{2}+Q_{x}^{2}+Q_{y}^{2}+Q_{z}^{2}.
$$

The identity is independent of the basis: a change of basis conjugates the coordinate matrix and leaves its determinant unchanged.

## The Gauge

**A change of basis of the same family.** Every other basis of the same family has the form

$$
\vec\Upsilon'_{+-}=t_{+}t_{-}^{-1}\vec\Upsilon_{+-},\qquad
\vec\Upsilon'_{-+}=t_{-}t_{+}^{-1}\vec\Upsilon_{-+},\qquad
t_{+},t_{-}\in\mathbb{C}^{\times},
$$

with the diagonal elements unchanged.

**Proof.** Each primed mixed element is a nonzero multiple of the unprimed one, say $\vec\Upsilon'_{+-}=c_{+}\vec\Upsilon_{+-}$ and $\vec\Upsilon'_{-+}=c_{-}\vec\Upsilon_{-+}$. The product normalization gives $c_{+}c_{-}=1$. Set $t_{+}=c_{+}$ and $t_{-}=1$; then $c_{+}=t_{+}t_{-}^{-1}$ and $c_{-}=t_{-}t_{+}^{-1}$. The converse is a direct check.

**The effective gauge.** Put $t=t_{-}t_{+}^{-1}$. Then

$$
\vec\Upsilon'_{+-}=t^{-1}\vec\Upsilon_{+-},\qquad
\vec\Upsilon'_{-+}=t\,\vec\Upsilon_{-+}.
$$

A common scalar in $t_{+}$ and $t_{-}$ acts trivially, because $(ct_{+})(ct_{-})^{-1}=t_{+}t_{-}^{-1}$. The effective group is

$$
G=(\mathbb{C}^{\times})^{2}/\mathbb{C}^{\times}\cong\mathbb{C}^{\times},
$$

of real dimension two. The parameter $t$ is the single complex gauge parameter of the biquaternion case.

**The bases form a torsor.** Fix the family. The set $\mathcal{B}(F)$ of its Peirce bases is a $G$-torsor: the action is free and transitive.

- *Free:* if a gauge element fixes both mixed elements, then $t_{+}t_{-}^{-1}=1$ and $t_{-}t_{+}^{-1}=1$, so $t_{+}=t_{-}$; the class in $G$ is the identity.
- *Transitive:* given two bases, their first mixed elements are nonzero multiples, $u'=cu$; set $t_{+}=c$, $t_{-}=1$, and the product normalization forces the second mixed element to be $c^{-1}v$, which is the transformed basis.

Equivalently, the map $u\mapsto$ the basis with first element $u$ is a bijection

$$
\mathcal{B}(F)\cong\mathbb{B}_{+-}\setminus\{0\},
$$

and $G$ acts on the right-hand side by $u\mapsto t^{-1}u$. No basis is distinguished.

**The stabilizer.** In $G$, the action is free, so the stabilizer of a basis is trivial. In the unit group, the units that fix the family are

$$
U=a\tilde\Pi_{+}+b\tilde\Pi_{-},\qquad a,b\in\mathbb{C}^{\times}.
$$

Conjugation by $U$ gives

$$
U\vec\Upsilon_{+-}U^{-1}=\frac{a}{b}\vec\Upsilon_{+-},\qquad
U\vec\Upsilon_{-+}U^{-1}=\frac{b}{a}\vec\Upsilon_{-+}.
$$

The map $U\mapsto(a,b)$ is an isomorphism from the stabilizer of the family in $\mathbb{B}^{\times}$ onto $\mathbb{C}^{\times}\times\mathbb{C}^{\times}$. The centre of $\mathbb{B}$ is $\mathbb{C}e_{t}$, and the centre of the unit group is the diagonal $a=b$. The quotient is $G$. A unit fixes a basis exactly when $a=b$, that is exactly when it is central. Two bases of the same family are conjugate by a unit, unique up to the centre.

**Coordinates under the gauge.** With $t=t_{-}t_{+}^{-1}$,

$$
Q'_{++}=Q_{++},\qquad
Q'_{+-}=tQ_{+-},\qquad
Q'_{-+}=t^{-1}Q_{-+},\qquad
Q'_{--}=Q_{--}.
$$

The product and the determinant are unchanged: the same element is read in another basis.

**Gauge fixing.** A gauge fixing is a point of the torsor, that is a nonzero element of one mixed line. The nonvanishing and the product normalization are part of the definition of a basis and do not fix the scale. The Hermitian condition restricts the gauge but does not fix it; see below.

**The Hermitian gauge.** Suppose the family is Hermitian, $\tilde\Pi_{\pm}^{*}=\tilde\Pi_{\pm}$, with the positive definite Hermitian form of the algebra. Then:

- A Hermitian basis exists. Choose a nonzero $u\in\mathbb{B}_{+-}$. Then $u^{*}\in\mathbb{B}_{-+}$ and $uu^{*}\in\mathbb{B}_{++}=\mathbb{C}\tilde\Pi_{+}$. The element $uu^{*}$ is Hermitian and nonzero, and $\mathrm{Sc}(uu^{*})>0$ by positive definiteness; write $uu^{*}=\lambda\tilde\Pi_{+}$ with $\lambda>0$, since $\mathrm{Sc}(\tilde\Pi_{+})=\frac12$. Replace $u$ by $\lambda^{-1/2}u$; then $uu^{*}=\tilde\Pi_{+}$. Now $u^{*}u\in\mathbb{B}_{--}=\mathbb{C}\tilde\Pi_{-}$ is nonzero, because $u(u^{*}u)=0$ would give $(uu^{*})u=u=0$; write $u^{*}u=\mu\tilde\Pi_{-}$. Then $u=uu^{*}u=\mu u$, so $\mu=1$. Thus $\vec\Upsilon_{+-}=u$ and $\vec\Upsilon_{-+}=u^{*}$ are a Hermitian basis.
- The Hermitian bases are the bases with $\vec\Upsilon_{-+}=\vec\Upsilon_{+-}^{*}$. Under the gauge, this condition reads $t\vec\Upsilon_{-+}=\bar t^{-1}\vec\Upsilon_{-+}$, so $t\bar t=1$. The Hermitian bases are therefore a $U(1)$-torsor, of real dimension one.
- The Hermitian condition does not fix a basis; a circle of bases remains. A gauge fixing in the Hermitian case is a point of that circle.

## Systems of Matrix Units

**Definition.** A **system of $2\times2$ matrix units** in $\mathbb{B}$ is a family

$$
\tilde\Pi_{+},\quad\vec\Upsilon_{+-},\quad\vec\Upsilon_{-+},\quad\tilde\Pi_{-}
$$

with the multiplication table

$$
\tilde\Pi_{+}^{2}=\tilde\Pi_{+},\quad
\tilde\Pi_{-}^{2}=\tilde\Pi_{-},\quad
\tilde\Pi_{+}\tilde\Pi_{-}=\tilde\Pi_{-}\tilde\Pi_{+}=0,
$$

$$
\vec\Upsilon_{+-}\vec\Upsilon_{-+}=\tilde\Pi_{+},\quad
\vec\Upsilon_{-+}\vec\Upsilon_{+-}=\tilde\Pi_{-},\quad
\vec\Upsilon_{+-}^{2}=\vec\Upsilon_{-+}^{2}=0.
$$

A Peirce basis is exactly such a system. The coordinate map of §*Coordinates* sends it to the four elementary matrices, so a system of matrix units is the same data as an algebra isomorphism $\mathbb{B}\to M_{2}(\mathbb{C})$ in which the family is the standard diagonal pair.

**Uniqueness up to conjugation.** Every two systems of $2\times2$ matrix units of $\mathbb{B}$ are conjugate by a unit, and the conjugating unit is unique up to the centre.

**Proof.** For two systems of the same family, the two bases differ by the gauge of §*The Gauge*, and that gauge is conjugation by $U=t_{+}\tilde\Pi_{+}+t_{-}\tilde\Pi_{-}$; the conjugating unit is unique up to a common scalar, that is up to the centre. For two systems of different families, pass to the matrix model. A nontrivial idempotent of $M_{2}(\mathbb{C})$ is a rank-one projection; choose a basis of $\mathbb{C}^{2}$ in which its image is the first coordinate line and its kernel the second. The projection is then $E_{11}$, and the mixed units are determined up to the diagonal torus. Every automorphism of $M_{2}(\mathbb{C})$ is inner, so the conjugation descends to $\mathbb{B}$. The centralizer of a full system of matrix units is the centre. Each system is therefore conjugate to the standard one, and any two systems are conjugate to each other; the unit is unique up to the centre.

## Dimensions

**The family.** A nondegenerate family is the same data as a nontrivial idempotent, by *The Peirce Decomposition of the Biquaternion Algebra*, §*From One Idempotent to Its Complement*. In the matrix model a nontrivial idempotent is a rank-one projection: its image is a line, of one complex parameter, and its kernel is a complementary line, of one complex parameter. The family therefore has complex dimension two, that is real dimension four.

**The basis.** Fix the family. A basis is a nonzero element of one mixed line, by §*Existence: The Nilpotent Route*. A complex line with its zero removed has complex dimension one, that is real dimension two. The basis is the family together with this point, so the basis space has real dimension $4+2=6$.

**The gauge.** The effective gauge is $\mathbb{C}^{\times}$, of real dimension two. It is the fibre of the map from bases to families. The count is

$$
\underbrace{4}_{\text{family}}+\underbrace{2}_{\text{mixed element}}=\underbrace{6}_{\text{basis}},
\qquad
\underbrace{6}_{\text{basis}}-\underbrace{2}_{\text{gauge}}=\underbrace{4}_{\text{family}}.
$$

The family is the input and the mixed element is the choice.

## Example: The Standard Family and Basis

The standard family is

$$
\tilde\Pi_{+}=\frac{e_{t}+i\vec e_{z}}{2},\qquad
\tilde\Pi_{-}=\frac{e_{t}-i\vec e_{z}}{2},
$$

and the standard mixed units are

$$
\vec\Upsilon_{+-}=\frac{i\vec e_{x}-\vec e_{y}}{2},\qquad
\vec\Upsilon_{-+}=\frac{i\vec e_{x}+\vec e_{y}}{2}.
$$

They satisfy

$$
\vec\Upsilon_{+-}\vec\Upsilon_{-+}=\tilde\Pi_{+},\qquad
\vec\Upsilon_{-+}\vec\Upsilon_{+-}=\tilde\Pi_{-},\qquad
\vec\Upsilon_{+-}^{2}=\vec\Upsilon_{-+}^{2}=0.
$$

The gauge transformation is

$$
\vec\Upsilon'_{+-}=t^{-1}\vec\Upsilon_{+-},\qquad
\vec\Upsilon'_{-+}=t\vec\Upsilon_{-+},
$$

for $t\in\mathbb{C}^{\times}$. The standard basis is Hermitian, $\vec\Upsilon_{-+}=\vec\Upsilon_{+-}^{*}$; the Hermitian gauges are the circle $|t|=1$, so the standard basis is one point of a $U(1)$-family and not a canonical one.

The coordinate matrix of an element is

$$
\begin{pmatrix}
Q_{++} & Q_{+-}\\
Q_{-+} & Q_{--}
\end{pmatrix},
$$

with determinant $Q_{++}Q_{--}-Q_{+-}Q_{-+}=\langle\tilde Q\rangle_{\natural}$.

## Summary

A Peirce basis of a nondegenerate complete family $\tilde\Pi_{+},\tilde\Pi_{-}$ is a pair of nonzero mixed elements $\vec\Upsilon_{+-}\in\mathbb{B}_{+-}$ and $\vec\Upsilon_{-+}\in\mathbb{B}_{-+}$ with $\vec\Upsilon_{+-}\vec\Upsilon_{-+}=\tilde\Pi_{+}$ and $\vec\Upsilon_{-+}\vec\Upsilon_{+-}=\tilde\Pi_{-}$. The diagonal elements are the idempotents and are forced. Existence is the nilpotent route: every nonzero element of one mixed line has a unique partner in the other, and the two idempotents are the two products. The bases are a $\mathbb{C}^{\times}$-torsor, equivalently the nonzero elements of one mixed line; the gauge is the reciprocal scaling, free and transitive. In the unit group the stabilizer of a basis is the centre. The Hermitian condition restricts the gauge to $U(1)$ and does not fix it. The coordinate matrix is a $2\times2$ matrix model, and its determinant is the quaternionic norm. The dimensions are $6=4+2$ real.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\Pi_{\pm}$ | The two idempotents of the family |
| $\mathbb{B}_{st}=\tilde\Pi_{s}\mathbb{B}\tilde\Pi_{t}$ | A Peirce line |
| $\vec\Upsilon_{+-},\vec\Upsilon_{-+}$ | The mixed units of a basis |
| $Q_{st}$ | The Peirce coordinates |
| $\mathcal{B}(F)$ | The set of bases of the family $F$ |
| $G=(\mathbb{C}^{\times})^{2}/\mathbb{C}^{\times}$ | The effective gauge group |
| $t_{+},t_{-},t$ | The gauge parameters, with $t=t_{-}t_{+}^{-1}$ |
| $\langle\tilde Q\rangle_{\natural}$ | The quaternionic norm |

## Further Reading

- [The Peirce Decomposition of the Biquaternion Algebra](the-peirce-decomposition-of-the-biquaternion-algebra.html), for the family, the four lines and the product rule.
- [Spinors as Peirce Coordinates in the Biquaternion Algebra](spinors-as-peirce-coordinates-in-the-biquaternion-algebra.html), for the coordinates of the two spinor spaces.
- [$M_2(\mathbb{C})$ Model : Peirce Coordinates, Matrix Units and the Spinor Planes](m2c-model-the-peirce-coordinates-matrix-units-and-the-spinor-planes.html), for the matrix model and the coordinate isomorphism.
- [The Peirce Decomposition in $n$ Dimensions](the-peirce-decomposition-in-n-dimensions.html), for the general gauge $(\mathbb{C}^{\times})^{n}/\mathbb{C}^{\times}$.
- [Biquaternion Automorphisms and Derivations](biquaternion-automorphisms-and-derivations.html), for the inner automorphisms used in §*Systems of Matrix Units*.
- [Idempotents](idempotents.html), for the classification of the idempotents and the standard pair.
