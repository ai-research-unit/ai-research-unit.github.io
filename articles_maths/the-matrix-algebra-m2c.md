# __The Matrix Algebra $M_2(\mathbb{C})$__

## Introduction

**The algebra $M_2(\mathbb{C})$ is the algebra of $2\times2$ complex matrices, and everything in it is decided by four matrix units and one product rule.**

This article fixes the algebra that the whole category reads: the matrix units and the rule $E_{ij}E_{kl}=\delta_{jk}E_{il}$, the trace, the determinant and the rank, the centre and the simplicity, the real dimension $8$, the unit group and the projective group, and the identification with the biquaternion algebra $\mathbb{B}$. It assumes only the linear algebra of $\mathbb{C}^{2}$. It defers the element to *The Element: Rank, Trace, Determinant, Characteristic Polynomial at $n=2$*, the real matrices to *The Two Base Fields: $M_2(\mathbb{R})$ inside $M_2(\mathbb{C})$*, and the ideal theory to *The Ideals, the Centre and the Simplicity of $M_2(\mathbb{C})$*.

No quadratic form is used in the proofs. The trace pairing is recorded as symmetric and nondegenerate, nothing more; its signature is *The Trace Form and Its Signature on the Two Halves of $M_2(\mathbb{R})$*.

## The Algebra

**Definition.** $M_2(\mathbb{C})$ is the set of $2\times2$ arrays of complex numbers with the entrywise sum and the product $(AB)_{ij}=\sum_{k}a_{ik}b_{kj}$. The **matrix units** $E_{ij}$ have a $1$ in position $(i,j)$ and $0$ elsewhere.

**Proposition (the product rule).** The four units are a $\mathbb{C}$-basis, and

$$
\boxed{\;E_{ij}E_{kl}=\delta_{jk}E_{il}.\;}
$$

**Proof.** The $(p,q)$-entry of $E_{ij}E_{kl}$ is $\sum_{r}\delta_{ip}\delta_{jr}\delta_{kr}\delta_{lq}=\delta_{jk}\delta_{ip}\delta_{lq}$, which is that of $\delta_{jk}E_{il}$. Independence holds because the $(i,j)$-entry of a combination is its own coefficient.

**Theorem.** With this product the algebra is associative, unital, non-commutative, of complex dimension $4$ and real dimension $8$.

**Proof.** Both $(AB)C$ and $A(BC)$ have $(i,l)$-entry $\sum_{j,k}a_{ij}b_{jk}c_{kl}$. The unit is $I$. Non-commutativity: $E_{12}E_{21}=E_{11}$ while $E_{21}E_{12}=E_{22}$.

**The product is composition.** The map $A\mapsto(x\mapsto Ax)$ is an isomorphism onto $\operatorname{End}_{\mathbb{C}}(\mathbb{C}^{2})$: injective because $Ae_{j}$ is the $j$-th column, surjective because a map is fixed by the images of a basis. The transpose is an anti-isomorphism onto the opposite algebra, since $(AB)^{\mathsf T}=B^{\mathsf T}A^{\mathsf T}$.

## Trace and Determinant

**Definition.** For $A=\begin{pmatrix}a&b\\c&d\end{pmatrix}$, the trace is $\operatorname{tr}A=a+d$, the determinant is $\det A=ad-bc$, and the characteristic polynomial is

$$
\chi_A(\lambda)=\det(\lambda I-A)=\lambda^{2}-(\operatorname{tr}A)\lambda+\det A .
$$

**Proposition (the trace).** The trace is linear, cyclic, $\operatorname{tr}(AB)=\operatorname{tr}(BA)$, and it is the only linear functional vanishing on all commutators, up to a scalar.

**Proof.** The cyclic identity is the equality $a_{11}b_{11}+a_{12}b_{21}+a_{21}b_{12}+a_{22}b_{22}=\operatorname{tr}(BA)$. A functional vanishes on commutators exactly when it is invariant under transposing the two factors. The commutator subspace is the traceless part, of dimension $3$, so its annihilator in the dual is one-dimensional, and the trace spans it.

**Proposition (the determinant).** The determinant is multiplicative, $\det(AB)=\det A\det B$, and it is the only multiplicative polynomial of degree two, normalised to $1$ at $I$, that vanishes on singular matrices.

**Proof.** Multiplicativity is that of the determinant of a linear map. The normalisation is the Leibniz formula over the two permutations of $S_2$.

**Cayley–Hamilton.** Substituting $A$ gives $A^{2}-(\operatorname{tr}A)A+(\det A)I=0$. At order two this is a four-entry computation: the diagonal identities are $a^{2}+bc=(a+d)a-ad$ and $cb+d^{2}=(a+d)d-ad$. Whenever $\det A\neq0$ the identity gives the inverse

$$
A^{-1}=\frac{1}{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}.
$$

**Worked example.** For $A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$ one has $\operatorname{tr}A=5$ and $\det A=-2$, so $\chi_A=\lambda^{2}-5\lambda-2$, with roots $(5\pm\sqrt{33})/2$, and $A^{-1}=-\tfrac12\begin{pmatrix}4&-2\\-3&1\end{pmatrix}$.

## Rank and the Singular Set

**The rank is the dimension of the image and takes the three values $0,1,2$.** It is $2$ exactly off the determinant hypersurface and $0$ only at the origin, so the rank-one matrices are the remaining stratum.

**Proposition (the strata).** The rank-$r$ set has complex dimension $r(4-r)$: that is $0,3,4$ for $r=0,1,2$.

**Proof.** A rank-one matrix is $uv^{\mathsf T}$ with $u,v\neq0$, and the pair is fixed up to $u\mapsto\lambda u$, $v\mapsto\lambda^{-1}v$, a count of $2+2-1=3$. The rank-two set is open in the four-dimensional space.

**The singular set is the determinant hypersurface.** It has complex dimension $3$ and real codimension $2$, and it is singular only at $0$, because the gradient of the determinant is the cofactor matrix, which vanishes only at rank $0$. **It is not the null cone of a form on the algebra**: the determinant is quadratic, but the singular set is its zero set inside the algebra, and the algebra is read with a positive definite form.

## The Centre and the Simplicity

**Theorem (the centre).** $Z(M_2(\mathbb{C}))=\mathbb{C}I$.

**Proof.** If $A$ commutes with $E_{11}$ then $a_{12}=a_{21}=0$, so $A$ is diagonal; commuting with $E_{12}$ then gives $a_{11}=a_{22}$; conversely a scalar matrix is central.

**Theorem (simplicity).** The only two-sided ideals are $0$ and the algebra.

**Proof.** Let $I\neq0$ and $0\neq A\in I$ with $a_{ij}\neq0$. Then $E_{ii}AE_{jj}=a_{ij}E_{ij}\in I$, so $E_{ij}\in I$, and $E_{ki}E_{ij}E_{jl}=E_{kl}\in I$ for all $k,l$.

**Corollary.** The algebra is central simple. Every automorphism is inner and every derivation is inner, by Skolem–Noether and Noether; the proofs are *The Ideals, the Centre and the Simplicity of $M_2(\mathbb{C})$*.

**The algebra is not a division algebra.** Every off-diagonal unit is a nonzero nilpotent, $E_{12}^{2}=0$, so there are zero divisors and the non-units are exactly the singular matrices.

## The Unit Group and the Projective Group

**Proposition.** $GL_2(\mathbb{C})=\{\det\neq0\}$ is a complex algebraic group of complex dimension $4$. The determinant maps it onto $\mathbb{C}^{\times}$, with kernel $SL_2(\mathbb{C})$ of complex dimension $3$.

**Proof.** The unit group is the complement of a hypersurface in $\mathbb{C}^{4}$; the determinant is polynomial, multiplicative and onto, since $\operatorname{diag}(d,1)$ has determinant $d$; its kernel is a hypersurface, of dimension $3$.

**Proposition.** $PGL_2(\mathbb{C})=GL_2(\mathbb{C})/\mathbb{C}^{\times}I\cong SL_2(\mathbb{C})/\{\pm I\}$, of complex dimension $3$.

**Proof.** Multiply a class by $\lambda$ with $\lambda^{2}=(\det A)^{-1}$ to reach determinant $1$; two such representatives differ by a scalar of square $1$.

**The action.** $PGL_2$ acts by $[g]\cdot A=gAg^{-1}$, and the orbits are the conjugacy classes, classified by $(\operatorname{tr},\det)$ in *The Spectrum of a $2\times2$ Matrix*. On the projective line the action is the Möbius action, which is strictly three-transitive.

## The Reading over the Real Numbers

**Every matrix splits into a Hermitian and an anti-Hermitian part.** Put $A^{*}=\bar A^{\mathsf T}$; the **Hermitian** matrices satisfy $H^{*}=H$ and the **anti-Hermitian** ones $S^{*}=-S$.

**Proposition.** Every $A$ splits uniquely as

$$
A=H+S,\qquad H=\tfrac12(A+A^{*}),\quad S=\tfrac12(A-A^{*}),
$$

so $M_2(\mathbb{C})=\mathfrak{u}(2)\oplus i\mathfrak{u}(2)$ over $\mathbb{R}$, with $\dim_{\mathbb{R}}\mathfrak{u}(2)=4$ and $\dim_{\mathbb{R}}\mathfrak{su}(2)=3$.

**Proof.** The star is conjugate-linear and involutive, so the two parts have the required symmetry and sum to $A$; they meet only at $0$ because $H=-H$ forces $H=0$. A Hermitian matrix has two real diagonal entries and one free off-diagonal complex entry, hence $4$ real parameters.

**Worked example.** For $A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$,

$$
H=\tfrac12(A+A^{*})=\begin{pmatrix}1&\tfrac52\\ \tfrac52&4\end{pmatrix},
\qquad
S=\tfrac12(A-A^{*})=\begin{pmatrix}0&-\tfrac12\\ \tfrac12&0\end{pmatrix},
$$

with $\operatorname{tr}H=5$ and $\operatorname{tr}S=0$.

**The product preserves neither half.** For anti-Hermitian $S,T$ one has $(ST)^{*}=TS$, which equals $-ST$ only when $S$ and $T$ anticommute. The split is one of the real vector space and of the real Lie algebra.

## The Identification with the Biquaternion Algebra

**The algebra is the biquaternion algebra.** The following is the dictionary between the two languages.

**Theorem.** There is an isomorphism of $\mathbb{C}$-algebras $\mathsf M_2:\mathbb{B}\to M_2(\mathbb{C})$ with

$$
\mathsf M_2(e_t)=I,\qquad
\mathsf M_2(\vec e_x)=-i\sigma_1,\qquad
\mathsf M_2(\vec e_y)=-i\sigma_2,\qquad
\mathsf M_2(\vec e_z)=-i\sigma_3 .
$$

**Proof.** The images are independent and reproduce the relations: $\mathsf M_2(\vec e_k)^{2}=-I$ because $\sigma_k^{2}=I$, and $(-i\sigma_1)(-i\sigma_2)=-\sigma_1\sigma_2=-i\sigma_3$ is the image of $\vec e_z$. A linear map agreeing with the products on a basis is a homomorphism, and it is bijective because both spaces have dimension four. The details are *$M_2(\mathbb{C})$ Pauli Representation*.

**Corollary.** $\operatorname{tr}\mathsf M_2(\tilde Q)=2Q_t$ and $\det\mathsf M_2(\tilde Q)=\langle\tilde Q\rangle_{\natural}=Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}$.

**The determinant is the algebraic norm $N$.** Multiplicativity of the determinant is multiplicativity of $N$, and the zero divisors of $\mathbb{B}$ are the singular matrices. This is what the dimension adds: at $n=2$ the determinant is a quadratic form with a genuine cone of real dimension $6$, while at $n\ge3$ the singular set is a hypersurface. The cone is *N-Regularity and N-Degeneracy in the Biquaternion Algebra*.

**Corollary (the four corners).** A complete family of two idempotents of $\mathbb{B}$ maps to a pair of complementary rank-one projections $P_{+}$ and $P_{-}=I-P_{+}$, and the Peirce lines $\mathbb{B}_{st}$ map onto the matrix corners $A_{kl}=P_kM_2(\mathbb{C})P_l$, each one-dimensional. The companion nilpotents $\vec\Upsilon_{+-},\vec\Upsilon_{-+}$ of *The Companion Nilpotents of the Biquaternion Algebra* map onto $E_{12},E_{21}$, and a Peirce basis onto the four matrix units.

**What the identification does not carry.** It is $\mathbb{C}$-linear, so it does not send the real form $\mathbb{H}$ to a real subalgebra; the image is a four-real-dimensional subspace. The two real forms are $M_2(\mathbb{R})$ and $\mathbb{H}$, treated in *The Two Base Fields: $M_2(\mathbb{R})$ inside $M_2(\mathbb{C})$*. The transpose is an anti-automorphism of the matrix algebra and not the quaternion conjugation of $\mathbb{B}$.

## Summary

$M_2(\mathbb{C})$ is the associative unital non-commutative $\mathbb{C}$-algebra of $2\times2$ complex matrices, with

$$
\boxed{\;E_{ij}E_{kl}=\delta_{jk}E_{il},\qquad \dim_{\mathbb{C}}=4,\qquad \dim_{\mathbb{R}}=8.\;}
$$

Its centre is $\mathbb{C}I$ and it is simple, hence central simple. The trace is the only commutator-vanishing functional up to scale, the determinant is multiplicative, and the two are the coefficients of $\chi_A=\lambda^{2}-(\operatorname{tr}A)\lambda+\det A$. The rank takes the values $0,1,2$ on strata of dimensions $0,3,4$, and the singular set is the determinant hypersurface of real codimension two. The unit group is $GL_2(\mathbb{C})$ of dimension $4$, and $PGL_2(\mathbb{C})\cong SL_2(\mathbb{C})/\{\pm I\}$ has dimension $3$. Over $\mathbb{R}$ the algebra is $\mathfrak{u}(2)\oplus i\mathfrak{u}(2)$. It is the biquaternion algebra under $\mathsf M_2(\vec e_k)=-i\sigma_k$, with $\operatorname{tr}=2Q_t$ and $\det=N$.

| Property | Value for $M_2(\mathbb{C})$ |
|---|---|
| Complex dimension | $4$ |
| Real dimension | $8$ |
| Centre | $\mathbb{C}I$ |
| Simple | yes |
| Division algebra | no; $E_{12}^{2}=0$ |
| Unit group | $GL_2(\mathbb{C})$, dimension $4$ |
| Projective group | $PGL_2\cong SL_2/\{\pm I\}$, dimension $3$ |
| Real reading | $\mathfrak{u}(2)\oplus i\mathfrak{u}(2)$, real dimensions $4+4$ |
| Biquaternion model | $\vec e_k\mapsto-i\sigma_k$; $\det=N$, $\operatorname{tr}=2Q_t$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M_2(\mathbb{C})$ | the algebra of $2\times2$ complex matrices |
| $E_{ij}$ | the matrix unit with $1$ in position $(i,j)$ |
| $I$ | the identity matrix |
| $\operatorname{tr}$, $\det$ | the trace and the determinant |
| $\chi_A$ | the characteristic polynomial $\det(\lambda I-A)$ |
| $\mathrm{rank}\,A$ | the dimension of the image |
| $A^{*}=\bar A^{\mathsf T}$ | the conjugate transpose |
| $\mathfrak{u}(2)$, $\mathfrak{su}(2)$ | the anti-Hermitian matrices, and the traceless ones |
| $GL_2(\mathbb{C})$, $SL_2(\mathbb{C})$ | the invertible matrices, and those of determinant $1$ |
| $PGL_2(\mathbb{C})$ | $GL_2(\mathbb{C})/\mathbb{C}^{\times}I$ |
| $\mathsf M_2$ | the isomorphism $\mathbb{B}\to M_2(\mathbb{C})$ |
| $N$ | the algebraic norm, equal to $\det$ |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 2013), for the matrix units, the trace and the determinant at order two.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for central simple algebras and the centre.
- [$M_2(\mathbb{C})$ Pauli Representation](m2c-pauli-representation.html), for the identification with the biquaternion algebra in full.
- [The Biquaternion Algebra](the-biquaternion-algebra.html), for the algebra $\mathbb{B}$ identified with this one.
