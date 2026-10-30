# __The Four Uses of Spin in the Biquaternion Algebra__

## Introduction

The question *which spins does the biquaternion algebra carry* has no answer until the structure is named. The Chirality article lists four algebraic uses of the word. They are not four notions: one is the definition, one is its adjoint instance, and two are signs that are not weights at all.

This article separates the four, then answers the highest-weight question exactly. The answer is a table of four uses, a definition, a closure theorem with exactly two structures, and an arithmetic obstruction that explains why no single list exists.

The thesis is short. There is **one** definition of spin, the highest weight of a module structure. There is **one** instance of it that is easily mistaken for a second definition, the adjoint action. And there are **two** signs that sit beside it but are not weights: the Peirce index and the chirality.

The highest-weight question has two module structures, and the values $0,\tfrac12,1$ are the union of the two lists. The union is not a direct sum. The reason is arithmetic: a single module structure on $\mathbb{B}$ would need $1+2+3=6$ states in a space of complex dimension $4$.

## The Four Uses

| use | what it labels | structure | values |
|---|---|---|---|
| highest weight | the representation | Casimir of a module structure | $0,\ \tfrac12,\ 1$ |
| adjoint action (traceless part) | the vector carrier | conjugation on the algebra | $1$ |
| Peirce index | the copy | Peirce decomposition | $+$ or $-$ |
| chirality | the Lorentz half | central sign in $\mathbb{B}[j]$ | $+$ or $-$ |

The first two rows are one notion. The adjoint action carries the two integer cases, $j=0$ on the centre and $j=1$ on the traceless part; the row records the $j=1$ carrier. The last two rows are signs, and neither is a weight.

**The Peirce index.** A complete family $\tilde\Pi_+,\tilde\Pi_-$ cuts the algebra into four lines $\mathbb{B}_{st}=\tilde\Pi_s\mathbb{B}\tilde\Pi_t$. The indices $s,t$ are the Peirce indices. The right index selects the copy: $S_+=\mathbb{B}\tilde\Pi_+$ and $S_-=\mathbb{B}\tilde\Pi_-$. Both copies carry spin $\tfrac12$. The Peirce index does not distinguish a spin from another spin; it distinguishes two copies of the same spin.

**The chirality.** In the complexification $\mathbb{B}[j]\cong\mathbb{B}\oplus\mathbb{B}$, with $j$ a central imaginary unit, $j^2=-e_t$, commuting with the algebra, the chirality is $\chi=ij$. It satisfies $\chi^2=+e_t$, and the central idempotents are $e_\pm=\tfrac12(e_t\pm\chi)$, with $\chi e_\pm=\pm e_\pm$. The two idempotents split the doubled algebra into two chiral halves. Chirality is a Lorentz label, not a rotation label: on the rotation subgroup the two halves carry the same spin.

So the four uses reduce to one definition, one instance and two signs. The rest of the article is the definition and its two structures.

## The Definition

**The group.** Let $G$ be the group of unit real quaternions,

$$
G=\{u\in\mathbb{H}_{\mathbb{B}}:uu^*=e_t\},
$$

with Lie algebra $\mathfrak{g}=\mathbb{H}_{\mathbb{B}}\cap\mathbb{M}_-=\operatorname{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z\}$.

**Structure.** A structure over $\mathbb{B}$ is a pair $(W,\rho)$ where $W$ is a finite-dimensional complex space and $\rho$ is either an algebra homomorphism $\rho:\mathbb{B}\to\operatorname{End}_{\mathbb{C}}(W)$ or a Lie-algebra homomorphism $\rho:\mathfrak{g}\to\operatorname{End}_{\mathbb{C}}(W)$. A **carrier** is such a pair with $W\neq0$. The two cases are kept apart throughout: the first is an associative module, the second is a module over a Lie algebra, and only the first is a module over $\mathbb{B}$.

**Irreducible.** A carrier is irreducible when its only invariant subspaces are $0$ and $W$. Irreducibility is a property of the pair, not of the dimension. A bare dimension carries no spin: over $\mathbb{B}\cong M_2(\mathbb{C})$ an associative module of complex dimension $n$ exists only for even $n$, and it is $S^{\oplus n/2}$.

**Subcarrier.** A **subcarrier of the regular module** is a nonzero subspace $W\subseteq\mathbb{B}$, invariant under $\lambda$ or under $\mathrm{ad}$, with the restricted action. The closure theorem below classifies the irreducible subcarriers and says nothing about carriers that are not subspaces of $\mathbb{B}$: a Lie-algebra module of $\mathfrak{g}$ exists in every dimension $2j+1$, so spin $\tfrac32$ and spin $2$ are carriers under the definition even though no subspace of $\mathbb{B}$ carries them.

**Generators.** For a carrier $(W,\rho)$, the rotation generators are

$$
J_k=\tfrac12\rho(i\vec e_k),
$$

so that $[J_i,J_j]=i\epsilon_{ijk}J_k$. The map $\rho$ is extended $\mathbb{C}$-linearly, so $\rho(i\vec e_k)$ is defined although $i\vec e_k\notin\mathfrak{g}$. On the two carriers below the trace form $\langle X,Y\rangle=\operatorname{tr}(X^*Y)$ makes each $J_k$ self-adjoint, hence with real spectrum; here $X^*$ is the biquaternion conjugate, complex conjugation composed with quaternion conjugation.

**Spin.** For a unit $\vec u\in\mathfrak{g}$, $uu^*=e_t$, the **spin** of an irreducible carrier is

$$
j=\max\operatorname{spec}\bigl(\vec u\cdot\vec J\bigr).
$$

The value does not depend on $\vec u$: any two unit elements of $\mathfrak{g}$ are conjugate in $G$, and conjugate operators have the same spectrum.

**Proposition.** On an irreducible carrier, $C=J_1^2+J_2^2+J_3^2=j(j+1)$ and $2j+1=\dim_{\mathbb{C}}W$.

**Proof.** Take $\vec u=\vec e_z$, so that $j$ is the largest eigenvalue of $J_3$. The ladder operators $J_\pm=J_1\pm iJ_2$ satisfy $[J_3,J_\pm]=\pm J_\pm$, so they shift weights by $1$. Finite dimension stops the ladder above at the highest weight $j$ and below at the lowest weight $j'$. The string generated from the top is invariant and nonzero, so by irreducibility it is all of $W$; its weights are $j,j-1,\dots,j'$. On a top vector $v$, $J_+v=0$ and $C=J_-J_++J_3(J_3+1)$ give $C=j(j+1)$. On a bottom vector $v'$, $J_-v'=0$ and $C=J_+J_-+J_3(J_3-1)$ give $C=j'(j'-1)$. Hence $j'(j'-1)=j(j+1)$, whose only solution with $j'\le j$ is $j'=-j$. The weights are $-j,-j+1,\dots,j$, there are $2j+1$ of them, and $C=j(j+1)$.

The formula $j=(n-1)/2$ is therefore a theorem about the pair, never a definition applied to a bare dimension.

## The Two Module Structures

The product of $\mathbb{B}$ induces two structures, and they are of different kinds.

**Left multiplication.** The map

$$
\lambda:\mathbb{B}\longrightarrow\operatorname{End}_{\mathbb{C}}(\mathbb{B}),\qquad
\lambda_Q(X)=QX,
$$

is an algebra homomorphism. It makes $\mathbb{B}$ a left module over itself. Restricted to $G$ it is two copies of the defining action.

**Conjugation.** The map

$$
\mathrm{Ad}:G\longrightarrow\mathrm{GL}_{\mathbb{C}}(\mathbb{B}),\qquad
\mathrm{Ad}_u(X)=uXu^{-1},
$$

is a group homomorphism, and its differential

$$
\mathrm{ad}:\mathfrak{g}\longrightarrow\operatorname{End}_{\mathbb{C}}(\mathbb{B}),\qquad
\mathrm{ad}_a(X)=aX-Xa,
$$

is a Lie-algebra homomorphism. This is **not** an algebra homomorphism of $\mathbb{B}$: $\mathrm{ad}_a^2\neq\mathrm{ad}_{a^2}$ in general. The second structure is a module over the Lie algebra, equivalently over its enveloping algebra, and it is not a module over the associative algebra $\mathbb{B}$.

That difference of kind is the source of every confusion in this subject. The two structures are both canonical, both induced by the product, and they are not two versions of one thing.

**Right multiplication.** The map $X\mapsto XQ$ is an algebra anti-homomorphism; it makes $\mathbb{B}$ a right module, and since $\mathbb{B}^{\mathrm{op}}\cong\mathbb{B}$ it gives the same constituents as the left structure. Up to equivalence there are therefore two structures: the associative one and the Lie one.

## The Left Module: Dimension Two

**The constituents.** The algebra is a left module over itself, and

$$
\mathbb{B}=S_+\oplus S_-,\qquad S_\pm=\mathbb{B}\tilde\Pi_\pm,
$$

with $S_+\cong S_-\cong S$ the simple left module, of complex dimension $2$. Every left module over $\mathbb{B}\cong M_2(\mathbb{C})$ is a direct sum of copies of $S$, so the only irreducible left carrier is $S$, and it occurs twice.

**The weights.** With $J_k=\tfrac12\lambda_{i\vec e_k}$ and the standard family $\tilde\Pi_\pm=\tfrac12(e_t\pm i\vec e_z)$,

$$
J_3\tilde\Pi_+=\tfrac12\tilde\Pi_+,\qquad
J_3\vec\Upsilon_{-+}=-\tfrac12\vec\Upsilon_{-+},
$$

on the adapted basis $(\tilde\Pi_+,\vec\Upsilon_{-+})$ of $S_+$, with $\vec\Upsilon_{-+}=\tfrac12(i\vec e_x+\vec e_y)$. The first identity uses $(i\vec e_z)^2=+e_t$, so that $i\vec e_z\tilde\Pi_+=\tilde\Pi_+$.

**The Casimir.** Because $\lambda$ is an algebra homomorphism, the same identity gives the Casimir in one line:

$$
C=\frac14\sum_k\bigl(\lambda_{i\vec e_k}\bigr)^2
=\frac14\sum_k\lambda_{(i\vec e_k)^2}
=\frac14\sum_k\lambda_{e_t}
=\frac34\operatorname{id}.
$$

**The result.** $C=\tfrac34=j(j+1)$ gives $j=\tfrac12$, and $2j+1=2$.

## The Adjoint Module: Dimensions One and Three

**The constituents.** Conjugation fixes the centre and preserves the traceless part, so

$$
\mathbb{B}=Z\oplus V,\qquad Z=\mathbb{C}e_t,\qquad V=\ker\operatorname{tr}.
$$

The centre is one-dimensional and trivial. The traceless part is the adjoint representation of $\mathfrak{sl}_2(\mathbb{C})$.

**The weights.** With $J_k=\tfrac12\mathrm{ad}_{i\vec e_k}$ and

$$
\varepsilon_\pm=\mp\tfrac{1}{\sqrt2}(\vec e_x\pm i\vec e_y),\qquad\varepsilon_0=\vec e_z,
$$

the signs being the Condon–Shortley phase, chosen so that the ladder coefficients are positive. One has

$$
J_3\varepsilon_\pm=\pm\varepsilon_\pm,\qquad J_3\varepsilon_0=0,\qquad J_3 e_t=0.
$$

With $J_\pm=J_1\pm iJ_2$, the nonzero ladder actions are

$$
J_+\varepsilon_-=\sqrt2\,\varepsilon_0,\qquad J_+\varepsilon_0=\sqrt2\,\varepsilon_+,\qquad J_-\varepsilon_+=\sqrt2\,\varepsilon_0,\qquad J_-\varepsilon_0=\sqrt2\,\varepsilon_-,
$$

and $J_+\varepsilon_+=J_-\varepsilon_-=0$.

**The Casimir.** Using $C=J_3^2+\tfrac12(J_+J_-+J_-J_+)$: on $\varepsilon_\pm$, $J_3^2=1$ and $\tfrac12(J_+J_-+J_-J_+)=1$; on $\varepsilon_0$, $J_3^2=0$ and $\tfrac12(J_+J_-+J_-J_+)=2$. In all three cases $C=2$. On $Z$ the Casimir is $0$. The value $2$ is $j(j+1)$ at $j=1$.

**The result.** Two carriers, of dimensions $1$ and $3$, with spins $0$ and $1$.

The shortcut used for the left module does not apply here: $\mathrm{ad}_a^2\neq\mathrm{ad}_{a^2}$, so the sum $\sum_k\mathrm{ad}_{i\vec e_k}^2$ must be evaluated on the weight basis rather than on the products $(i\vec e_k)^2$.

## The Closure Theorem

**Theorem (closure of the subcarriers).** Let $W\subseteq\mathbb{B}$ be a nonzero subspace, invariant and irreducible under $\lambda$ or under $\mathrm{ad}$. Then, up to isomorphism, $W$ is one of $S$ (dimension $2$), $Z$ (dimension $1$), $V$ (dimension $3$).

**Proof for the left action.** A $\lambda$-invariant subspace is a left ideal. The left ideals of $M_2(\mathbb{C})$ are $0$, the minimal left ideals, and the whole algebra. Every minimal left ideal is $\mathbb{B}\tilde\Pi$ for an idempotent of rank one, and any two are isomorphic to $S$. The whole algebra is $S_+\oplus S_-$ and is reducible. So the irreducible ones are the minimal left ideals, all isomorphic to $S$.

**Proof for the adjoint action.** An $\mathrm{ad}$-invariant subspace $W$ satisfies $[\mathbb{B},W]\subseteq W$. Since $[\mathbb{B},\mathbb{B}]=V$, the centre is fixed and $V$ is preserved. Let $W$ be invariant and not contained in $Z$, and let $\pi:\mathbb{B}\to V$ be the projection along $Z$. Then $\pi(W)$ is a nonzero $\mathrm{ad}$-submodule of $V$, hence $\pi(W)=V$ by the irreducibility of the adjoint representation.

If $\dim W=3$, then $W$ is the graph of a linear map $\varphi:V\to Z$, that is, $W=\{v+\varphi(v)\}$. For $v\in V$ and $a\in\mathbb{B}$,

$$
[a,v+\varphi(v)]=[a,v],
$$

because $\varphi(v)$ is central. This element lies in $W$, so it equals $u+\varphi(u)$ with $u=[a,v]$; hence $\varphi([a,v])=0$. As $a$ and $v$ vary, $[a,v]$ ranges over $V$, so $\varphi=0$ and $W=V$. If $\dim W=4$, then $W=\mathbb{B}$, which is reducible. The irreducible invariant subspaces are therefore $Z$ and $V$.

**Corollary.** The irreducible subcarriers have dimensions $1$, $2$ and $3$. Since $2j+1=\dim_{\mathbb{C}}W$, the spins are $0$, $\tfrac12$ and $1$.

**Corollary.** No irreducible invariant subspace has dimension $4$ or more. The only four-dimensional invariant subspace is $\mathbb{B}$ itself, and it is reducible in both structures: $S_+\oplus S_-$ on the left, $Z\oplus V$ under conjugation.

**The obstruction.** Suppose a single structure on $\mathbb{B}$ contained all three subcarriers. They would be distinct irreducible submodules, since their dimensions $1,2,3$ differ, and distinct irreducible submodules intersect trivially, so their dimensions would add. A carrier of spin $j$ has $2j+1$ states, so the three would occupy

$$
1+2+3=6>4=\dim_{\mathbb{C}}\mathbb{B}
$$

states. This is impossible. The three spins are therefore never the constituents of one action; they are the union of the constituents of two actions.

**Remark, not a definition.** The two lists are the two restrictions of one irreducible object. Since $\mathbb{B}\cong\operatorname{End}_{\mathbb{C}}(S)$ with $\dim_{\mathbb{C}}S=2$, the algebra is the space of endomorphisms of the simple module. It is irreducible of complex dimension $4$ under the action of $G\times G$ by left and right multiplication. Restricting to the left factor gives $S\oplus S$; restricting to the diagonal gives $Z\oplus V$. The two lists are the two shadows of one object, and this is why there are exactly two and not three. It is a remark about where the lists come from, and it is not the definition of spin.

## Why the Dimensions Are One, Two and Three

Three descriptions of the same arithmetic.

**Matrix arithmetic.** A left ideal of $M_2(\mathbb{C})$ is a sum of columns, each of dimension $2$. The centre is the line of scalar matrices. The traceless part is the complement, of dimension $4-1=3$.

**Tensor degree.** The simple module $S$ has dimension $2$. The first three tensor degrees are

$$
\mathbb{C}\ (\text{degree }0),\qquad S\ (\text{degree }1),\qquad \operatorname{End}_{\mathbb{C}}(S)\ (\text{degree }2),
$$

of dimensions $1$, $2$ and $4$. The last splits as $\mathbf{1}\oplus\mathbf{3}$ under $G$: the identity matrix is the trivial summand and the traceless matrices are the adjoint. So the dimensions $1,2,3$ are the dimensions of the degree-$0$, degree-$1$ and traceless degree-$2$ objects.

**The truncation.** The list stops at degree $2$ because $\mathbb{B}$ *is* the degree-two object, the algebra of $2\times2$ matrices. Degree $3$ is $\operatorname{End}(S)\otimes S$, of dimension $8$, and it is not a subspace of $\mathbb{B}$. Higher spin therefore requires a tensor product: it is a carrier, but not a subcarrier of $\mathbb{B}$.

## The Three Signs

**The central sign.** A rotation by $2\pi$ is $-e_t$. On the half-integer carriers, the left modules $S_\pm$, it acts as $-\operatorname{id}$. On the integer carriers, the adjoint modules $Z$ and $V$, it acts as the identity. The sign of $-e_t$ is therefore the compact mark of the integrality class. It is not the eigenvalue of one operator on $\mathbb{B}$: on the left regular module $-e_t$ acts as $-\operatorname{id}$ on all of $\mathbb{B}$, and in the adjoint action it acts trivially on all of $\mathbb{B}$. The two signs are read in the two structures, not as the two eigenspaces of one operator.

**The Peirce sign is not the central sign.** The central element $-e_t$ acts as $-\operatorname{id}$ on $S_+$ and on $S_-$ alike; it cannot separate them. The Peirce sign is the right multiplication $P=R_{i\vec e_z}$. Since $(i\vec e_z)^2=+e_t$, $P^2=\operatorname{id}$, and

$$
P\tilde\Pi_+=\tilde\Pi_+,\qquad P\tilde\Pi_-=-\tilde\Pi_-,
$$

so $P$ is $+1$ on $S_+$ and $-1$ on $S_-$. It is implemented by the element $i\vec e_z$, which is not central: $i\vec e_z\vec e_x=+i\vec e_y$ while $\vec e_x i\vec e_z=-i\vec e_y$. The Peirce index is therefore an inner, non-central copy label, and it never changes a spin value. Right multiplication by the nilpotent $\vec\Upsilon_{+-}$ gives the module isomorphism $S_+\to S_-$, but it is not the grading: $\vec\Upsilon_{+-}^2=0$, so it cannot be an involution.

**Chirality is central, but not a spin.** In $\mathbb{B}[j]$ the chirality $\chi=ij$ is central, and $\chi^2=e_t$. Its two eigenspaces are the chiral halves $e_\pm=\tfrac12(e_t\pm\chi)$. Both halves carry the same rotation spin. Chirality distinguishes the two Lorentz chiralities, not two values of $j$.

The three signs are therefore distinct: a central sign that marks integer against half-integer, an inner non-central sign that separates two copies of one half-integer carrier, and a central sign in a doubled algebra that separates two Lorentz halves. Only the first tracks the integrality of a spin; none of the three is a spin value.

## What the Algebra Does Not Determine

**Which structure a particle uses.** The algebra carries both lists. It does not say that the electron uses the left module and the photon the adjoint; that assignment is physics.

**No dynamics.** The Casimir is a kinematical label. No mass, no Hamiltonian and no equation of motion follow from it.

**No statistics.** The algebraic split matches the two integrality classes. The spin–statistics theorem is not proved by the algebra.

**No full Lorentz label.** Under left multiplication by $SL(2,\mathbb{C})$ the algebra carries the chiral spinor $(\tfrac12,0)$ with multiplicity two; under conjugation it carries the four-vector $(\tfrac12,\tfrac12)$. The split of the four-vector into $\mathbf{1}\oplus\mathbf{3}$ is the work of the compact subgroup $G$. The rotation spin is the little-group shadow of the Lorentz label, not the whole label.

## Summary

Spin in the corpus has four uses, and they are not four notions. The highest weight of a module structure is the definition. The adjoint action carries its two integer instances, $j=0$ and $j=1$. The Peirce index and the chirality are signs, and neither is a weight.

The highest-weight question has two module structures. Left multiplication gives the simple module $S$, of dimension $2$, with weights $\pm\tfrac12$, Casimir $\tfrac34$ and spin $\tfrac12$. Conjugation gives the centre $Z$, of dimension $1$, with spin $0$, and the traceless part $V$, of dimension $3$, with weights $\pm1,0$, Casimir $2$ and spin $1$.

The closure theorem states that these are all the irreducible subcarriers. There is no fourth, and the arithmetic $1+2+3=6>4$ shows that the three can never be the constituents of one action. The three values are the union of two lists, not a single list.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | The biquaternion algebra |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | Its basis; $\vec e_k^2=-e_t$ |
| $Z=\mathbb{C}e_t$ | The centre |
| $V=\ker\operatorname{tr}$ | The traceless part |
| $G$ | The group of unit real quaternions |
| $\mathfrak{g}$ | Its Lie algebra, the real pure quaternions |
| $\lambda_Q$ | Left multiplication by $Q$ |
| $\mathrm{Ad}_u$, $\mathrm{ad}_a$ | Conjugation and its differential |
| $S$ | The simple left module, of complex dimension $2$ |
| $S_\pm=\mathbb{B}\tilde\Pi_\pm$ | The two minimal left ideals |
| $J_k$ | The rotation generators of a carrier |
| $C=J_1^2+J_2^2+J_3^2$ | The Casimir |
| $j$ | The spin, the maximal weight |
| $\mathbb{B}[j]$ | The complexification by the central imaginary unit $j$, $j^2=-e_t$ |
| $\tilde\Pi_\pm=\tfrac12(e_t\pm i\vec e_z)$ | The standard orthogonal idempotents |
| $\vec\Upsilon_{+-},\vec\Upsilon_{-+}$ | The mixed units; $\vec\Upsilon_{+-}=\tfrac12(i\vec e_x-\vec e_y)$, $\vec\Upsilon_{-+}=\tfrac12(i\vec e_x+\vec e_y)$ |
| $X^*$ | The biquaternion conjugate |

## Further Reading

- [The Category of Modules in the Biquaternion Algebra](the-category-of-modules.html), for the simple module $S$, the classification of the modules and the lines of $\mathbb{C}^2$ that index the minimal left ideals.
- [The Minimal Left Ideals in the Biquaternion Algebra](the-minimal-left-ideals.html), for the direct sum ${}_\mathbb{B}\mathbb{B}\cong S\oplus S$.
- [The Regular Module in the Biquaternion Algebra](the-regular-module.html), for the ideals and the two-sided simplicity.
- [Spinors as Peirce Coordinates in the Biquaternion Algebra](spinors-as-peirce-coordinates-in-the-biquaternion-algebra.html), for the spinor spaces, the mixed units and the ladder.
- [Chirality: The Conjugate Pair in the Biquaternion Algebra](chirality-the-conjugate-pair.html), for the Peirce sign and the central chiral sign.
- [The Casimir Operator](the-casimir-operator.html), for the general theory of the Casimir operator.
- [Representations of Lie Algebras](representations-of-lie-algebras.html), for the highest-weight classification.
- [The Determination of the Possible Spins in Biquaternionic Form](../articles_physics/the-determination-of-the-possible-spins-in-biquaternionic-form.html), for the physical interpretation.
- [Spin and the Three Elementary Carriers](../articles_physics/spin-and-the-three-elementary-carriers.html), for the carrier table and the two copies of the spin-half carrier.
