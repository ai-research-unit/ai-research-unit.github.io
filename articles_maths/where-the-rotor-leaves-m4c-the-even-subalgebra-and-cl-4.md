# __Where the Rotor Leaves $M_4(\mathbb{C})$: the Even Subalgebra and $Cl(4)$__

## Introduction

**A rotor is an even product of vectors, so it lies in the even Clifford algebra $\mathrm{Cl}^{+}(4,\mathbb{C})\cong M_2(\mathbb{C})\oplus M_2(\mathbb{C})\cong\mathbb{B}\oplus\mathbb{B}$ of complex dimension $8$, which is semisimple with two simple ideals and a two-dimensional centre; it is a subalgebra of the simple $M_4(\mathbb{C})$, the commutant of the chirality, but never an ideal, and the two one-sided biquaternion images inside it span only seven dimensions.**

The article proves that the rotor is even, identifies the even Clifford algebra and its two ideals, places the even part inside the matrix algebra as a subalgebra and shows that it is not an ideal, computes the dimension of the span of the two one-sided images, identifies the rotors with the norm-one part of the even Clifford group, and compares the picture with the gamma frame, where the five frame operators generate the whole algebra and the rotors are the even words among the sixteen graded products.

It assumes *The Rotor as a Square Root of a Rotation: the Two Signs and the Double Cover at $n=4$*, *The Clifford Group and the Frame Stabiliser* and *The Gamma Frame and the Complexified Dirac Algebra of $M_4(\mathbb{C})$*. The versor theory is *Biquaternion Versors and the Orthogonal Group*.

## The Rotor Is Even

**Definition.** A **rotor** is a product $\rho=v_1v_2\cdots v_{2m}$ of an even number of vectors of the four-dimensional space, and a **vector** is an element of the image of $V$ in $\mathrm{Cl}(4,\mathbb{C})$.

**Proposition.** $\rho$ is a sum of even-grade elements, and $-\rho$ is the rotor with all the vectors negated.

**Proof.** A product of an even number of vectors is a sum of products of an even number of them, which is the definition of the even part; and $(-v_1)(-v_2)=v_1v_2$, so an even number of sign changes cancels.

**Corollary.** The rotors lie in $\mathrm{Cl}^{+}(4,\mathbb{C})$, and the odd products $v_1\cdots v_{2m+1}$ lie in the odd part, which is $\rho V$.

**Proof.** The parity of the number of factors, and the fact that multiplying by one more vector switches parity.

**Corollary.** A rotor acts on vectors by $\Phi_\rho(x)=\rho x\rho^{-1}$, and the action preserves the parity of the words it produces.

**Proof.** $\rho x\rho^{-1}$ is the product of an even, an odd and an even number of vectors, hence odd, hence a vector again when $\rho$ is invertible.

## The Even Clifford Algebra

**Theorem.** $\mathrm{Cl}(4,\mathbb{C})\cong M_4(\mathbb{C})$ and $\mathrm{Cl}^{+}(4,\mathbb{C})\cong\mathrm{Cl}(3,\mathbb{C})\cong M_2(\mathbb{C})\oplus M_2(\mathbb{C})$, of complex dimensions $16$ and $8$.

**Proof.** The complex Clifford algebra of an even-dimensional space with nondegenerate form is the full matrix algebra; the even part of $\mathrm{Cl}(n,\mathbb{C})$ is $\mathrm{Cl}(n-1,\mathbb{C})$, and $\mathrm{Cl}(3,\mathbb{C})$ is the sum of two copies of $M_2$, since the real $\mathrm{Cl}(3)$ is the sum of two copies of the quaternions.

**Corollary.** The even part is semisimple with exactly two simple ideals, each of complex dimension $4$, and its centre is two-dimensional.

**Proof.** A direct sum of two matrix algebras has two simple ideals and a centre spanned by the two identities.

**Corollary.** The even part is not simple, and it has exactly four two-sided ideals: zero, the two summands and the whole.

**Proof.** The ideals of a direct sum of simples are the sums of ideals of the summands.

**The biquaternion form.** $\mathrm{Cl}^{+}(4,\mathbb{C})\cong\mathbb{B}\oplus\mathbb{B}$, each summand a copy of the biquaternion algebra of complex dimension $4$.

**Proof.** $M_2(\mathbb{C})\cong\mathbb{B}$.

## The Even Part inside the Matrix Algebra

**Theorem.** $\mathrm{Cl}^{+}(4,\mathbb{C})$ sits inside $M_4(\mathbb{C})$ as the commutant of the chirality: if $\omega$ is the product of the four frame operators, with $\omega^{2}=\mathrm I_4$, then a matrix is even exactly when it commutes with $\omega$.

**Proof.** The odd elements anticommute with $\omega$ and the even ones commute with it; $\omega$ has two eigenvalues, each of multiplicity two, so its commutant has dimension $2^{2}+2^{2}=8$, which is the dimension of the even part.

**Corollary.** In a basis where $\omega=\operatorname{diag}(1,1,-1,-1)$ the even part is the block-diagonal subalgebra $M_2\oplus M_2$, and the odd part is the two off-diagonal blocks.

**Proof.** A matrix commuting with a diagonal matrix with two eigenvalues is block diagonal with respect to the two eigenspaces.

**Corollary.** The even part is a subalgebra of $M_4(\mathbb{C})$ and not an ideal: $M_4$ is simple and has no proper two-sided ideal.

**Proof.** $M_4$ is central simple, so its only ideals are zero and itself, and the even part is neither.

**The correction.** A semisimple algebra can perfectly well be a subalgebra of a matrix algebra — the block-diagonal $M_2\oplus M_2$ is one — so the even part does sit inside $M_4$. What fails is not the inclusion but the ideal property and the equality with the whole algebra: the even part has dimension $8$ and the algebra has dimension $16$, and the odd part is its complement as a vector space and not as an ideal.

**Proof.** The two statements above and the dimension count.

## The Two One-Sided Images and the Mixed Products

**Proposition.** The two copies of $\mathbb{B}$ in the Kronecker reading are the left image $M_2\otimes\mathrm I$ and the right image $\mathrm I\otimes M_2$; each has dimension $4$, they meet in the scalars, and their sum has dimension $7$.

**Proof.** $\dim(B_L+B_R)=\dim B_L+\dim B_R-\dim(B_L\cap B_R)=4+4-1$; the intersection is the scalars because $L(a)=R(b)$ forces $a=b=\lambda e_t$.

**Corollary.** The two one-sided families do not span the even part: they supply seven of its eight dimensions, and one more direction is needed.

**Proof.** The even part has dimension $8$ and the sum of the images has dimension $7$.

**Proposition.** The linear map $(a,b)\mapsto L_a+R_b$ from $\mathbb{B}\oplus\mathbb{B}$ to $M_4$ has kernel the pairs $(\lambda,-\lambda)$ and is not multiplicative: the product of two images picks up the two-sided terms $L_aR_d+R_bL_c$.

**Proof.** Compute $(L_a+R_b)(L_c+R_d)=L_{ac}+L_aR_d+R_bL_c+R_{bd}$, and the two middle terms vanish only when one of $a,b,c,d$ is a scalar.

**Corollary.** The rotors act two-sidedly precisely because the two-sided products are the mixed terms: a rotor with $a$ and $b$ both non-scalar produces a two-sided operator, which is not the sum of a left and a right action.

**Proof.** The product of two two-sided rotations is a two-sided rotation with both factors non-scalar, and the expansion above exhibits the mixing.

**The rank-one operators.** The mixed terms $L_aR_b$ are the two-sided operators of the earlier articles, and their matrices are the sixteen $T_{\mu\nu}$ on the units.

**Proof.** The definition $T_{a,b}(X)=aXb$ and the product rule $T_{a,b}T_{c,d}=T_{ac,db}$.

## The Rotors and the Spin Group

**Theorem.** The group of invertible even elements is $\mathbb{C}^{\times}\cdot\mathrm{Spin}(4,\mathbb{C})$, and $\mathrm{Spin}(4,\mathbb{C})\cong SL_2(\mathbb{C})\times SL_2(\mathbb{C})$, of complex dimension $6$.

**Proof.** The even Clifford group is the scalars times the spin group; the spin group is the product of the norm-one parts of the two copies of $\mathbb{B}^{\times}$, that is $SL_2\times SL_2$.

**Corollary.** Each simple ideal of the even part contributes one factor, so the two ideals of $\mathrm{Cl}^{+}$ are the two factors of the spin group.

**Proof.** The unit group of a direct sum of two matrix algebras is the product of the two general linear groups.

**Corollary.** The rotor group double covers $SO(4,\mathbb{C})$ with kernel $\{\pm1\}$, and the kernel is the simultaneous sign in the two factors.

**Proof.** The covering of the earlier article and the identification of the factors.

**The real case.** Over $\mathbb{R}$ with the definite form the same computation gives $\mathrm{Cl}^{+}(4)\cong\mathbb{H}\oplus\mathbb{H}$ and $\mathrm{Spin}(4)\cong SU(2)\times SU(2)$, and the rotors of the previous article are exactly the norm-one even elements.

**Proof.** The real form of the classification and the identifications of the two factors with the unit quaternions.

## The Comparison with the Gamma Frame

**Proposition.** In the gamma frame the five operators generate the whole of $M_4(\mathbb{C})$, and their sixteen antisymmetrised products are a basis; the even words among them span the eight-dimensional even part.

**Proof.** The generation is the statement of the frame article; the graded products are distributed as $1+4+6+4+1$ over the five grades, and the even grades contribute $1+6+1=8$.

**Corollary.** The rotors are the even words of the frame, the odd words carry the spinor maps, and the frame itself uses the whole algebra and not one factor.

**Proof.** Parity of the words and the dimension count of the grades.

**The bivector generators.** The six bivectors of the frame span $\Lambda^{2}\mathbb{C}^{4}\cong\mathfrak{so}(4,\mathbb{C})$, and the rotor is the exponential of a bivector.

**Proof.** The bivectors are the half-commutators of the frame operators, and their span is the Lie algebra of the spin group.

**Corollary.** The rotor does not leave $M_4(\mathbb{C})$: it leaves the odd part, the one-sided factor and the commutant of the chirality, and it stays in the even part, which is a subalgebra of dimension eight.

**Proof.** The three exclusions and the inclusion of the theorem above.

**The precise sense of the title.** "Where the rotor leaves $M_4$" means: the rotor is not in the odd part, is not in a single one-sided family, and is not an ideal-generating element; it is an even element of the matrix algebra, and the even algebra it generates is semisimple with two ideals, in contrast with the simple ambient algebra.

**Proof.** The three statements of the preceding corollary.

## Summary

A rotor is an even product of vectors, so it lies in the even Clifford algebra, of complex dimension eight. That algebra is $\mathrm{Cl}(3,\mathbb{C})\cong M_2\oplus M_2\cong\mathbb{B}\oplus\mathbb{B}$, semisimple with two simple ideals of dimension four and a two-dimensional centre.

Inside $M_4(\mathbb{C})$ the even part is the commutant of the chirality, hence block diagonal of type $M_2\oplus M_2$; it is a subalgebra and not an ideal, since the ambient algebra is simple. The two one-sided biquaternion images are the two simple ideals in the Kronecker reading; they are four-dimensional each, meet in the scalars and span only seven dimensions, so the two-sided products are exactly what the eighth direction and the rotor action require.

The invertible even elements are the scalars times $\mathrm{Spin}(4,\mathbb{C})\cong SL_2\times SL_2$, and over the reals the spin group is $SU(2)\times SU(2)$. In the gamma frame the rotors are the even words among the sixteen graded products, and the odd words carry the spinor maps.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{Cl}^{+}(4,\mathbb{C})$ | the even Clifford algebra, dimension $8$ |
| $M_2\oplus M_2$ | its two simple ideals |
| $\omega$ | the chirality, with $\omega^{2}=\mathrm I_4$ |
| $B_L$, $B_R$ | the two one-sided images, of dimension $4$ each |
| $\mathbb{C}^{\times}\cdot\mathrm{Spin}(4,\mathbb{C})$ | the group of invertible even elements |
| $1+4+6+4+1$ | the graded count of the frame basis |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the even part and the rotor group.
- [The Clifford Group and the Frame Stabiliser](the-clifford-group-and-the-frame-stabiliser.html), for the even Clifford group and its two biquaternion factors.
- [The Gamma Frame and the Complexified Dirac Algebra of $M_4(\mathbb{C})$](the-gamma-frame-and-the-complexified-dirac-algebra-of-m4c.html), for the five frame operators and the graded basis.
- [The Rotor as a Square Root of a Rotation: the Two Signs and the Double Cover at $n=4$](the-rotor-as-a-square-root-of-a-rotation-the-two-signs-and-the-double-cover-at-n-4.html), for the rotors and the covering.
- [Biquaternion Versors and the Orthogonal Group](biquaternion-versors-and-the-orthogonal-group.html), for the versor map in the biquaternion algebra.
