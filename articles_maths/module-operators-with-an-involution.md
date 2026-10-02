
# __Module Operators with an Involution__

## Introduction

When a module carries a non-degenerate pairing, its endomorphism ring carries an involution, and the individual endomorphisms fall into classes according to how they meet it: those fixed by the involution, those negated by it, and the units it preserves. This article develops the calculus of a single operator with respect to the involution — the decomposition into a self-adjoint and a skew-adjoint part, the behaviour of products, the congruences $f \mapsto g^{*}fg$, and the action of the unitary group.

The article is the second of the `* Operator Theory` group of this category. The involution itself, its construction from a pairing and the property of being an involution are the subject of *The Involution on the Endomorphism Ring of a Module*; this article assumes that structure, writes the involutive algebra of operators as $(E,{}^{*})$, and studies its elements. The classification of the involutions a ring can carry is *Involutions of the Module Endomorphism Ring*; the adjoints of the specific operators of the preceding articles are *The Adjoint of the Sandwich on a Bimodule over an Algebra* and its signed variant. The article stays inside Part I: no distance, norm, positivity, topology or limit occurs, and a self-adjoint operator is one fixed by the involution, not one bounded or closed. Throughout, $R$ is a commutative ring with $1 \neq 0$ in which $2$ is invertible, $(A,\sigma)$ is an involutive $R$-algebra, $M$ is a left $A$-module with a non-degenerate reflexive $\sigma$-sesquilinear pairing, and $(E,{}^{*})$ is the involutive $R$-algebra $\operatorname{End}_A(M)$ with the adjoint involution of *The Involution on the Endomorphism Ring of a Module*.

## Operators on a Module with an Involution

### The structure assumed

**Proposition.** The pair $(E,{}^{*})$ is an involutive $R$-algebra: ${}^{*}$ is an additive, $R$-linear, anti-multiplicative map of order two, and $E$ is a unital associative $R$-algebra. The map ${}^{*}$ restricts to the involution $\sigma$ of $A$ on the image of the action, in the sense $(L_a)^{*}=L_{\sigma(a)}$.

*Proof.* This is *The Involution on the Endomorphism Ring of a Module*; the last clause is the formula for the adjoint of a left multiplication. $\square$

An operator $f \in E$ is therefore an element of an involutive algebra, and the definitions of the symmetric, the antisymmetric and the unitary elements of such an algebra apply to it. The concrete origin of the involution — the pairing — enters whenever one asks what an operator does to the pairing, and the isometry characterisation below is the bridge.

### Elementary classes

**Definition.** An operator $f \in E$ is **self-adjoint** when $f^{*}=f$, **skew-adjoint** when $f^{*}=-f$, and **unitary** when $f^{*}f=ff^{*}=\mathrm{id}$. Write

$$
\operatorname{Sym}(M)=\{f : f^{*}=f\}, \qquad \operatorname{Skew}(M)=\{f : f^{*}=-f\}, \qquad U(M)=\{f : f^{*}f=ff^{*}=\mathrm{id}\}.
$$

**Proposition.** $\operatorname{Sym}(M)$ and $\operatorname{Skew}(M)$ are $R$-submodules with $\operatorname{Sym}(M)\cap\operatorname{Skew}(M)=0$ and $E=\operatorname{Sym}(M)\oplus\operatorname{Skew}(M)$; the map $f \mapsto \frac12(f+f^{*})$ is the projection onto the first summand. $U(M)$ is a subgroup of $E^{\times}$.

*Proof.* The decomposition, the projection formula and the group property are *The Involution on the Endomorphism Ring of a Module*. $\square$

## Self-Adjoint Operators

### The real and the imaginary part

**Definition.** For $f \in E$ the **self-adjoint part** and the **skew part** are

$$
\operatorname{Re}f=\tfrac12(f+f^{*}), \qquad \operatorname{Im}f=\tfrac12(f-f^{*}),
$$

so that $f=\operatorname{Re}f+\operatorname{Im}f$ and $(\operatorname{Re}f)^{*}=\operatorname{Re}f$, $(\operatorname{Im}f)^{*}=-\operatorname{Im}f$.

**Proposition.** The assignment $f \mapsto (\operatorname{Re}f,\operatorname{Im}f)$ is an $R$-linear isomorphism $E \to \operatorname{Sym}(M)\oplus\operatorname{Skew}(M)$, natural in $f$, and $\operatorname{Re}f=f$ exactly for self-adjoint $f$ while $\operatorname{Im}f=f$ exactly for skew-adjoint $f$.

*Proof.* The map is $R$-linear because ${}^{*}$ is, it is injective because its composite with the sum is the identity, and its image is contained in the direct sum; dimensions (or the projection formula) give the isomorphism. The last clauses are the definitions. $\square$

This is the operator-level form of the decomposition of an involutive algebra into its symmetric and antisymmetric parts; no order structure is attached to $\operatorname{Sym}(M)$, because positivity needs a norm and belongs to Part II.

### Products of self-adjoint operators

**Theorem.** Let $f$ and $g$ be self-adjoint. Then $fg$ is self-adjoint if and only if $f$ and $g$ commute; $fg+gf$ and $fgf$ are self-adjoint always; and $f^{2}$ is self-adjoint.

*Proof.* $(fg)^{*}=g^{*}f^{*}=gf$, so $fg$ is self-adjoint exactly when $gf=fg$. For the sum, $(fg+gf)^{*}=gf+fg=fg+gf$; for the product $fgf$, $(fgf)^{*}=f^{*}g^{*}f^{*}=fgf$; and $f^{2}$ is the case $g=f$. $\square$

So the self-adjoint operators are closed under the Jordan product $\frac12(fg+gf)$ and under the square, as *The Involution on the Endomorphism Ring of a Module* records, but not under the ordinary product unless the factors commute.

### Operators of the form $f^{*}f$

**Proposition.** For every $f \in E$ the operators $f^{*}f$ and $ff^{*}$ are self-adjoint, and $f$ is unitary if and only if $f^{*}f=ff^{*}=\mathrm{id}$; consequently $u^{*}fu$ is self-adjoint when $f$ is self-adjoint and $u$ is unitary.

*Proof.* $(f^{*}f)^{*}=f^{*}f$ and $(ff^{*})^{*}=ff^{*}$, by $(f^{*})^{*}=f$ and anti-multiplicativity; if $u\in U(M)$ then $(u^{*}fu)^{*}=u^{*}f^{*}u=u^{*}fu$. $\square$

The operators $f^{*}f$ and $ff^{*}$ are the two self-adjoint squares of $f$; in Part II they receive a norm and an order, and the polar decomposition is built from them, but over a general ring they are only self-adjoint elements.

### Congruences

**Definition.** A **congruence** by $g \in E$ is the map

$$
\operatorname{cong}_g : E \to E, \qquad \operatorname{cong}_g(f)=g^{*}fg .
$$

**Proposition.** For every $g$ the congruence preserves self-adjointness: if $f^{*}=f$ then $(g^{*}fg)^{*}=g^{*}fg$. If $g$ is unitary, the congruence is the inner automorphism $f \mapsto g^{-1}fg$ and is an algebra automorphism; for general $g$ it is additive and $R$-linear, it satisfies $\operatorname{cong}_g\circ\operatorname{cong}_h=\operatorname{cong}_{hg}$, and it is invertible exactly when $g$ is a unit.

*Proof.* $(g^{*}fg)^{*}=g^{*}f^{*}(g^{*})^{*}=g^{*}fg$. For unitary $g$, $g^{*}=g^{-1}$ and $g^{*}fg=g^{-1}fg$, which is conjugation and preserves products; for general $g$, $\operatorname{cong}_g(fh)=g^{*}fhg$ while $\operatorname{cong}_g(f)\operatorname{cong}_g(h)=g^{*}fgg^{*}hg$, equal only when $gg^{*}$ is central. The composition is $\operatorname{cong}_g(\operatorname{cong}_h(f))=g^{*}h^{*}fhg=(hg)^{*}f(hg)=\operatorname{cong}_{hg}(f)$; when $g$ is a unit, $\operatorname{cong}_{g^{-1}}$ is a two-sided inverse. $\square$

Congruences are the general "change of pairing" operation on operators: replacing the pairing by an equivalent one conjugates the involution, and composing the new involution with the old gives a congruence, as the last section shows.

## Unitary Operators

### Isometries and the unitary group

**Theorem.** An operator $u$ is unitary if and only if it preserves the pairing, $\langle u(m),u(n)\rangle=\langle m,n\rangle$ for all $m,n$. The unitary operators form a subgroup $U(M)$ of $E^{\times}$, the isometry group of the pairing, and for $u \in U(M)$ and $f \in E$,

$$
(ufu^{*})^{*}=u f^{*}u^{*}, \qquad (ufu^{-1})^{*}=u f^{*}u^{-1}.
$$

*Proof.* The isometry characterisation and the group property are *The Involution on the Endomorphism Ring of a Module*; the two identities use $u^{*}=u^{-1}$ and anti-multiplicativity. $\square$

The action $f \mapsto ufu^{-1}$ of $U(M)$ on $E$ is **unitary conjugation**, an inner action by the unitary group; it preserves products, self-adjointness and skew-adjointness, and it is the operator-level counterpart of the action of the unitary group of an involutive algebra on its symmetric elements.

### Unitary equivalence of operators

**Definition.** Two operators $f$ and $h$ are **unitarily equivalent** when $h=ufu^{*}$ for some $u \in U(M)$; they are **congruent** when $h=g^{*}fg$ for some $g\in E^{\times}$.

**Proposition.** Unitary equivalence is an equivalence relation on $E$ and preserves the classes of self-adjoint, skew-adjoint and unitary operators. Congruence by an invertible $g$ preserves self-adjointness and is transitive; it coincides with unitary equivalence exactly when $g$ is unitary.

*Proof.* The group $U(M)$ acts, so unitary equivalence is an equivalence relation, and the class preservation is the displayed identities. Congruence preserves self-adjointness by the proposition above and composes as $\operatorname{cong}_g\circ\operatorname{cong}_h=\operatorname{cong}_{gh}$ up to a congruence; it is unitary equivalence when $g^{*}=g^{-1}$. $\square$

The two relations differ in the same way the symmetric bilinear and the hermitian classifications differ: unitary equivalence preserves the pairing, congruence does not.

### The unitary orbit

**Definition.** For $f \in E$ the **unitary orbit** of $f$ is

$$
U(M)\cdot f=\{ufu^{*} : u \in U(M)\}.
$$

**Proposition.** The unitary orbit of a self-adjoint operator consists of self-adjoint operators, and the unitary group acts on the set of self-adjoint operators with orbits the unitary orbits. The stabiliser of $f$ is the subgroup $\{u : uf=fu\}$.

*Proof.* If $f^{*}=f$ then $(ufu^{*})^{*}=ufu^{*}$, so the orbit is inside the self-adjoint part; the stabiliser computation is immediate from the action's definition. $\square$

The classification of the orbits of self-adjoint operators requires invariants (in the classical theory the eigenvalues, or the spectrum), which need a field, a norm and the spectral theorem; they belong to Part II, and only the orbit–stabiliser statement is available here.

## Operator Identities

### The involution and a single operator

**Proposition.** For every $f \in E$,

$$
f+f^{*} \in \operatorname{Sym}(M), \qquad f-f^{*} \in \operatorname{Skew}(M), \qquad f f^{*} \in \operatorname{Sym}(M), \qquad f^{*} f \in \operatorname{Sym}(M) .
$$

Moreover $f$ is self-adjoint if and only if $f=f^{*}$, and $f$ is skew-adjoint if and only if $f=-f^{*}$.

*Proof.* $(f+f^{*})^{*}=f^{*}+f$; $(f-f^{*})^{*}=f^{*}-f=-(f-f^{*})$; the products are the self-adjoint squares. $\square$

### The $*$-congruence and equivalence

**Proposition.** The map $f \mapsto g^{*}fg$ is additive and $R$-linear; if $g$ is a unit then the map is invertible with inverse $h \mapsto (g^{*})^{-1}h\,g^{-1}$, and it carries the involutive algebra structure $(E,{}^{*})$ to the involutive algebra structure with involution $f \mapsto g^{-1}f^{*}g$.

*Proof.* Additivity and $R$-linearity are clear. For invertibility, $g^{*}f g=h$ with $g$ a unit is solved by $f=(g^{*})^{-1}hg^{-1}$; and $(g^{*}fg)^{*}=g^{*}f^{*}g$, so the transformed involution is $f\mapsto g^{-1}f^{*}g$ on the transformed element. $\square$

This is how a module with two pairings carries two involutions on one ring, as *The Involution on the Endomorphism Ring of a Module* notes.

## Examples

**(a) The orthogonal case.** For $M=R^n$ with the standard bilinear pairing, the self-adjoint operators are the symmetric matrices, the skew-adjoint the alternating matrices, and $U(M)=O(n)$; unitarily equivalent self-adjoint operators are orthogonally similar.

**(b) The unitary case.** For $M=\mathbb{C}^n$ with the sesquilinear pairing, the self-adjoint operators are the hermitian matrices, the skew-adjoint the skew-hermitian ones, and $U(M)=U(n)$.

**(c) The symplectic case.** For $M=R^{2n}$ with the alternating pairing, the self-adjoint operators form the symplectic Lie algebra and $U(M)=Sp(2n)$; the congruence $f \mapsto g^{*}fg$ is the symplectic change of basis.

**(d) The regular module of a division ring.** For $M=A=D$ with the regular pairing $\langle a,b\rangle=\sigma(a)b$, the self-adjoint operators under $\operatorname{End}_D(D)\cong D^{\mathrm{op}}$ are the symmetric elements of $D$, the skew-adjoint the antisymmetric elements, and $U(M)$ the unitary group of $D$.

**(e) A congruence that is not unitary.** For $M=R^2$ with the standard pairing and $g=\operatorname{diag}(2,1)$, the congruence $f \mapsto g^{*}fg=g f g$ preserves self-adjointness but is not conjugation by a unitary element; it changes the operator's "shape" while keeping it symmetric.

## Summary

On a module with a non-degenerate reflexive pairing, the endomorphism ring is an involutive $R$-algebra $(E,{}^{*})$, and its elements are classified by the involution: self-adjoint, skew-adjoint, and unitary. Every operator decomposes uniquely as $f=\operatorname{Re}f+\operatorname{Im}f$ with the two parts self-adjoint and skew-adjoint; the self-adjoint part is closed under the Jordan product and the square but under the ordinary product only when the factors commute; the products $f^{*}f$ and $ff^{*}$ are always self-adjoint, and a congruence $f \mapsto g^{*}fg$ preserves self-adjointness while being multiplicative only for unitary $g$. The unitary operators are the isometries of the pairing and form a subgroup $U(M)$ of the unit group, acting by unitary conjugation $f \mapsto ufu^{-1}$ and preserving the involutive algebra structure; the unitary orbit and the congruence orbit are the two natural equivalence relations on the self-adjoint operators, and their classification needs the spectrum, which belongs to Part II. Nothing here uses a norm, a positivity or a topology; the classes are defined by the involution alone, and the operator identities are the ones available over a general coefficient ring.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(A,\sigma)$ | involutive $R$-algebra |
| $M$, $\langle\cdot,\cdot\rangle$ | module with non-degenerate reflexive σ-sesquilinear pairing |
| $(E,{}^{*})$ | involutive algebra of operators, $E=\operatorname{End}_A(M)$ |
| $\operatorname{Sym}(M)$ | self-adjoint operators, $f^{*}=f$ |
| $\operatorname{Skew}(M)$ | skew-adjoint operators, $f^{*}=-f$ |
| $\operatorname{Re}f$, $\operatorname{Im}f$ | $\frac12(f+f^{*})$ and $\frac12(f-f^{*})$ |
| $U(M)$ | unitary group, $u^{*}u=uu^{*}=\mathrm{id}$ |
| $\operatorname{cong}_g(f)=g^{*}fg$ | congruence by $g$ |
| $f\sim h$ | unitarily equivalent, $h=ufu^{*}$ |
| $L_a^{*}=L_{\sigma(a)}$ | the involution on the action |
| $f\circ g=\frac12(fg+gf)$ | the Jordan product on the self-adjoint part |

## Further Reading

- Nicolas Bourbaki, *Algebra I*, Chapters 1–3 (Springer, 1998), for involutions, sesquilinear forms and their unitary groups.
- Israel N. Herstein, *Noncommutative Rings* (Mathematical Association of America, 1968), for symmetric and antisymmetric elements of an involutive ring.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, American Mathematical Society Colloquium Publications 44 (1998), for involutions, their symmetric elements and the unitary groups they define.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, second edition, 2001), for involutions, congruence and matrix examples.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the operator identities in an involutive algebra of endomorphisms.
