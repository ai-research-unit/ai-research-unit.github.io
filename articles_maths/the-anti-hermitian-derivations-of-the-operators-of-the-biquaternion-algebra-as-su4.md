# __The Anti-Hermitian Derivations of the Operators of the Biquaternion Algebra as $\mathfrak{su}(4)$__

## Introduction

**Two conditions pick out the generators: anti-Hermitian and traceless. The carrier has moved up one level. A generator is now an operator $K$ on the biquaternion algebra, the carrier of the derivation is the sixteen-dimensional space of operators $\operatorname{End}(\mathbb{B})$, and the fifteen parameters of $\mathfrak{su}(4)$ are fifteen directions in which an operator can be turned. Of the fifteen, three come from the algebra itself, the three inner derivations of the previous level, and twelve come from outside.**

The operator is $S\mapsto KS-SK$, anti-Hermitian for the Hilbert–Schmidt form on the sixteen-dimensional carrier, and its exponential is the conjugation by the rotor $U=e^{K}\in\mathrm{SU}(4)$ acting on operators. This is the same object as in the matrix article, with the same fifteen generators; what the operator frame adds is the reading of the carrier as the sixteen products of the algebra, and with it the split of the fifteen into the three that the algebra supplies and the twelve that it does not.

The article gives the three families of generators as operators, the array of the derivation in the basis of the sixteen products, the action of each family on those products, the dimension ladder with the count of the multiplier space, and the invariants of the rotor.

The article assumes the operator calculus of *The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure in $M_2(\mathbb{C})$*, the derivation identities of *Star-Derivations and the Anti-Hermitian Derivations*, and the reading of $\operatorname{End}(\mathbb{B})\cong M_4(\mathbb{C})$.

## The Two Conditions on the Generator

**Proposition (the generators).** The operators $K\in\operatorname{End}(\mathbb{B})$ with $K^{*}=-K$ and $\operatorname{tr}K=0$ form a real vector space of dimension fifteen, closed under the bracket, isomorphic to $\mathfrak{su}(4)$.

**Proof.** In the coefficient basis the operator is a $4\times4$ complex matrix, so the count is the count of the matrix case: sixteen real parameters for anti-Hermitian, one equation for the trace, fifteen left. The bracket of two anti-Hermitian operators is anti-Hermitian, and the trace of a commutator vanishes.

**Remark (why the trace is available here and not on an element).** The trace is taken in the coefficient basis of the algebra, which is a basis of four. It is a property of the operator and not of the element, which is why the operator level carries the same two conditions as the matrix level.

**Remark (the split as six and nine).** In the coefficient basis the fifteen split as six real antisymmetric and nine $i$ times real symmetric traceless. The six form $\mathfrak{so}(4)$ and close; the nine do not. The split depends on the chosen basis, and the three families below are the same three families as in the matrix article, read in the coefficient basis.

## The Three Families of Generators

**Definition.** With $E_{ij}$ the matrix units of order four in the coefficient basis of the algebra, the fifteen generators are

$$
S_{ij}=i(E_{ij}+E_{ji}),\quad A_{ij}=E_{ij}-E_{ji},\quad H_k\ \text{the three imaginary diagonal traceless},
$$

six, six and three of them.

**Proposition (three come from the algebra).** The three inner derivations of the algebra, written as operators in the coefficient basis, are exactly

$$
\mathrm{ad}_{\vec e_x}=\begin{pmatrix}0&0&0&0\\0&0&0&0\\0&0&0&-2\\0&0&2&0\end{pmatrix},\quad
\mathrm{ad}_{\vec e_y}=\begin{pmatrix}0&0&0&0\\0&0&0&2\\0&0&0&0\\0&-2&0&0\end{pmatrix},\quad
\mathrm{ad}_{\vec e_z}=\begin{pmatrix}0&0&-2&0\\0&0&0&0\\0&2&0&0\\0&0&0&0\end{pmatrix}.
$$

Each is anti-Hermitian, of trace zero, of square $-4P$ with $P$ the projection onto one coordinate plane, and the three are independent.

**Proof.** The arrays are the difference of the left and right multipliers of a unit vector, computed in the coefficient basis with the multiplication rules $\vec e_x\vec e_y=\vec e_z$ and so on. The anti-Hermitian and traceless properties are read from the entries, which are real and antisymmetric with zero diagonal.

**Remark (what the three are, among the fifteen).** In the labelling $e_t,\vec e_x,\vec e_y,\vec e_z$ the three arrays above are exactly

$$
\mathrm{ad}_{\vec e_x}=-2A_{34},\qquad \mathrm{ad}_{\vec e_y}=+2A_{24},\qquad \mathrm{ad}_{\vec e_z}=-2A_{23},
$$

with the indices $2,3,4$ standing for the three vector coefficients. So the three directions that the algebra supplies are three of the six of the $A$ family, and the other twelve are the remaining three of that family, the six of the $S$ family and the three diagonal ones. The element level has three directions; the operator level has three of each kind that the algebra supplies and twelve that it does not.

## The Derivation and Its Array

**Proposition (it is a derivation and it is anti-Hermitian).** For $S,T$ operators, $\mathrm{ad}_K(ST)=\mathrm{ad}_K(S)T+S\,\mathrm{ad}_K(T)$; and for the Hilbert–Schmidt form $\langle S,T\rangle=\operatorname{tr}(S^{*}T)$ on the operator space, $(\mathrm{ad}_K)^{*}=\mathrm{ad}_{K^{*}}$, so $\mathrm{ad}_K$ is anti-Hermitian exactly when $K$ is. The map $K\mapsto\mathrm{ad}_K$ has kernel the scalars of the operator algebra, so it is injective on the fifteen.

**Proof.** The Leibniz rule is associativity of the composition of operators. For the adjoint, $\operatorname{tr}([K,S]^{*}T)=\operatorname{tr}(S^{*}[K^{*},T])$ by the cyclic invariance. The kernel is the centre of the operator algebra, which is the scalars $\mathbb{C}\,\mathrm{id}$, and the only scalar multiple of the identity among the traceless operators is zero.

**Proposition (the array).** In the basis of the sixteen products $T_{a,b}$, the array of $\mathrm{ad}_K$ is the Kronecker difference of the array of $K$ with itself,

$$
[K,\cdot]\longleftrightarrow K\otimes\mathrm{I}_4-\mathrm{I}_4\otimes K^{\mathsf T},
$$

in the same row stacking as the matrix article.

**Proof.** The carrier is a full matrix algebra in the coefficient basis, and the derivation is the commutator, so the array is the commutator array. The sixteen products are a basis of the carrier, and the change of basis from the matrix units to the products is a similarity, which leaves the spectrum and the trace alone.

**Corollary (the spectrum).** The spectrum of the array is the multiset of the sixteen differences $\alpha_i-\alpha_j$ of the eigenvalues of the generator in the coefficient basis; the trace is zero; the exponential is unitary of determinant one.

**Proof.** As in the matrix case: the eigenvalues of a Kronecker product are the products of the eigenvalues, $-\alpha_j$ from the second factor.

**Corollary (an explicit diagonal array).** For the generator $K=i\operatorname{diag}(1,-1,0,0)$ the array is diagonal in the matrix-unit basis with the sixteen entries, in row-major order,

$$
(0,\,2i,\,i,\,i;\;\;-2i,\,0,\,-i,\,-i;\;\;-i,\,i,\,0,\,0;\;\;-i,\,i,\,0,\,0).
$$

**Proof.** The entry $S_{ij}$ of an operator $S$ is multiplied by $\alpha_i-\alpha_j$ under the derivation, so the array is diagonal on the matrix units with the differences. The same array is diagonal on the products up to the similarity of the change of basis.

## The Sixteen Products as the Carrier

**Proposition (the carrier is the enveloping algebra).** The sixteen products $T_{a,b}$ with $a,b$ running over a basis of the algebra form a basis of $\operatorname{End}(\mathbb{B})$, so the carrier of the derivation is the full operator algebra, of complex dimension sixteen.

**Proof.** $T_{a,b}(X)=aXb$ is linear in $X$ and the sixteen of them are independent and span the sixty-four-real-dimensional space of real-linear maps, of which the complex-linear ones are the thirty-two of complex dimension sixteen.

**Proposition (the multipliers span seven, not eight).** The left multipliers $L(\mathbb{B})$ form a subspace of complex dimension four, the right multipliers $R(\mathbb{B})$ another of complex dimension four, and their intersection is the scalars, of complex dimension one. The span therefore has complex dimension $4+4-1=7$.

**Proof.** $L_a=L_b$ forces $a=b$ on the identity, so the left multipliers are four-dimensional; likewise the right. $L_a=R_b$ forces $aX=Xb$ for all $X$, which on the identity gives $a=b$ and then forces $a$ to be central. So the intersection is the scalars, and the sum has dimension seven.

**Remark (the two-sided operators).** The products $T_{a,b}$ with $a,b$ both non-central are the ones that are neither left nor right multipliers, and they fill the remaining nine complex dimensions of the carrier. The count is $16=4+4-1+9$, which is the additive form of the same identity as $7+9=16$.

**Remark (why the carrier being sixteen matters).** The derivation is an operator on a sixteen-dimensional space, so its array has order sixteen and two hundred and fifty-six complex entries. The counts of the ladder all follow: two hundred and fifty-six complex dimensions of endomorphisms is five hundred and twelve real, half of them anti-Hermitian, and the derivations among them are the inner ones, of complex dimension fifteen.

## The Exponential of Each Generator

**Theorem (the exponential is the conjugation).** With $U=e^{K}$, $e^{\mathrm{ad}_K}(S)=USU^{*}$ for every operator $S$, and the array of that operator is $U\otimes\bar U$.

**Proof.** The exponential of the commutator with $K$ is the conjugation by $e^{K}$. On the array, the two factors exponentiate and commute.

**Proposition (the three families, read on the sixteen products).** Exponentiated, the three families act on the products as follows.

| family | the rotor | on the products $T_{a,b}$ | in words |
|---|---|---|---|
| $A_{ij}$ | real orthogonal, in $\mathrm{SO}(4)$ | mixes the products whose coefficient labels are $i$ or $j$, with real coefficients | turns the pair of labels, and turns the two sides in opposite senses |
| $S_{ij}$ | complex, with the factor $i$ | mixes the same products with the factor $i$ off the diagonal | turns the pair of labels in the complex sense |
| $H_k$ | diagonal | multiplies $T_{a,b}$ by the phase $\alpha_i-\alpha_j$ attached to its labels | shifts each product by the difference of two phases |

**Proof.** The rotor acts by $S\mapsto USU^{*}$, which is the left factor on the first label and the right factor on the second. For the diagonal rotor the two factors are phases and the product is the difference. For the other two families the same statement is read block by block.

**Corollary (the fixed operators).** The fixed points of the exponential are the operators commuting with $K$, of complex dimension $\sum_l m_l^{2}$ for the multiplicities $m_l$ of the eigenvalues of $K$: four in the generic case, which is the span of $\mathrm{I},K,K^{2},K^{3}$, and sixteen for the zero generator. The scalars are always fixed.

**Proof.** $USU^{*}=S$ exactly when $S$ commutes with $U$, which is the commutant.

**Remark (what each family does to the algebra inside the carrier).** The copy of the algebra, spanned by the four products $T_{a,e_t}$, is moved by the rotor unless the rotor preserves it. Only rotors coming from the algebra itself, the three directions of the previous level, preserve the copy; the twelve outside directions move it into the rest of the carrier. So the operator frame shows a fact with no matrix counterpart: the algebra sits inside its operator algebra, and almost every rotation of the carrier tilts it.

## The Dimension Ladder

| set | defining condition | real dimension |
|---|---|---|
| $\mathbb{B}$ | none | $8$ |
| $\operatorname{End}(\mathbb{B})$, the carrier | none | $32$ |
| the anti-Hermitian operators | $K^{*}=-K$ | $16$ |
| the traceless operators | $\operatorname{tr}K=0$ | $30$ |
| $\mathfrak{su}(4)$ of generators | both | $15$ |
| the three from the algebra | inner derivations | $3$ |
| the twelve from outside | the complement | $12$ |
| the multipliers $L$ and $R$ | one side only | $14$ |
| $\operatorname{End}(\operatorname{End}(\mathbb{B}))$ | none | $512$ |
| the anti-Hermitian endomorphisms | $F^{*}=-F$ | $256$ |
| the derivations | Leibniz rule | $30$ |
| the anti-Hermitian derivations | both | $15$ |

**Remark (the number seven).** The span of the left and right multipliers has complex dimension seven, so fourteen real. It is a proper subspace of the carrier, and it is the part of the carrier that is generated by the algebra acting on itself from one side or the other. The two-sided operators that are neither are the remaining nine complex dimensions.

**Remark (three inside fifteen, and the split of the twelve).** The three inner derivations sit inside the fifteen and the map $D\mapsto\mathrm{ad}_D$ carries the six derivations of the algebra into the thirty of the carrier, of which three are anti-Hermitian. The complement of the three inside the fifteen has dimension twelve, and there is no canonical way to split it: a choice of basis of the carrier gives one, and a different basis gives another.

## The Invariants

**Proposition (what the rotor preserves).** The conjugation by $U$ preserves the trace, the determinant, the spectrum, the rank and the characteristic polynomial of every operator, and it preserves the Hermitian cone, the unitary group and the singular values.

**Proof.** The conjugation is an algebra automorphism, so every polynomial invariant is preserved; it carries $S^{*}$ to $(USU^{*})^{*}$, so the cone is preserved; similar matrices have the same eigenvalues, and the singular values are the eigenvalues of $S^{*}S$, which is carried to $U(S^{*}S)U^{*}$.

**Corollary (the period and the kernel).** The operator has period $\pi$ in the parameter for a unit generator, $e^{\pi\mathrm{ad}_K}=\mathrm{id}$; and the map $U\mapsto\mathrm{Ad}_U$ has kernel the fourth roots of unity, with image $\mathrm{PSU}(4)$, of real dimension fifteen.

**Proof.** At $\theta=\pi$ the rotor is $-U_0$ with $U_0$ the rotor at $\theta=0$; a sign commutes with everything, so the conjugation is the identity. The kernel of the conjugation map on $\mathrm{SU}(4)$ is its centre, which is $\mathbb{Z}_4$, and $15-0=15$ for the dimension of the image.

**Remark (the determinant is free).** $\operatorname{tr}\mathrm{ad}_K=0$ for every generator, so $\det e^{\mathrm{ad}_K}=1$ with no hypothesis. This is the statement that the derivation condition alone carries the determinant, and it is why the operator level needs only the anti-Hermitian condition added to it.

## The Worked Example

**Proposition (two double eigenvalues).** For $K=i\operatorname{diag}(1,1,-1,-1)$ the spectrum of the array is $0$ eight times and $\pm2i$ four times each, the commutant of $K$ in the carrier is eight complex dimensional, and at $\theta=\pi/2$ the rotor fixes the commutant and negates the rest.

**Proof.** The differences of $i,i,-i,-i$ give the stated spectrum: eight zeros for the pairs of equal eigenvalue, four $2i$ and four $-2i$. The commutant of a matrix with two eigenvalues of multiplicity two is the block diagonal subalgebra, of complex dimension $4+4=8$. The rotor at $\theta=\pi/2$ is $\operatorname{diag}(i,i,-i,-i)$, whose conjugation multiplies the entry $S_{ij}$ by $e^{i\theta(\epsilon_i-\epsilon_j)}$ with $\epsilon=(1,1,-1,-1)$, which is $-1$ across the blocks and $1$ inside.

**Remark (the five patterns).** The commutant of the generator is the fixed space of the rotor, and its complex dimension is $\sum_l m_l^{2}$ over the multiplicities: $4$ for $1+1+1+1$, $6$ for $2+1+1$, $8$ for $2+2$, $10$ for $3+1$ and $16$ for the zero generator. The generic generator therefore fixes four complex dimensions, the polynomials in the generator, and not only the scalars; the example fixes eight, the largest value for a generator with two distinct eigenvalues.

## The Two Frames

| statement | operator frame, this article | matrix frame |
|---|---|---|
| carrier | the sixteen products $T_{a,b}$ | the sixteen matrix units |
| the fifteen | three from the algebra, twelve outside | the fifteen matrices of three families |
| the array | sixteen by sixteen, a Kronecker difference | the same |
| what the frame adds | the algebra sits inside the carrier and the rotor tilts it | the fifteen matrices can be written out |

**Remark (the same operator in two bases).** The change of basis between the two carriers is the isomorphism $\operatorname{End}(\mathbb{B})\cong M_4(\mathbb{C})$, and it carries the products to the units. The spectrum, the trace and the determinant of the array are the same in both frames, and the three counts $6,6,3$ are the same, because they are properties of the operator and not of the basis.

## Summary

The anti-Hermitian traceless operators of the carrier $\operatorname{End}(\mathbb{B})$ form $\mathfrak{su}(4)$, of real dimension fifteen, and split as three inner derivations of the algebra and twelve directions from outside. Each generator gives the derivation $S\mapsto KS-SK$, anti-Hermitian for the Hilbert–Schmidt form, of array $K\otimes\mathrm{I}_4-\mathrm{I}_4\otimes K^{\mathsf T}$ and of spectrum the differences of the eigenvalues of the generator.

The exponential is the conjugation by the rotor $U=e^{K}$, which preserves every similarity invariant, splits the carrier into the scalars and the rest, and acts on the products by the left factor on one label and the right factor on the other. The three families act by a real rotation, by a mixing with $i$, and by a pair of opposite phases.

The numbers are these. The algebra has real dimension $8$ and its carrier has real dimension $32$; the anti-Hermitian operators of the carrier have $16$, the traceless ones $30$, and the two conditions together leave $15$, which is $\mathfrak{su}(4)$. The endomorphisms of the carrier have real dimension $512$, the anti-Hermitian ones $256$, the derivations $30$, and the anti-Hermitian derivations $15$.

The multipliers span seven complex dimensions, so $14$ real, of the carrier's $16$ complex dimensions, and the algebra sits inside its carrier as a copy that every rotor coming from the twelve outside directions tilts.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $T_{a,b}$ | the product operator $X\mapsto aXb$ |
| $L_a$, $R_b$ | left and right multiplication by an element |
| $K$ | the generator, an anti-Hermitian traceless operator |
| $\alpha_k$ | the eigenvalues of the generator in the coefficient basis |
| $\mathrm{ad}_K$ | the derivation $S\mapsto KS-SK$ |
| $\langle S,T\rangle$ | the Hilbert–Schmidt form $\operatorname{tr}(S^{*}T)$ |
| $U$ | the rotor $e^{K}\in\mathrm{SU}(4)$ |
| $\mathrm{Ad}_U$ | the conjugation $S\mapsto USU^{*}$ |
| $S_{ij}$, $A_{ij}$, $H_k$ | the three families of generators |
| $\mathrm{PSU}(4)$ | the image of the rotor map |

## Further Reading

- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations* (Springer, 2015), for derivations, inner automorphisms and $\mathfrak{su}(n)$.
- Roger A. Horn and Charles R. Johnson, *Topics in Matrix Analysis* (Cambridge University Press, 1991), for the Kronecker product and the commutator equation.
- [The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure in $M_2(\mathbb{C})$](the-enveloping-operator-algebra-of-the-biquaternion-algebra-and-the-bi-module-structure-in-m2c.html), for the sixteen products as a basis.
- [The Anti-Hermitian Derivations of the Biquaternion Algebra as $\mathfrak{su}(2)$](the-anti-hermitian-derivations-of-the-biquaternion-algebra-as-su2.html), for the level below, with three generators.
- [The Anti-Hermitian Derivations of $M_4(\mathbb{C})$ as $\mathfrak{su}(4)$](the-anti-hermitian-derivations-of-m4c-as-su4.html), for the same fifteen in the matrix frame, written out in full.
- [Star-Derivations and the Anti-Hermitian Derivations](star-derivations-and-the-anti-hermitian-derivations.html), for the derivation identities.
- [The Adjoint Action, the Orbits and the Flag Variety of $M_4(\mathbb{C})$](the-adjoint-action-the-orbits-and-the-flag-variety-of-m4c.html), for the orbit structure of the conjugation on the carrier.
