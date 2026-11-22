# __Classification of the Complex Structures of the Operators of the Biquaternion Algebra, including Lie Algebras and Lie Groups in $M_2(\mathbb{C})$__

## Introduction

**The question.** Two scalar extensions act on the operator algebra: $\mathcal{E}_{\mathbb{C}}\otimes_{\mathbb{R}}\mathbb{C}\cong M_4(\mathbb{C})\oplus M_4(\mathbb{C})$ and $\mathcal{E}_{\mathbb{R}}\otimes_{\mathbb{R}}\mathbb{C}\cong M_8(\mathbb{C})$. This article classifies their real structures and real forms, and describes the layers above them.

**Why it is the same statement.** This is the in-depth matrix reading of [Classification of the Complex Structures of the Operators of the Biquaternion Algebra, including Lie Algebras and Lie Groups](classification-of-the-complex-structures-of-the-operators-of-the-biquaternion-algebra.html). The source proves the direct-sum splitting and counts the structures abstractly; the display writes the splitting as the rule $\Phi(A\otimes z)=(zA,\bar zA)$ on $4\times4$ matrices and computes every fixed set in coordinates. The statements are the same statements, and only the writing is new.

**What the article proves.** In this order. The first complexification is the direct sum $M_4(\mathbb{C})\oplus M_4(\mathbb{C})$, with an isomorphism that is real and not complex. The two central idempotents give a trivial Peirce cut, in contrast with the non-central cut of a rank-one projection, whose blocks have dimensions $1,3,3,9$. The sum has five real structures and four real algebras: the two unmixed sums, the mixed sum and the slanted realification. The second complexification $M_8(\mathbb{C})$ is simple and has two real forms. The diagonal correspondence is two into four. The associative layer is Goursat's theorem, the Lie layer carries the Killing inertias $(18,12)$, $(10,20)$, $(14,16)$, $(15,15)$, and the trace form does not separate the last two.

**What the article does not do.** It does not classify the full subalgebra lattices of the four real algebras, which is not known in closed form. It does not reprove the two real forms of $M_4(\mathbb{C})$, which is [Classification of the Structures of the Operators of the Biquaternion Algebra in $M_2(\mathbb{C})$](classification-of-the-structures-of-the-operators-of-the-biquaternion-algebra-in-m2c.html), and it does not develop the two forms of the split case, which is [Classification of the Real Structures of the Operators of the Biquaternion Algebra, including Lie Algebras and Lie Groups in $M_2(\mathbb{C})$](classification-of-the-real-structures-of-the-operators-of-the-biquaternion-algebra-in-m2c.html).

**Conventions.** The display is $\mathsf M_2(\tilde Q)=Q_t\mathrm I_2-i(Q_x\sigma_1+Q_y\sigma_2+Q_z\sigma_3)$. $\mathcal{E}_{\mathbb{C}}=M_4(\mathbb{C})$ in the frame $(E_t,E_x,E_y,E_z)$ with $E_t=\mathrm I_2$, $E_x=-i\sigma_1$, $E_y=-i\sigma_2$, $E_z=-i\sigma_3$. The real structures of a factor are $\tau_{\mathbb{R}}(A)=\bar A$ and $\tau_{\mathbb{H}}(A)=J_0\bar AJ_0^{-1}$. A pair is written $(A,B)$, first slot first. Inertias are (positive, negative).

**Boundaries.** The two-sided operators are [Operators Acting on Two Sides in $M_2(\mathbb{C})$](operators-acting-on-two-sides-in-m2c.html). The elements of the display and the four sectors are [Introduction to the Operators on the Four Sectors in $M_2(\mathbb{C})$](introduction-to-the-operators-on-the-four-sectors-in-m2c.html). The spin groups are [From the Spin Group to the Spin of a Single Rotor in $M_2(\mathbb{C})$](from-the-spin-group-to-the-spin-of-a-single-rotor-in-m2c.html). The $n=2$ spine is [The One-Sided Operators at $n=2$](the-one-sided-operators-at-n-2.html) and [The Two-Sided Operators and the Segre Cone at $n=2$](the-two-sided-operators-and-the-segre-cone-at-n-2.html), and the display is [$M_2(\mathbb{C})$ Pauli Representation : Operators](m2c-pauli-representation-operators.html).

**Letters.** $\Phi$ is the splitting isomorphism; $E_1,E_2$ the two central idempotents; $\iota_{\mathrm{sc}}$ and $\iota_{\mathrm{d}}$ the scalar and diagonal embeddings; $A_0$ a real form of $\mathcal{E}_{\mathbb{C}}$; $K$ the Killing form.

## The Two Complexifications

**The two operators.** $\mathcal{E}_{\mathbb{C}}=M_4(\mathbb{C})$ of complex dimension sixteen sits inside $\mathcal{E}_{\mathbb{R}}=M_8(\mathbb{R})$ as its complex-linear part, of real dimension thirty-two inside sixty-four.

**The first complexification.** $\mathcal{E}^{\oplus2}_{\mathbb{C}}=\mathcal{E}_{\mathbb{C}}\otimes_{\mathbb{R}}\mathbb{C}$, of complex dimension thirty-two, because the ground field of the tensor is $\mathbb{R}$.

**Proposition (the splitting).** The rule
$$
\Phi(A\otimes z)=(zA,\ \bar zA)
$$
is an isomorphism of real algebras $\mathcal{E}_{\mathbb{C}}\otimes_{\mathbb{R}}\mathbb{C}\to\mathcal{E}_{\mathbb{C}}\oplus\mathcal{E}_{\mathbb{C}}$, verified as multiplicative on random $A,B,z,w$ to $6\cdot10^{-15}$.

*Proof.* Bilinearity over $\mathbb{R}$ is clear; multiplicativity is
$$
(zA,\bar zA)(wB,\bar wB)=(zwAB,\overline{zw}AB).
$$
Surjectivity follows from $A=\tfrac12(U+V)$, $B=-\tfrac{i}2(U-V)$, and the dimensions agree at sixty-four.

**The isomorphism is real and not complex.** The complex structure of the tensor sits in the second slot and is carried to $z*(U,V)=(zU,\bar zV)$, which is not the product complex structure. The second summand carries the conjugate structure, and $M_4(\mathbb{C})$ is isomorphic to its conjugate by the transpose, so the sum is $M_4(\mathbb{C})\oplus M_4(\mathbb{C})$ as a complex algebra.

**The second complexification.** $\mathcal{E}_{\mathbb{R}}\otimes_{\mathbb{R}}\mathbb{C}\cong M_8(\mathbb{R})\otimes_{\mathbb{R}}\mathbb{C}\cong M_8(\mathbb{C})$, of complex dimension sixty-four.

**The inclusion.** $\mathcal{E}^{\oplus2}_{\mathbb{C}}\cong M_4(\mathbb{C})\oplus M_4(\mathbb{C})\subset M_8(\mathbb{C})$, of codimension thirty-two. In matrices the image is the algebra of operators on $\mathbb{C}^8$ preserving the splitting of $\mathbb{C}^8$ into two copies of $\mathbb{C}^4$ that the complex structure of the carrier produces.

**The master table.**

| algebra | ground field | dimension | centre |
|---|---|---|---|
| $\mathcal{E}^{\oplus2}_{\mathbb{C}}\cong M_4(\mathbb{C})\oplus M_4(\mathbb{C})$ | $\mathbb{C}$ | $32$ complex | $\mathbb{C}\oplus\mathbb{C}$ |
| $\mathcal{E}_{\mathbb{R},\mathbb{C}}\cong M_8(\mathbb{C})$ | $\mathbb{C}$ | $64$ complex | $\mathbb{C}\mathrm I_8$ |

## The Two Central Idempotents and the Trivial Peirce Cut

**The idempotents.** $E_1=(\mathrm I_4,0)$ and $E_2=(0,\mathrm I_4)$ are idempotent, orthogonal, sum to the identity, and are central. They are the only nonzero central idempotents, since a central idempotent is a pair of scalars in $\{0,1\}$.

**The Peirce decomposition.** The off-diagonal blocks vanish,
$$
E_1(A,B)E_2=(0,0)=E_2(A,B)E_1,
$$
so the decomposition is $A_{11}\oplus A_{22}=M_4(\mathbb{C})\oplus0\oplus0\oplus M_4(\mathbb{C})$.

**The contrast with a non-central cut.** For a rank-one projection $P$ of $M_4(\mathbb{C})$ the four blocks $PM_4P$, $PM_4(\mathrm I_4-P)$, $(\mathrm I_4-P)M_4P$ and $(\mathrm I_4-P)M_4(\mathrm I_4-P)$ have complex dimensions $1,3,3,9$, computed from a random unit vector and verified as matrix ranks, and none of the off-diagonal blocks vanishes. The central cut separates two ideals; the non-central cut separates four corners of a simple algebra.

**Why the cut is trivial.** The family is central, so the two components are ideals. This says nothing about subalgebras, which may hold only the pairs satisfying a relation.

## Five Real Structures and Four Real Algebras

**The real structures of a factor.** $M_4(\mathbb{C})$ has the two real structures $\tau_{\mathbb{R}}(A)=\bar A$ and $\tau_{\mathbb{H}}(A)=J_0\bar AJ_0^{-1}$, with fixed algebras $M_4(\mathbb{R})$ and $M_2(\mathbb{H})$ and trace-form inertias $(10,6)$ and $(6,10)$.

**Theorem (the real structures of the sum).** A real structure of $A\oplus A$, with $A=M_4(\mathbb{C})$, either preserves or exchanges the two simple summands.

- Preserving: $\theta=\theta_1\times\theta_2$ with each $\theta_i$ one of the two, four maps.
- Exchanging: $\theta(A,B)=(\varphi(B),\varphi^{-1}(A))$ with $\varphi$ a conjugate-linear automorphism, and all such are conjugate.

Hence five real structures and four isomorphism classes of fixed algebra:
$$
M_4(\mathbb{R})\oplus M_4(\mathbb{R}),\quad
M_2(\mathbb{H})\oplus M_2(\mathbb{H}),\quad
M_4(\mathbb{R})\oplus M_2(\mathbb{H}),\quad
M_4(\mathbb{C})^{\mathrm{swap}}_{\mathbb{R}}.
$$

*Proof.* A conjugate-linear automorphism permutes the two-element set of simple ideals. In the exchanging case $\theta^2=1$ forces the inverse in the second slot, and $\varphi=\operatorname{Ad}_G\circ\tau_{\mathbb{R}}$ by Skolem–Noether; conjugation by $(1,U)$ replaces $G$ by $G\bar U$, which runs over $GL_4(\mathbb{C})$.

**The five structures.**

| real structure | fixed algebra | $\dim_{\mathbb{R}}$ | type |
|---|---|---|---|
| $\tau_{\mathbb{R}}\times\tau_{\mathbb{R}}$ | $M_4(\mathbb{R})\oplus M_4(\mathbb{R})$ | $32$ | split $\oplus$ split |
| $\tau_{\mathbb{R}}\times\tau_{\mathbb{H}}$ | $M_4(\mathbb{R})\oplus M_2(\mathbb{H})$ | $32$ | mixed |
| $\tau_{\mathbb{H}}\times\tau_{\mathbb{R}}$ | $M_2(\mathbb{H})\oplus M_4(\mathbb{R})$ | $32$ | mixed, other order |
| $\tau_{\mathbb{H}}\times\tau_{\mathbb{H}}$ | $M_2(\mathbb{H})\oplus M_2(\mathbb{H})$ | $32$ | quaternionic $\oplus$ quaternionic |
| $\theta(A,B)=(\bar B,\bar A)$ and twists | $\{(A,\bar A)\}\cong M_4(\mathbb{C})^{\mathrm{swap}}_{\mathbb{R}}$ | $32$ | slanted |

**The swap exchanges the mixed pair.** $s(A,B)=(B,A)$ satisfies $s\circ(\tau_{\mathbb{R}}\times\tau_{\mathbb{H}})\circ s^{-1}=\tau_{\mathbb{H}}\times\tau_{\mathbb{R}}$, so the two mixed structures are conjugate. Five structures, four algebras; the two counts are different counts and both are used.

**The slanted form.** The fixed set of the exchange structure is $\{(A,\bar A)\}$, of real dimension thirty-two, and it is isomorphic to the realification $M_4(\mathbb{C})_{\mathbb{R}}$ by $(A,\bar A)\mapsto A$.

**The trace-form inertias.**
$$
(20,12),\qquad (12,20),\qquad (16,16),\qquad (16,16).
$$
The last is $\operatorname{Re}\operatorname{tr}(A^2)=\operatorname{tr}(X^2)-\operatorname{tr}(Y^2)$ for $A=X+iY$, which is $(10,6)+(6,10)$, verified on a real basis of thirty-two elements.

**Which invariant separates.** Simplicity separates the slanted form from the three sums, and the multiset of summand types separates the three sums. The trace form does not separate the mixed sum from the slanted form, both $(16,16)$; the Killing form does, in the table below.

## The Two Real Forms of the Second Complexification

**The algebra is simple.** $M_8(\mathbb{C})$ has no two-sided ideals, so its real structures are the real forms of a simple complex algebra, and there are two:
$$
M_8(\mathbb{R}),\qquad M_4(\mathbb{H}),
$$
with trace-form inertias $(36,28)$ and $(28,36)$. The counts $36+28=64$ and $28+36=64$ are the dimension counts.

**Why two.** The real forms of $M_m(\mathbb{C})$ correspond to the classes of the Brauer group of $\mathbb{R}$, which has two elements; the split form is $M_m(\mathbb{R})$ and the quaternionic form is $M_{m/2}(\mathbb{H})$ at even $m$.

**The contrast with the first complexification.** The first complexification has two simple ideals and five real structures; the second is simple and has two. Simplicity is the reason the second count is the count of the real forms of a simple algebra and not a count of permutations of summands.

**The table.**

| algebra | simple | real forms | inertias |
|---|---|---|---|
| $M_4(\mathbb{C})\oplus M_4(\mathbb{C})$ | no, two ideals | $4$ classes from $5$ structures | $(20,12)$, $(12,20)$, $(16,16)$, $(16,16)$ |
| $M_8(\mathbb{C})$ | yes | $2$ | $(36,28)$, $(28,36)$ |

## The Biquaternion Base Inside the Complexifications

**The regular families.** $\mathrm I_2\otimes M_2(\mathbb{C})$ and $M_2(\mathbb{C})^{\mathsf T}\otimes\mathrm I_2$ are complex subspaces of $\mathcal{E}_{\mathbb{C}}$ of dimension four, and their images under $(A,B)\mapsto(A,A)$ and $(A,B)\mapsto(A,\bar A)$ are the two real-forms of the base inside the complexification.

**The element copy.** $L(M_2(\mathbb{C}))\cong M_2(\mathbb{C})$ sits inside $\mathcal{E}^{\oplus2}_{\mathbb{C}}$ diagonally, in both slots, and its conjugate sits in the slanted copy with one slot conjugated. The display writes the two embeddings as
$$
A\longmapsto(\mathsf M_2(\tilde Q),\mathsf M_2(\tilde Q)),\qquad
A\longmapsto(\mathsf M_2(\tilde Q),\overline{\mathsf M_2(\tilde Q)}),
$$
and the second is the slanted one.

**Inside the second complexification.** $M_4(\mathbb{C})\oplus M_4(\mathbb{C})\subset M_8(\mathbb{C})$ carries the base as two diagonal blocks of $4\times4$ matrices, and the base of the base, $L(\mathbb{H})\cong\mathbb{H}$, appears as a four-real-dimensional subspace in each block.

**The real forms of the base.** The split copy $L(M_2(\mathbb{R}))$ and the quaternionic copy $L(\mathbb{H})$ sit in the two real forms $M_4(\mathbb{R})$ and $M_2(\mathbb{H})$, and their complexifications are the same complex subspace by the identity $M_2(\mathbb{R})\otimes\mathbb{C}=\mathbb{H}\otimes\mathbb{C}=M_2(\mathbb{C})$.

## The Diagonal Correspondence

**The two maps.** For a real form $A_0$ of $\mathcal{E}_{\mathbb{C}}$,
$$
\iota_{\mathrm{sc}}(A)=(A,\bar A),\qquad \iota_{\mathrm{d}}(A)=(A,A).
$$
Both are injective homomorphisms of real algebras with image of real dimension sixteen.

**The maps as block arrays.** An element of the second complexification is one $8\times8$ array, and the two maps read
$$
\iota_{\mathrm{sc}}(A)=\begin{pmatrix}A&0\\0&\bar A\end{pmatrix},
\qquad
\iota_{\mathrm{d}}(A)=\begin{pmatrix}A&0\\0&A\end{pmatrix},
$$
in the two diagonal $4\times4$ blocks. For $A=\mathrm I_2$ both give the identity of $M_8(\mathbb{C})$; for $A=E_1$ the first gives
$$
\begin{pmatrix}E_1&0\\0&-E_1\end{pmatrix},
$$
verified. The off-diagonal blocks are zero in both maps, which is why the images lie in the sum of the two blocks.

**The coincidence.** For $A_0=M_4(\mathbb{R})$ the two maps coincide, since $\bar A=A$. For $A_0=M_2(\mathbb{H})$ they differ, since $\bar A=J_0^{-1}AJ_0$ is not $A$ in general.

**The correspondence.** $A_0\mapsto A_0\oplus A_0$ sends $M_4(\mathbb{R})$ to the split sum and $M_2(\mathbb{H})$ to the quaternionic sum, and it is injective and not surjective: the mixed sum and the slanted form are not of that shape.

**Why the two exclusions.** The mixed form is a sum of two non-isomorphic simple ideals, while $A_0\oplus A_0$ has two isomorphic ones. The slanted form is simple, while $A_0\oplus A_0$ never is.

**The warning.** The diagonal map $A\mapsto(A,A)$ starts from a real form of real dimension sixteen; the two-sided span $A_0\otimes A_0^{\mathrm{op}}\cong M_4(\mathbb{R})$ starts from an element form of real dimension four and lands inside $\mathcal{E}_{\mathbb{C}}$, not in its complexification. The two agree only in that the split span is the image of the diagonal map for the split form.

## Associative Subalgebras of the Complexified Algebras

**The structural theorem.** A subalgebra $S\subset A\oplus A$ has two projections $S_1,S_2$, and it is the fibre product of a quotient of $S_1$ and a quotient of $S_2$ over a common quotient: there are ideals $I_i\triangleleft S_i$ and an isomorphism $S_1/I_1\cong S_2/I_2$ such that
$$
S=\{(a,b)\in S_1\oplus S_2:\ f_1(a)=f_2(b)\}.
$$
This is Goursat's theorem, and it is the classification of the subalgebras of a direct sum.

**The three shapes.** The graph of an isomorphism $S_1\to S_2$, the full product $S_1\oplus S_2$, and the fibre product over a proper common quotient. At $B=M_2(\mathbb{C})$ the common quotients range over $\mathbb{C}$, $M_2(\mathbb{C})$, $M_2(\mathbb{C})\oplus M_2(\mathbb{C})$ and the matrix algebras above the base, so the fibre-product shape is the generic one.

**The distinguished members.** The diagonal $M_4(\mathbb{C})$, the two summands, the biquaternion base $L(M_2(\mathbb{C}))$ in each slot, and the graph of the transpose, of complex dimension sixteen.

**The second complexification.** $M_8(\mathbb{C})$ is simple, so the same dictionary applies with $n=8$ and the maximal proper subalgebras are the stabilizers of subspaces, of dimensions $1+7+49=57$, $16+16+16=48$ and the like.

## Lie Subalgebras and Killing Forms

**The two forms.** The trace form $(X,Y)\mapsto\operatorname{tr}(XY)$ and the Killing form, which is $2n$ times the trace form on the traceless part. On $\mathfrak{gl}(4,\mathbb{F})$ at $n=4$,
$$
K(X,Y)=8\operatorname{tr}(XY)-2\operatorname{tr}(X)\operatorname{tr}(Y),
$$
verified on random real pairs to $4\cdot10^{-15}$.

**The table.**

| algebra | $\dim_{\mathbb{R}}$ | trace form | Killing, semisimple part | radical |
|---|---|---|---|---|
| $M_4(\mathbb{R})^{\oplus2}$ | $32$ | $(20,12)$ | $(18,12)$ | $2$ |
| $M_2(\mathbb{H})^{\oplus2}$ | $32$ | $(12,20)$ | $(10,20)$ | $2$ |
| $M_4(\mathbb{R})\oplus M_2(\mathbb{H})$ | $32$ | $(16,16)$ | $(14,16)$ | $2$ |
| $M_4(\mathbb{C})^{\mathrm{swap}}_{\mathbb{R}}$ | $32$ | $(16,16)$ | $(15,15)$ | $2$ |

**The sums add.** $K_{\mathfrak g\oplus\mathfrak h}=K_{\mathfrak g}\oplus K_{\mathfrak h}$, since the adjoint action is block diagonal, so the inertias and the radicals add. This is the only doubling in the table: $(18,12)=2(9,6)$ and $(10,20)=2(5,10)$.

**The slanted arithmetic.** For the realification the rule is $K_{\mathbb{R}}(X,Y)=2\operatorname{Re}K_{\mathbb{C}}(X,Y)$, because the realification of a complex operator has twice the real trace. On $\mathfrak{sl}(4,\mathbb{C})_{\mathbb{R}}=\mathfrak{su}(4)\oplus i\,\mathfrak{su}(4)$ the form is negative definite on the first summand and positive definite on the second, giving $(15,15)$, verified on a real basis of thirty elements. Doubling $(9,6)$ would give $(18,12)$ and is wrong.

**What each form is for.** The Killing form decides compactness and is the Lie invariant; the trace form is the invariant of the operator algebra and is the form of the biquaternion base, where $\operatorname{tr}(U_1U_2)$ is the form on the traceless part.

## The Jordan Layer

**The complexified Jordan algebras.** $M_4(\mathbb{C})^{+}\oplus M_4(\mathbb{C})^{+}$ and $M_8(\mathbb{C})^{+}$, with the symmetrized product $X\circ Y=\tfrac12(XY+YX)$.

**The idempotents.** The pair $(P,Q)$ of rank-one projections is an idempotent of the sum, and the Peirce decomposition of the Jordan algebra follows the corner decomposition of the associative one. The non-central Peirce blocks $1,3,3,9$ are the Jordan blocks of a rank-one idempotent of $M_4(\mathbb{C})^{+}$.

**The three real Jordan forms.** $M_4(\mathbb{R})^{+}$, $M_2(\mathbb{H})^{+}$ and $H_4(\mathbb{C})$, of inertias $(10,6)$, $(6,10)$ and $(16,0)$, sit inside the complexified Jordan algebra as its real forms, exactly as the associative ones do.

## Where $n=2$ Differs

**The dimensions.** At the element level the first complexification is $M_2(\mathbb{C})\oplus M_2(\mathbb{C})$ of complex dimension eight, and the second is $M_4(\mathbb{C})$ of complex dimension sixteen. At the operator level they are $32$ and $64$. Every count is multiplied by four, which is the square of the size ratio.

**The Peirce dimensions.** The non-central cut of a rank-one projection gives blocks $1,1,1,1$ at $n=2$ and $1,3,3,9$ at $n=4$. The general formula is $1$, $n-1$, $n-1$, $(n-1)^2$, and at $n=2$ the three sizes collapse.

**The counts of structures do not change.** Five real structures and four real algebras at both levels, and two real forms of the simple complexification at both levels. The reason is that a real structure of $A\oplus A$ permutes two summands and does not see the size of $A$.

**The inertia numbers change.** $(10,6)$ against $(6,10)$ at $n=4$ becomes $(3,1)$ against $(1,3)$ at $n=2$, and the slanted inertia $(15,15)$ on $\mathfrak{sl}(4,\mathbb{C})_{\mathbb{R}}$ becomes $(3,3)$ on $\mathfrak{sl}(2,\mathbb{C})_{\mathbb{R}}\cong\mathfrak{so}(3,1)$.

## Summary

The two complexifications are $\mathcal{E}_{\mathbb{C}}\otimes_{\mathbb{R}}\mathbb{C}\cong M_4(\mathbb{C})\oplus M_4(\mathbb{C})$, of complex dimension thirty-two, and $\mathcal{E}_{\mathbb{R}}\otimes_{\mathbb{R}}\mathbb{C}\cong M_8(\mathbb{C})$, of dimension sixty-four. The splitting is $\Phi(A\otimes z)=(zA,\bar zA)$, an isomorphism of real algebras, verified multiplicative to $6\cdot10^{-15}$, and not an isomorphism of complex algebras, because the second summand carries the conjugate structure.

The first complexification has the two central idempotents $E_1=(\mathrm I_4,0)$ and $E_2=(0,\mathrm I_4)$, a trivial Peirce cut, and five real structures: the four preserving ones and the exchanging one. The four real algebras are $M_4(\mathbb{R})^{\oplus2}$, $M_2(\mathbb{H})^{\oplus2}$, the mixed sum and the slanted realification, with trace inertias $(20,12)$, $(12,20)$, $(16,16)$, $(16,16)$. The second complexification is simple, with the two real forms $M_8(\mathbb{R})$ and $M_4(\mathbb{H})$.

The diagonal correspondence $A_0\mapsto A_0\oplus A_0$ is two into four: the mixed and the slanted forms are not diagonal. The associative layer is Goursat's theorem. The Killing inertias are $(18,12)$, $(10,20)$, $(14,16)$, $(15,15)$, and the Killing form separates the four algebras where the trace form does not.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Phi$ | the splitting $(A\otimes z)\mapsto(zA,\bar zA)$ |
| $E_1,E_2$ | the central idempotents of the sum |
| $\tau_{\mathbb{R}},\tau_{\mathbb{H}}$ | the two real structures of a factor |
| $\iota_{\mathrm{sc}},\iota_{\mathrm{d}}$ | the slanted and the diagonal embeddings |
| $M_4(\mathbb{C})^{\mathrm{swap}}_{\mathbb{R}}$ | the slanted realification |
| $K$ | the Killing form |

## Further Reading

- [Classification of the Complex Structures of the Operators of the Biquaternion Algebra, including Lie Algebras and Lie Groups](classification-of-the-complex-structures-of-the-operators-of-the-biquaternion-algebra.html), for the source's abstract splitting and its comparison with the element level.
- [Classification of the Real Structures of the Operators of the Biquaternion Algebra, including Lie Algebras and Lie Groups in $M_2(\mathbb{C})$](classification-of-the-real-structures-of-the-operators-of-the-biquaternion-algebra-in-m2c.html), for the two real forms whose complexification this article splits.
- [Classification of the Structures of the Operators of the Biquaternion Algebra in $M_2(\mathbb{C})$](classification-of-the-structures-of-the-operators-of-the-biquaternion-algebra-in-m2c.html), for the double centralizer and the biquaternion base.
- [The Adjoints and the Polar Decomposition of an Operator at $n=2$](the-adjoints-and-the-polar-decomposition-of-an-operator-at-n-2.html), for the real structures as conjugations of the operator space.
- [The Lie Correspondence and the Adjoint Representation](the-lie-correspondence-and-the-adjoint-representation.html), for the group theory attached to the inertias.
