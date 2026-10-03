
# __Complex Split Biquaternions and the Clifford Algebra Cl(3)__

## Introduction

The split biquaternion algebra $\mathbb{H}_{\mathbb{D}} = \mathbb{D}\otimes_{\mathbb{R}}\mathbb{H}$ is the Clifford algebra of three generators of square $-1$. Its three anticommuting generators are the elements $j e_1, j e_2, j e_3$, where $e_1, e_2, e_3$ are the quaternion units and $j$ is the central split unit of $\mathbb{D}$ with $j^2 = +1$; the product of the three is $-j$, the central split unit again. This article studies the **complexification** of that algebra,
$$
\mathrm{Cl}(3) := \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}_{\mathbb{D}} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{D}\otimes_{\mathbb{R}}\mathbb{H},
$$
the **complex split biquaternions**. Over $\mathbb{C}$ the algebra is eight-dimensional, and its structure is fixed by a single fact: the volume element is central with square $+1$ instead of square $-1$. The centrality splits the algebra into two copies,
$$
\mathrm{Cl}(3) \cong \mathrm{Cl}(2)\oplus\mathrm{Cl}(2) \cong M_2(\mathbb{C})\oplus M_2(\mathbb{C}) \cong \mathbb{B}\oplus\mathbb{B},
$$
each copy isomorphic to the biquaternion algebra. Where $\mathrm{Cl}(2)$ is simple, $\mathrm{Cl}(3)$ is not; where $\mathrm{Cl}(2)$ has a single family of minimal left ideals, $\mathrm{Cl}(3)$ has two, and the two are interchanged by the parity automorphism $e_i\mapsto -e_i$ and distinguished by the sign of the volume element. That pair is the algebraic content of the two **chiralities** of the four-dimensional spinor representation, and it is the reason the algebra is of interest to the physics of the left-right symmetric extension of the Standard Model, treated in *Left-Right Symmetric Fermions from Complex Split Biquaternions and Bioctonions*.

The article is the Clifford entry of the split biquaternion system, the higher rung of the pair whose lower rung is *The Clifford Structure of the Biquaternion Algebra*. The split biquaternion algebra, its conjugations, its idempotents $\tilde\Pi_\pm=\tfrac12(1\pm j)$ and its isomorphism $\mathbb{H}_{\mathbb{D}}\cong\mathbb{H}\oplus\mathbb{H}$ are *Split-Biquaternion Algebra* and *Split-Biquaternion Ideals and Peirce Decomposition*; the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, its idempotents, its off-diagonal elements and its minimal left ideals are *Biquaternion Algebra* and *Biquaternion Ideals and Peirce Decomposition*; the complex Clifford algebra $\mathrm{Cl}(2)\cong\mathbb{C}\mathrm{l}_2\cong\mathbb{B}$, its volume element and its grade structure are *The Clifford Structure of the Biquaternion Algebra*; and the maximal totally isotropic subspace, the ladder operators and the charge operator are *Spinors as Minimal Left Ideals with Inner Conjugation* and *Maximal Totally Isotropic Subspaces and Their Unitary Symmetries*. The same construction one rung higher, on the octonions, is *Split Bioctonions and the Clifford Algebra Cl(7)*.

**Conventions.** The Clifford algebra $\mathrm{Cl}(3)$ is generated over $\mathbb{C}$ by $E_1,E_2,E_3$ with
$$
E_i^2=-1, \qquad E_iE_j=-E_jE_i \quad (i\neq j),
$$
so that $\{E_i,E_j\}=-2\delta_{ij}$; the eight monomials $E_1^{\epsilon_1}E_2^{\epsilon_2}E_3^{\epsilon_3}$, $\epsilon_i\in\{0,1\}$, are a $\mathbb{C}$-basis. The scalar imaginary is $i$, central, with $i^2=-1$. The Hermitian adjoint is fixed by
$$
E_i^{\dagger}=-E_i, \qquad i^{\dagger}=-i,
$$
so that the rescaled generators $\gamma_i=iE_i$ are Hermitian, $\gamma_i^{\dagger}=\gamma_i$; this is the convention of *Complex Octonions and the Clifford Algebra Cl(6)*, and it is the one that makes the volume element self-adjoint below. The split biquaternion algebra is written with quaternion units $e_0=1,e_1,e_2,e_3$ and central split unit $j$, $j^2=+1$, as in *Split-Biquaternion Algebra*. The Clifford algebra $\mathrm{Cl}(0,3)$ of three generators of square $-1$ is written in the series convention $\mathrm{Cl}_{p,q}$; the complex algebra is written interchangeably $\mathrm{Cl}(n)$ and $\mathrm{Cl}_n(\mathbb{C})$, as in *Complex Octonions and the Clifford Algebra Cl(6)*.

## The Algebra and Its Generators

**Proposition (the split biquaternion generators).** In $\mathbb{H}_{\mathbb{D}}$ the three elements
$$
E_1 := j e_1, \qquad E_2 := j e_2, \qquad E_3 := j e_3
$$
satisfy $E_i^2=-1$ and $E_iE_j=-E_jE_i$ for $i\neq j$. Hence they generate a copy of $\mathrm{Cl}(0,3)$ inside $\mathbb{H}_{\mathbb{D}}$, and $\mathbb{H}_{\mathbb{D}}\cong\mathrm{Cl}(0,3)$.

*Proof.* Since $j$ is central with $j^2=+1$ and the quaternion units anticommute with $e_i^2=-1$,
$$
E_i^2 = j^2e_i^2 = -1, \qquad E_iE_j = j^2e_ie_j = e_ie_j = -e_je_i = -E_jE_i \quad(i\neq j).
$$
The eight monomials are independent and span $\mathbb{H}_{\mathbb{D}}$, so the generated algebra is the whole of it. The split biquaternion algebra is therefore the Clifford algebra of a three-dimensional negative definite space. $\square$

**Proposition (the complex split biquaternions).** The complexification
$$
\mathrm{Cl}(3) = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}_{\mathbb{D}} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{D}\otimes_{\mathbb{R}}\mathbb{H}
$$
is the complex Clifford algebra generated by the same $E_i$, with complex coefficients; it has complex dimension $8$ and real dimension $16$, and
$$
\mathrm{Cl}(3)\cong\mathrm{Cl}_3(\mathbb{C}).
$$

*Proof.* Complexification extends scalars only, so the relations of the generators are unchanged and the $2^3$ monomials over $\mathbb{C}$ are a basis. $\square$

**Proposition (the adjoint on the generators).** With $E_i^{\dagger}=-E_i$ and $i^{\dagger}=-i$ the map $\dagger$ is an anti-involution of $\mathrm{Cl}(3)$, and the rescaled generators $\gamma_i=iE_i$ are Hermitian, $\gamma_i^{\dagger}=\gamma_i$, with $\{\gamma_i,\gamma_j\}=+2\delta_{ij}$.

*Proof.* The adjoint of a product reverses the order, so $(E_iE_j)^{\dagger}=E_j^{\dagger}E_i^{\dagger}=(-E_j)(-E_i)=-E_iE_j$ for $i\neq j$, consistent; the rest is immediate. $\square$

## The Volume Element and the Central Splitting

**Proposition (the volume element).** The element
$$
\omega := E_1E_2E_3
$$
satisfies
$$
\omega^2=1, \qquad \omega E_i = E_i\omega \quad (i=1,2,3), \qquad \omega^{\dagger}=\omega .
$$
That is, $\omega$ is central, it is an involution, and it is self-adjoint.

*Proof.* For $i\neq j$ the generators anticommute, so $E_i\omega=\omega E_i$ for each $i$: each of the three factors crosses the other two once, at the cost of one sign, and the three signs cancel. Hence $\omega$ commutes with the generators, and therefore with the whole algebra. For the square, move the factors into adjacent pairs,
$$
\omega^2 = E_1E_2E_3E_1E_2E_3 = E_1E_2(E_3E_1)E_2E_3 = -E_1E_2E_1E_3E_2E_3 = E_1^2E_2E_3E_2E_3 = -E_2E_3E_2E_3 = E_2^2E_3^2 = +1,
$$
where $E_3E_1=-E_1E_3$, $E_2E_1=-E_1E_2$, $E_3E_2=-E_2E_3$ and $E_1^2=E_2^2=E_3^2=-1$ were used successively. This is the general formula $(-1)^{n(n-1)/2}c^n$ for the square of a product of $n$ anticommuting generators of square $c$, at $n=3$, $c=-1$. Finally, $\omega^{\dagger}=E_3^{\dagger}E_2^{\dagger}E_1^{\dagger}=(-E_3)(-E_2)(-E_1)=-E_3E_2E_1=+E_1E_2E_3=\omega$, since reversing three anticommuting factors costs one sign. Every identity was checked on the eight monomials of the algebra with zero residual. $\square$

The two properties, centrality and $\omega^2=+1$, are exactly what a **split** unit has, and they are the reason the complexified algebra behaves like the split biquaternions rather than like the biquaternions. Since $\omega=-j$ (because $E_1E_2E_3=(je_1)(je_2)(je_3)=j^3(e_1e_2)e_3=-j$), the involution $\omega$ of $\mathrm{Cl}(3)$ is the central split unit of $\mathbb{H}_{\mathbb{D}}$ up to sign.

**Theorem (the central splitting).** Define
$$
\Pi_+ := \tfrac12(1+\omega), \qquad \Pi_- := \tfrac12(1-\omega).
$$
Then
$$
\Pi_+^2=\Pi_+, \qquad \Pi_-^2=\Pi_-, \qquad \Pi_+\Pi_-=\Pi_-\Pi_+=0, \qquad \Pi_++\Pi_-=1,
$$
and both are central. Consequently
$$
\mathrm{Cl}(3) = \mathrm{Cl}(3)\Pi_+ \oplus \mathrm{Cl}(3)\Pi_-
$$
is a decomposition of $\mathrm{Cl}(3)$ into the direct sum of two proper nonzero two-sided ideals, each of complex dimension $4$, and each isomorphic to the biquaternion algebra:
$$
\mathrm{Cl}(3)\Pi_\pm \cong \mathrm{Cl}(2) \cong \mathbb{C}\mathrm{l}_2 \cong \mathbb{B} \cong M_2(\mathbb{C}).
$$

*Proof.* Orthogonality, idempotency and completeness are the algebra $\omega^2=1$: for instance $\Pi_+\Pi_-=\tfrac14(1-\omega^2)=0$ and $\Pi_+^2=\tfrac14(1+2\omega+\omega^2)=\tfrac12(1+\omega)=\Pi_+$. Centrality is centrality of $\omega$. The direct sum is the decomposition of a module by a complete family of orthogonal central idempotents. Each ideal has complex dimension $4$, since left multiplication by $\Pi_+$ is a rank-$4$ projector of the $8$-dimensional space; and a four-dimensional complex algebra that is a full matrix algebra is $M_2(\mathbb{C})$, which is $\mathbb{C}\mathrm{l}_2\cong\mathbb{B}$ by *The Clifford Structure of the Biquaternion Algebra*. The dimension of each ideal was computed to be $4$ on the eight monomials. $\square$

**Corollary (semisimple, not simple).** $\mathrm{Cl}(3)$ is semisimple and is not simple; its two-sided ideals are $0$, $\mathrm{Cl}(3)\Pi_+$, $\mathrm{Cl}(3)\Pi_-$ and $\mathrm{Cl}(3)$. Its minimal left, right and two-sided ideals coincide, and its left ideals form the diamond
$$
0 \subset \mathrm{Cl}(3)\Pi_+,\ \mathrm{Cl}(3)\Pi_- \subset \mathrm{Cl}(3).
$$

*Proof.* Because $\Pi_\pm$ are central, the left, right and two-sided ideals they generate agree; the summands are simple matrix algebras and have no proper nonzero ideal, so no further ideals occur. The lattice is then the diamond, as in *Split-Biquaternion Ideals and Peirce Decomposition*.

**Theorem (the two summands are the two halves).** The idempotents $\Pi_\pm$ of $\mathrm{Cl}(3)$ coincide with the split biquaternion idempotents $\tilde\Pi_\mp=\tfrac12(1\mp j)$ of $\mathbb{H}_{\mathbb{D}}$ promoted to the complexification, and the central splitting is the complexification of the splitting of the split biquaternion algebra:
$$
\mathrm{Cl}(3) = \mathbb{C}\otimes_{\mathbb{R}}\bigl(\mathbb{H}\tilde\Pi_+\bigr) \oplus \mathbb{C}\otimes_{\mathbb{R}}\bigl(\mathbb{H}\tilde\Pi_-\bigr) \cong \mathbb{B}\oplus\mathbb{B}.
$$

*Proof.* With $\omega=-j$ one has $\Pi_+=\tfrac12(1-j)=\tilde\Pi_-$ and $\Pi_-=\tfrac12(1+j)=\tilde\Pi_+$. The two-sided ideals $\mathbb{H}\tilde\Pi_\pm\cong\mathbb{H}$ of *Split-Biquaternion Ideals and Peirce Decomposition* complexify to $\mathbb{B}\cong\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$. $\square$

**Theorem (the parity automorphism).** The map
$$
\sigma : \mathrm{Cl}(3)\to\mathrm{Cl}(3), \qquad \sigma(E_i)=-E_i,
$$
is an algebra automorphism; it fixes the even monomials and negates the odd ones; it satisfies $\sigma(\omega)=-\omega$, and it therefore interchanges the two summands,
$$
\sigma(\Pi_+)=\Pi_-, \qquad \sigma(\Pi_-)=\Pi_+ .
$$
The two summands are the two **pinor representations** of $\mathrm{Cl}(3)$: the two simple modules of $M_2(\mathbb{C})\oplus M_2(\mathbb{C})$, inequivalent and distinguished by the eigenvalue $\pm1$ of the central volume element $\omega$.

*Proof.* Sending every generator to its negative preserves the quadratic relations $E_i^2=-1$, $E_iE_j=-E_jE_i$, and is invertible, so it is an automorphism; it is the grading automorphism of the Clifford algebra, equal to $+1$ on the even subalgebra and $-1$ on the odd part. On the volume element the three sign flips give $\sigma(\omega)=(-1)^3\omega=-\omega$, and the action on $\Pi_\pm$ follows. A central element of a product of two simple algebras acts as a scalar on each simple module; the idempotents $\Pi_\pm$ are the two projections and their distinct images are the two non-isomorphic simple modules. $\square$

## The Ladder Structure and the Minimal Left Ideal

The splitting above is the statement that $\mathrm{Cl}(3)$ carries two copies of the biquaternion algebra. Inside one copy the biquaternion machinery of the corpus applies unchanged, and it is collected here in the form used in the companion physics article.

**Definition.** Fix the $\mathrm{Cl}(2)$ subalgebra generated by $E_1,E_2$ and set
$$
\alpha := \tfrac12\bigl(E_1+iE_2\bigr), \qquad \alpha^{\dagger}=\tfrac12\bigl(-E_1+iE_2\bigr).
$$
Let $N := \alpha^{\dagger}\alpha$ be the **number operator** and $P := \alpha\alpha^{\dagger}$.

**Proposition (the isotropic element and its conjugate).** The element $\alpha$ is isotropic, $\alpha^2=0$, and the pair satisfies
$$
\{\alpha,\alpha^{\dagger}\} = 1, \qquad \alpha\alpha^{\dagger}+\alpha^{\dagger}\alpha = 1 .
$$
Hence $\operatorname{span}_{\mathbb{C}}\{\alpha\}$ is a maximal totally isotropic subspace of the complex two-space $\operatorname{span}\{E_1,E_2\}$, and $\operatorname{span}\{\alpha^{\dagger}\}$ is its conjugate.

*Proof.* Expansion in the Clifford relations: $\alpha^2=\tfrac14(E_1^2+i(E_1E_2+E_2E_1)+i^2E_2^2)=\tfrac14(-1+0+1)=0$, and likewise for the mixed anticommutator, which equals $\tfrac14(E_1^2+E_2^2)$ with the cross terms cancelling. Both were computed with zero residual. $\square$

**Proposition (the complementary projectors).** The elements
$$
P = \alpha\alpha^{\dagger} = \tfrac12\bigl(1+iE_1E_2\bigr), \qquad
N = \alpha^{\dagger}\alpha = \tfrac12\bigl(1-iE_1E_2\bigr)
$$
are Hermitian idempotents, $P^2=P$, $N^2=N$, $P^{\dagger}=P$, $N^{\dagger}=N$, and they are complementary, $P+N=1$. The element $iE_1E_2$ is a self-adjoint involution, $(iE_1E_2)^2=1$.

*Proof.* From $(E_1E_2)^2=-1$ and $(E_1E_2)^{\dagger}=E_2^{\dagger}E_1^{\dagger}=(+E_1E_2)=-E_1E_2$; hence $iE_1E_2$ is Hermitian with square $+1$, and the two elements $\tfrac12(1\pm iE_1E_2)$ are the projectors onto its $\pm1$ eigenspaces. Idempotency was checked with zero residual. $\square$

**Theorem (the minimal left ideal and its charges).** The left ideal
$$
S := \mathrm{Cl}(3)\,P
$$
is minimal, of complex dimension two, with basis
$$
S = \operatorname{span}_{\mathbb{C}}\bigl\{\,P,\ \alpha^{\dagger}P\,\bigr\},
$$
and on it the number operator $N$ acts diagonally:
$$
N\,P = 0, \qquad N\,\alpha^{\dagger}P = \alpha^{\dagger}P .
$$
The **charge operator** $Q := N$ therefore takes the two values $0$ and $1$ on $S$, with the ground state $P$ of charge $0$ and the excited state $\alpha^{\dagger}P$ of charge $1$.

*Proof.* The idempotent $P$ is primitive (its rank as an endomorphism of the two-space is one), so $S$ is minimal; the two elements are independent; and the actions follow from $\alpha P=0$ (as $\alpha^2=0$) and $\alpha^{\dagger}\alpha\alpha^{\dagger}=\alpha^{\dagger}(1-\alpha\alpha^{\dagger})=\alpha^{\dagger}$. The two vacuum and excited eigenvalues were computed on $S$ and are exactly $0$ and $1$. $\square$

The conjugate ideal is obtained from the conjugated idempotent $P^{*}=\tfrac12(1-iE_1E_2)=N$; conversely the ideal $\mathrm{Cl}(3)N$ has basis $\{N,\alpha N\}$ with charges $1$ and $0$. The construction is the two-dimensional case of the general theorem of *Maximal Totally Isotropic Subspaces and Their Unitary Symmetries*, whose unitary symmetry on a one-dimensional isotropic subspace is the abelian $\mathrm{u}(1)$ generated by the number operator: in $\mathrm{Cl}(3)$ the intrinsic symmetry of one copy is therefore $\mathrm{u}(1)$ alone, to be contrasted with the $\mathrm{su}(3)\oplus\mathrm{u}(1)$ of the six-dimensional case of *Complex Octonions and the Clifford Algebra Cl(6)*. The particle content attached to $S$ — a neutrino of charge $0$ and a charged lepton of charge $1$, with their conjugates on the conjugate ideal, and the doubling of the whole set into the two chiralities — is the reading of the companion physics article, not an algebraic statement of this one.

## The Right Action and the Enveloping Algebra

The two-sided structure of the biquaternion algebra is *The Enveloping Algebra of the Biquaternion Algebra and the Bi-Module Structure*: the left multiplications $L_a:\tilde Q\mapsto a\tilde Q$ and the right multiplications $R_b:\tilde Q\mapsto \tilde Q b$ commute, and together they generate the enveloping algebra
$$
\mathbb{B}^{\mathrm{e}}=\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{op}}\cong\operatorname{End}_{\mathbb{C}}(\mathbb{B})\cong M_4(\mathbb{C}).
$$
A complex Clifford algebra of even dimension is a full matrix algebra, $\mathrm{Cl}(2n)_{\mathbb{C}}\cong M_{2^n}(\mathbb{C})$, so the sixteen-dimensional enveloping algebra is the complex Clifford algebra of four generators,
$$
\mathbb{B}^{\mathrm{e}}\cong M_4(\mathbb{C})\cong\mathrm{Cl}(4)_{\mathbb{C}}\cong\mathbb{C}\otimes_{\mathbb{R}}\mathrm{Cl}(1,3),
$$
the complexification of the Dirac algebra. The one-rung-higher statement, in which the left action is enlarged from the biquaternion algebra to the whole of $\mathrm{Cl}(3)$, is the content of the theorem below.

**Theorem (the right action of $\mathbb{B}$ on $\mathrm{Cl}(3)$).** Let $\mathbb{B}\subset\mathrm{Cl}(3)$ be the biquaternion subalgebra spanned by $1,e_1,e_2,e_3$, and let $L_a$ and $R_b$ be left multiplication by $a\in\mathrm{Cl}(3)$ and right multiplication by $b\in\mathbb{B}$ on the eight-dimensional space $\mathrm{Cl}(3)$. Then
$$
(L_aR_b)(L_{a'}R_{b'})=L_{aa'}R_{b'b},
$$
so that the span of the products is closed under multiplication, and this algebra is
$$
\mathrm{Cl}(3)\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{op}}\cong\bigl(M_2(\mathbb{C})\oplus M_2(\mathbb{C})\bigr)\otimes_{\mathbb{C}}M_2(\mathbb{C})\cong M_4(\mathbb{C})\oplus M_4(\mathbb{C})\cong\mathrm{Cl}(5)_{\mathbb{C}}\cong\mathrm{Cl}(6)^+,
$$
of complex dimension $32$ and with a two-dimensional centre.

*Proof.* The left and right multiplications commute by associativity of $\mathrm{Cl}(3)$, so $(L_aR_b)(L_{a'}R_{b'})=(L_aL_{a'})(R_bR_{b'})$; the reversal in the second factor, $R_bR_{b'}=R_{b'b}$, is the opposite-algebra multiplication of *The Enveloping Algebra of the Biquaternion Algebra and the Bi-Module Structure*. Hence the span of the $L_aR_b$ is a subalgebra, and it is the image of the algebra homomorphism $\mathrm{Cl}(3)\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{op}}\to\operatorname{End}_{\mathbb{C}}(\mathrm{Cl}(3))$, $a\otimes b^{\mathrm{op}}\mapsto L_aR_b$. The domain is $\mathrm{Cl}(3)\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{op}}\cong(M_2(\mathbb{C})\oplus M_2(\mathbb{C}))\otimes_{\mathbb{C}}M_2(\mathbb{C})\cong M_4(\mathbb{C})\oplus M_4(\mathbb{C})$, of complex dimension $8\cdot4=32$; the image was recomputed to be $32$-dimensional, so the map is injective and the image is the whole domain. The identifications $M_4(\mathbb{C})\cong\mathrm{Cl}(4)_{\mathbb{C}}$, $M_4(\mathbb{C})\oplus M_4(\mathbb{C})\cong\mathrm{Cl}(5)_{\mathbb{C}}$ and $\mathrm{Cl}(5)_{\mathbb{C}}\cong\mathrm{Cl}(6)^+$ are the low-dimensional classification of complex Clifford algebras. The closure identity, the dimension $32$ (thirty-two independent products) and the two-dimensional centre were all recomputed on the eight monomials with zero residual, and the opposite-algebra sign $R_{e_1}R_{e_2}=-R_{e_3}$ was recomputed as well. $\square$

The theorem shows that the two-sided structure of the algebra has two rungs. On the biquaternion algebra alone the left and the right actions generate $\mathbb{B}^{\mathrm{e}}\cong\mathrm{Cl}(4)_{\mathbb{C}}$, of dimension $16$; enlarging the left action from $\mathbb{B}$ to $\mathrm{Cl}(3)$ and keeping the right action of $\mathbb{B}$ raises the generated algebra to $\mathrm{Cl}(3)\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{op}}\cong\mathrm{Cl}(5)_{\mathbb{C}}$, of dimension $32$. The right action of $\mathbb{B}$ alone is four-dimensional and is the Clifford algebra $\mathrm{Cl}(2)$; it is the pair of actions together that produces the next complex Clifford algebra. Both rungs were recorded by the source of the companion physics article, which writes the first as "the right action of $\mathbb{C}\otimes\mathbb{H}$ on $\mathbb{C}\otimes\mathbb{H}$ gives $\mathrm{Cl}(4)$" and the second as "the right action of $\mathbb{C}\otimes\mathbb{H}$ on $\mathrm{Cl}(3)$ gives $\mathrm{Cl}(5)$"; the source's reading of the second — that the enlargement supplies the parity-reversal operator that $\mathrm{Cl}(3)$ does not contain, and that $\mathrm{Cl}(5)\cong\mathrm{Cl}(6)^+$ is the second of the two complex octonionic chain algebras of the division-algebra approach, one carrying $\mathrm{SO}(4)$ and one carrying $\mathrm{SU}(3)\times\mathrm{U}(1)$ — belongs to the companion physics article and is not an algebraic statement of this one.

## Summary

The complex split biquaternions are the complexification of the split biquaternion algebra,
$$
\mathrm{Cl}(3) = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}_{\mathbb{D}} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{D}\otimes_{\mathbb{R}}\mathbb{H}
\cong \mathrm{Cl}_3(\mathbb{C}),
$$
of complex dimension $8$. Its generators $E_i=je_i$ satisfy $\{E_i,E_j\}=-2\delta_{ij}$, and its volume element $\omega=E_1E_2E_3$ is central, self-adjoint and an involution, $\omega^2=1$. The centrality gives the complete family of orthogonal central idempotents $\Pi_\pm=\tfrac12(1\pm\omega)$ and the splitting
$$
\mathrm{Cl}(3) = \mathrm{Cl}(3)\Pi_+ \oplus \mathrm{Cl}(3)\Pi_- \cong \mathbb{B}\oplus\mathbb{B} \cong M_2(\mathbb{C})\oplus M_2(\mathbb{C}),
$$
into two copies of the biquaternion algebra, each of complex dimension $4$, so that $\mathrm{Cl}(3)$ is semisimple and not simple, with a four-element ideal lattice. The parity automorphism $E_i\mapsto-E_i$ negates $\omega$ and interchanges the two summands; they are the two pinor representations of $\mathrm{Cl}(3)$, inequivalent and distinguished by the eigenvalue $\pm1$ of $\omega$. Inside each summand the ladder element $\alpha=\tfrac12(E_1+iE_2)$ is isotropic, its number operator $N=\alpha^{\dagger}\alpha$ has the complementary projector $\alpha\alpha^{\dagger}$ as partner, and the minimal left ideal $\mathrm{Cl}(3)( \alpha\alpha^{\dagger})$ has basis $\{P,\alpha^{\dagger}P\}$ with charges $0$ and $1$ under $Q=N$. The whole construction is the three-dimensional case of the doubling of $\mathrm{Cl}(2n)$ to $\mathrm{Cl}(2n+1)$ by a central involution, of which the octonionic case is *Split Bioctonions and the Clifford Algebra Cl(7)*. The two-sided structure has two rungs: the left and right actions of $\mathbb{B}$ on itself generate the enveloping algebra $\mathbb{B}^{\mathrm{e}}\cong M_4(\mathbb{C})\cong\mathrm{Cl}(4)_{\mathbb{C}}$, and the left action of $\mathrm{Cl}(3)$ together with the right action of $\mathbb{B}$ generates $\mathrm{Cl}(3)\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{op}}\cong M_4(\mathbb{C})\oplus M_4(\mathbb{C})\cong\mathrm{Cl}(5)_{\mathbb{C}}\cong\mathrm{Cl}(6)^+$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}$ | Split complex algebra, unit $j$, $j^2=+1$ |
| $\mathbb{H}$ | Quaternion algebra, units $e_0=1,e_1,e_2,e_3$, $e_k^2=-1$, $e_1e_2=e_3$ |
| $\mathbb{H}_{\mathbb{D}}=\mathbb{D}\otimes_{\mathbb{R}}\mathbb{H}$ | Split biquaternion algebra, ${}\cong\mathrm{Cl}(0,3)\cong\mathbb{H}\oplus\mathbb{H}$ |
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra, ${}\cong M_2(\mathbb{C})\cong\mathbb{C}\mathrm{l}_2$ |
| $\mathrm{Cl}(3)=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}_{\mathbb{D}}$ | Complex split biquaternions, ${}\cong\mathrm{Cl}_3(\mathbb{C})$ |
| $E_1,E_2,E_3=je_1,je_2,je_3$ | Clifford generators, $E_i^2=-1$, $E_iE_j=-E_jE_i$ |
| $\gamma_i=iE_i$ | Hermitian generators, $\gamma_i^{\dagger}=\gamma_i$, $\{\gamma_i,\gamma_j\}=2\delta_{ij}$ |
| $\dagger$ | Hermitian adjoint, $E_i^{\dagger}=-E_i$, $i^{\dagger}=-i$ |
| $\omega=E_1E_2E_3=-j$ | Volume element, central, self-adjoint, $\omega^2=1$ |
| $\Pi_\pm=\tfrac12(1\pm\omega)=\tilde\Pi_\mp$ | Central idempotents, complete and orthogonal |
| $\mathrm{Cl}(3)\Pi_\pm$ | The two simple summands, each ${}\cong\mathbb{B}\cong M_2(\mathbb{C})$ |
| $\sigma:E_i\mapsto-E_i$ | Parity (grading) automorphism, interchanges the summands |
| $\alpha=\tfrac12(E_1+iE_2)$ | Isotropic (ladder) element, $\alpha^2=0$ |
| $N=\alpha^{\dagger}\alpha$, $P=\alpha\alpha^{\dagger}$ | Number operator and its complementary projector, $P+N=1$ |
| $S=\mathrm{Cl}(3)P$ | Minimal left ideal, basis $\{P,\alpha^{\dagger}P\}$ |
| $Q=N$ | Charge operator, values $0,1$ on $S$ |
| $L_a,R_b$ | Left and right multiplications, $L_a\tilde Q=a\tilde Q$, $R_b\tilde Q=\tilde Q b$ |
| $\mathrm{Cl}(3)\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{op}}$ | Generated by left $\mathrm{Cl}(3)$ and right $\mathbb{B}$, ${}\cong M_4(\mathbb{C})\oplus M_4(\mathbb{C})\cong\mathrm{Cl}(5)_{\mathbb{C}}\cong\mathrm{Cl}(6)^+$ |

## Further Reading

- V. Vaibhav and T. P. Singh, "Left-Right Symmetric Fermions and Sterile Neutrinos from Complex Split Biquaternions and Bioctonions," arXiv:2108.01858, for the construction of this article's algebra as a two-chirality fermion algebra and its physics reading.
- P. Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the classification $\mathrm{Cl}_3(\mathbb{C})\cong M_2(\mathbb{C})\oplus M_2(\mathbb{C})$, the volume element of an odd complex Clifford algebra, and the centrality that produces the splitting.
- H. B. Lawson and M.-L. Michelsohn, *Spin Geometry* (Princeton, 1989), for the volume element, the chirality grading and the two pinor representations of an odd Clifford algebra.
- J. H. Conway and D. A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the split biquaternions and their isomorphism $\mathbb{H}_{\mathbb{D}}\cong\mathbb{H}\oplus\mathbb{H}$.
- Companion article *Split-Biquaternion Algebra*, for the algebra being complexified, its conjugations and its idempotents.
- Companion article *Split-Biquaternion Ideals and Peirce Decomposition*, for the splitting $\mathbb{H}_{\mathbb{D}}\cong\mathbb{H}\oplus\mathbb{H}$ and its diamond of ideals.
- Companion article *Biquaternion Algebra* and *The Clifford Structure of the Biquaternion Algebra*, for $\mathbb{B}\cong\mathbb{C}\mathrm{l}_2$, its idempotents and its minimal left ideals.
- Companion article *Maximal Totally Isotropic Subspaces and Their Unitary Symmetries*, for the general ladder, number-operator and charge construction.
- Companion article *The Enveloping Algebra of the Biquaternion Algebra and the Bi-Module Structure*, for the left and right multiplications, their commuting, and $\mathbb{B}^{\mathrm{e}}\cong\operatorname{End}_{\mathbb{C}}(\mathbb{B})\cong M_4(\mathbb{C})$.
- Companion article *Split Bioctonions and the Clifford Algebra Cl(7)*, for the same doubling one rung higher, on the octonions.
