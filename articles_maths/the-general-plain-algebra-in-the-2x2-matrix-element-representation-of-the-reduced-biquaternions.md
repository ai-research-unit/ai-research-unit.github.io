# __The General Plain Algebra in the $2\times2$ Matrix Element Representation of the Reduced Biquaternions__

## Introduction

This article reads the general plain algebra in its **$2\times2$ matrix element representation**, the model in which an element is realised as a complex diagonal matrix. The realisation is forced by the idempotent coordinates: because the multiplication is componentwise, the map
$$
\varphi:\mathbb{B}_{\mathrm{r}}\to M_{2}(\mathbb{C}),\qquad T=A+Bj\mapsto\operatorname{diag}(A+B,\ A-B)=\operatorname{diag}(q_1,q_2),
$$
is an algebra isomorphism of $(\mathbb{B}_{\mathrm{r}},\cdot)$ onto the algebra $\mathcal D_{2}(\mathbb{C})$ of the complex **diagonal** $2\times2$ matrices. On the basis it reads
$$
1\mapsto \mathrm I_{2},\qquad i\mapsto i\,\mathrm I_{2},\qquad j\mapsto \sigma_{3}=\operatorname{diag}(1,-1),\qquad ij\mapsto i\sigma_{3}=\operatorname{diag}(i,-i).
$$

**The results.** In the model the multiplication is the matrix product, the unit is $\mathrm I_{2}$, and every structural object of the algebra is a matrix condition or a matrix invariant:

- the **norm** is the determinant, $\langle T\rangle_{\natural}=\det\varphi(T)=q_1q_2$; the **trace** of the element is $\tfrac12\operatorname{Tr}\varphi(T)=A$, and the two eigenvalues of the operator of *The Multiplication Operators of the General Plain Algebra of the Reduced Biquaternions* are the two diagonal entries;
- the **units** are the invertible diagonal matrices, and the **zero divisors** are the nonzero singular diagonal matrices, those with exactly one zero entry;
- the **idempotents** are the four diagonal matrices with entries in $\{0,1\}$, and the two nontrivial ones are the matrix units $E_{11}=\operatorname{diag}(1,0)$ and $E_{22}=\operatorname{diag}(0,1)$;
- the **two minimal ideals** are the two coordinate lines, the matrices with a single nonzero diagonal entry, and the **Peirce decomposition** is the pair of the two diagonal entries, with the off-diagonal entries identically zero;
- the **bar** is the conjugate transpose $\dagger$, the **natural sign** is the swap of the two diagonal entries $\operatorname{diag}(q_1,q_2)\mapsto\operatorname{diag}(q_2,q_1)$, equivalently the conjugation by $\sigma_{1}$, and the **star** is their composite;
- the **general quaternionic sesquilinear form** is $\tfrac12$ the Hilbert–Schmidt form on the diagonal matrices, $\langle T,W\rangle_{\natural*}=\tfrac12\operatorname{Tr}\bigl(\varphi(T)\varphi(W)^{\dagger}\bigr)$, positive definite.

The model is the reduced biquaternion analogue of the matrix realisation $\mathbb{B}\cong M_{2}(\mathbb{C})$ of the biquaternion category, and the difference is the content of the article: the biquaternion algebra is the **whole** of $M_{2}(\mathbb{C})$, the reduced biquaternion algebra is its **diagonal** subalgebra, and the missing off-diagonal entries are the missing matrix units $E_{12},E_{21}$ of the Peirce decomposition.

**Boundaries.** The general plain algebra and its multiplication are *Introduction to the General Plain Algebra of the Reduced Biquaternions*; the norm and the units are *Norm and Invertibility in the General Plain Algebra of the Reduced Biquaternions* and *The Group of Units of the General Plain Algebra of the Reduced Biquaternions*; the ideals and the Peirce decomposition are *Ideals and Peirce Decomposition of the General Plain Algebra of the Reduced Biquaternions*; the multiplication operators are *The Multiplication Operators of the General Plain Algebra of the Reduced Biquaternions*; and the forms are *The Forms of the General Plain Algebra of the Reduced Biquaternions*. The general $2\times2$ element representation of the category, of which this article reads the algebra, is *Introduction to the $2\times2$ Matrix Element Representation of Reduced Biquaternions*; the four-vector model is *The Four-Vector Element Representation of the Reduced Biquaternions*; and the non-commutative matrix realisation is *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*.

## The Representation

### The Map on the Basis

**The map sends the four basis elements to $\mathrm I_{2}$, $i\mathrm I_{2}$, $\sigma_{3}$ and $i\sigma_{3}$, and the real basis to a real four-dimensional space of matrices.**

**Definition.** The **$2\times2$ matrix element representation** of the general plain algebra is the map
$$
\varphi(T)=\varphi(A+Bj)=\begin{pmatrix}A+B&0\\ 0&A-B\end{pmatrix}=\operatorname{diag}(q_1,q_2),
$$
and its image is the algebra $\mathcal D_{2}(\mathbb{C})=\{\operatorname{diag}(q_1,q_2):q_1,q_2\in\mathbb{C}\}\subset M_{2}(\mathbb{C})$.

**Proposition (the images of the basis).** On the real basis,
$$
\varphi(1)=\mathrm I_{2},\qquad \varphi(i)=i\,\mathrm I_{2},\qquad \varphi(j)=\sigma_{3},\qquad \varphi(ij)=i\,\sigma_{3}.
$$

*Proof.* By the definition, $\varphi(1)=\operatorname{diag}(1,1)=\mathrm I_{2}$; $\varphi(i)=\operatorname{diag}(i,i)=i\mathrm I_{2}$; $\varphi(j)=\operatorname{diag}(1,-1)=\sigma_{3}$; and $\varphi(ij)=\operatorname{diag}(i,-i)=i\sigma_{3}$, since $ij=i\cdot j$.

**Corollary (the real structure).** The real span of the four images is the four-dimensional real space of the complex diagonal matrices written in the real basis $(\mathrm I_{2},i\mathrm I_{2},\sigma_{3},i\sigma_{3})$, that is the $\mathbb{R}$-span of $\mathrm I_{2}$ and $\sigma_{3}$ over $\mathbb{C}$; the image of the real algebra is the real space $\mathbb{C}\mathrm I_{2}\oplus\mathbb{C}\sigma_{3}$.

### The Algebra Isomorphism

**The map is an isomorphism of algebras onto the diagonal matrices.**

**Theorem.** $\varphi$ is an isomorphism of $\mathbb{C}$-algebras, $\varphi(TW)=\varphi(T)\varphi(W)$, $\varphi(1)=\mathrm I_{2}$, injective, with image $\mathcal D_{2}(\mathbb{C})$.

*Proof.* In the idempotent coordinates the product is componentwise, $\varphi(TW)=\operatorname{diag}(q_{1,T}q_{1,W},q_{2,T}q_{2,W})=\operatorname{diag}(q_{1,T},q_{2,T})\operatorname{diag}(q_{1,W},q_{2,W})$, which is the multiplicativity; the unit is $\operatorname{diag}(1,1)$. The kernel is $\{T:q_1=q_2=0\}=\{0\}$, so the map is injective, and onto $\mathcal D_{2}(\mathbb{C})$ because every pair $(q_1,q_2)$ is the image of $T=\tfrac12\bigl((q_1+q_2)+(q_1-q_2)j\bigr)$.

**Corollary (the isomorphism of the algebra).** $\mathbb{B}_{\mathrm{r}}\cong\mathcal D_{2}(\mathbb{C})\cong\mathbb{C}\times\mathbb{C}$; the diagonal matrices and the direct product of two copies of $\mathbb{C}$ are two presentations of the same algebra.

**Remark (the diagonal and not the whole matrix algebra).** The image $\mathcal D_{2}(\mathbb{C})$ is a commutative two-dimensional subalgebra of $M_{2}(\mathbb{C})$, of complex dimension two, whereas $M_{2}(\mathbb{C})$ has complex dimension four. The biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ is realised as the whole of $M_{2}(\mathbb{C})$, with the three vector images $-i\sigma_{1},-i\sigma_{2},-i\sigma_{3}$ and the off-diagonal entries carrying the vector part; here the two off-diagonal entries are identically zero, and the vector part $Bj$ sits in the difference of the two diagonal entries, $\langle\cdot,\cdot\rangle=(q_1-q_2)/2$.

## The Structure in the Model

### The Multiplication and the Conjugations

**The product is the matrix product, the bar is the conjugate transpose, the natural sign is the swap, and the star is their composite.**

**Theorem (the conjugations).** Under $\varphi$:
$$
\varphi(\overline{T})=\varphi(T)^{\dagger},\qquad \varphi(T^{\natural})=\sigma_{1}\varphi(T)\sigma_{1}=\operatorname{diag}(q_2,q_1),\qquad \varphi(T^{*})=\operatorname{diag}(\bar q_2,\bar q_1).
$$

*Proof.* The bar conjugates the coefficients, hence each diagonal entry, so it is the conjugate transpose; the natural sign sends $A+Bj$ to $A-Bj$ and hence $(q_1,q_2)$ to $(q_2,q_1)$, which is the conjugation by $\sigma_{1}$ on a diagonal matrix; the star is the composite of the two, $\operatorname{diag}(\bar q_2,\bar q_1)$.

**Corollary (the swap and the transposition).** The map $\operatorname{diag}(q_1,q_2)\mapsto\operatorname{diag}(q_2,q_1)$ is the **transposition of the two factors** of $\mathcal D_{2}(\mathbb{C})\cong\mathbb{C}\times\mathbb{C}$, equivalently the conjugation by $\sigma_{1}$; it is **not** the ordinary matrix transposition, which acts as the identity on the image because every diagonal matrix is symmetric. The natural sign is therefore an **algebra** symmetry of the image invisible in the individual entries; it is visible only through the swap of the two diagonal positions.

### The Norm, the Trace and the Determinant

**The norm is the determinant, and the trace of the element is half the trace of the matrix.**

**Theorem.** For $T=A+Bj$,
$$
\langle T\rangle_{\natural}=\det\varphi(T)=q_1q_2,\qquad \operatorname{Tr}\varphi(T)=q_1+q_2=2A .
$$

*Proof.* The determinant of a diagonal matrix is the product of the entries, $q_1q_2=(A+B)(A-B)=A^{2}-B^{2}=\langle T\rangle_{\natural}$; the trace is the sum, $q_1+q_2=2A$.

**Corollary (the multiplicativity).** $\det\varphi(TW)=\det\varphi(T)\det\varphi(W)$ is the multiplicativity of the norm, read as the multiplicativity of the determinant on diagonal matrices; this is the mechanism of the unit group of *The Group of Units of the General Plain Algebra of the Reduced Biquaternions*.

### The Units, the Zero Divisors and the Idempotents

**The units are the invertible diagonal matrices, the zero divisors the nonzero singular ones, and the idempotents the diagonal matrices with entries $0$ and $1$.**

**Theorem.** Under $\varphi$:

- $T$ is a **unit** exactly when $\varphi(T)$ is invertible, that is $q_1\neq0$ and $q_2\neq0$;
- $T$ is a **zero divisor** exactly when $\varphi(T)\neq0$ is singular, that is exactly one of $q_1,q_2$ is $0$;
- the **idempotents** of the algebra are the four matrices $\operatorname{diag}(\epsilon_{1},\epsilon_{2})$ with $\epsilon_{i}\in\{0,1\}$.

*Proof.* These are the criterion of *Norm and Invertibility in the General Plain Algebra of the Reduced Biquaternions* and *The Group of Units of the General Plain Algebra of the Reduced Biquaternions*, read through the determinant; the idempotents are the diagonal matrices with each entry an idempotent of $\mathbb{C}$, that is $0$ or $1$, which are the four elements of *Square Roots of One and the Idempotents of the General Plain Algebra of the Reduced Biquaternions*.

**Corollary (the idempotent decomposition).** The two nontrivial idempotents are the matrix units
$$
\Pi_{1}\mapsto\operatorname{diag}(1,0)=E_{11},\qquad \Pi_{2}\mapsto\operatorname{diag}(0,1)=E_{22},
$$
with $E_{11}+E_{22}=\mathrm I_{2}$ and $E_{11}E_{22}=0$; the decomposition $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\Pi_{1}\oplus\mathbb{C}\Pi_{2}$ is the decomposition of a diagonal matrix into its two entries.

## The Ideals and the Peirce Decomposition in the Model

**The ideals are the coordinate lines of the diagonal algebra, and the Peirce decomposition is the pair of diagonal entries, the off-diagonal being identically zero.**

**Theorem (the ideals).** The ideals of $\mathcal D_{2}(\mathbb{C})$ are
$$
0,\qquad \mathbb{C}E_{11},\qquad \mathbb{C}E_{22},\qquad \mathcal D_{2}(\mathbb{C}),
$$
where $\mathbb{C}E_{11}$ is the set of the matrices whose only nonzero entry is the first diagonal one, and $\mathbb{C}E_{22}$ the mirror.

*Proof.* This is the ideal theorem of *Ideals and Peirce Decomposition of the General Plain Algebra of the Reduced Biquaternions*, transported by the isomorphism $\varphi$; the coordinate lines are the images of the two minimal ideals.

**Corollary (the Peirce decomposition).** The Peirce decomposition of $\mathcal D_{2}(\mathbb{C})$ along $E_{11}$ is
$$
\mathcal D_{2}(\mathbb{C})=\mathbb{C}E_{11}\oplus\{0\}\oplus\{0\}\oplus\mathbb{C}E_{22},
$$
the two mixed spaces vanishing. The matrix picture makes the reason visible: the image of $\varphi$ contains the diagonal matrix units and **no** off-diagonal one, so there are no $E_{12}$ and $E_{21}$ to carry the mixed spaces; the biquaternion model has them, and this is exactly the difference between a full matrix algebra and the diagonal subalgebra.

## The Forms in the Model

**The general quaternionic sesquilinear form is half the Hilbert–Schmidt form on the diagonal matrices, and the other three forms are its companions read with the transpose and the plain slots.**

**Theorem (the four forms).** For $T=A+Bj$ and $W=C+Dj$ with images $\varphi(T)=\operatorname{diag}(q_1,q_2)$ and $\varphi(W)=\operatorname{diag}(q_1',q_2')$,
$$
\langle T,W\rangle_{\natural*}=\tfrac12\operatorname{Tr}\bigl(\varphi(T)\varphi(W)^{\dagger}\bigr)=\tfrac12\bigl(q_1\bar q_1'+q_2\bar q_2'\bigr),
$$
$$
\langle T,W\rangle_{*}=\tfrac12\bigl(q_1\bar q_2'+q_2\bar q_1'\bigr),\qquad \langle T,W\rangle=\tfrac12\bigl(q_1q_1'+q_2q_2'\bigr),\qquad \langle T,W\rangle_{\natural}=\tfrac12\bigl(q_1q_2'+q_2q_1'\bigr).
$$

*Proof.* Substitute $A=\tfrac12(q_1+q_2)$, $\langle\cdot,\cdot\rangle=\tfrac12(q_1-q_2)$, $C=\tfrac12(q_1'+q_2')$, $D=\tfrac12(q_1'-q_2')$ into the four forms $AC+BD$, $AC-BD$, $A\bar C-B\bar D$, $A\bar C+B\bar D$ of *The Forms of the General Plain Algebra of the Reduced Biquaternions*. The Hilbert–Schmidt identity is $\operatorname{Tr}(\varphi(T)\varphi(W)^{\dagger})=\operatorname{Tr}\bigl(\operatorname{diag}(q_1,q_2)\operatorname{diag}(\bar q_1',\bar q_2')\bigr)=q_1\bar q_1'+q_2\bar q_2'$.

**Corollary (the definiteness and the norms).** $\langle\cdot\rangle_{\natural*}$ is $\tfrac12$ the Hilbert–Schmidt inner product, positive definite, with the norm $\langle T\rangle_{\natural*}=\tfrac12\bigl(|q_1|^{2}+|q_2|^{2}\bigr)=\tfrac12\lVert\varphi(T)\rVert_{F}^{2}$, half the squared Frobenius norm of the matrix; $\langle T\rangle_{*}=\tfrac12\bigl(|q_1|^{2}-|q_2|^{2}\bigr)$ indefinite; and the two bilinear norms are $\langle T\rangle=\tfrac12(q_1^{2}+q_2^{2})$ and $\langle T\rangle_{\natural}=\tfrac12(q_1q_2+q_2q_1)=q_1q_2=\det\varphi(T)$, the determinant. So the multiplicativity of $\langle\cdot,\cdot\rangle_{\natural}$ is the multiplicativity of the determinant, and the definiteness of $\langle\cdot,\cdot\rangle_{\natural*}$ is the definiteness of the Hilbert–Schmidt form.

## Worked Examples

**A generic element.** For $T=3+ij$ the image is $\varphi(T)=\operatorname{diag}(3+i,3-i)$; its determinant is $9-i^{2}=10=\langle T\rangle_{\natural}$, its trace is $6=2A$ with $A=3$, and it is a unit. The Frobenius square is $|3+i|^{2}+|3-i|^{2}=20$, so $\langle T\rangle_{\natural*}=10$.

**A zero divisor.** For $T=\Pi_{1}$ the image is $E_{11}=\operatorname{diag}(1,0)$, with determinant $0$; it is singular, so $T$ is a zero divisor, and its kernel in the model is the coordinate line $\mathbb{C}E_{22}$, the companion of §*The Kernel and the Invertibility* of *The Multiplication Operators of the General Plain Algebra of the Reduced Biquaternions*.

**A root of one.** For $T=j$ the image is $\sigma_{3}=\operatorname{diag}(1,-1)$, an involution with determinant $-1$; its square is $\mathrm I_{2}$, the model reading of $j^{2}=1$, and its trace is $0$, the model reading of $A=0$.

**The conjugations.** For $T=2+3j$ the image is $\operatorname{diag}(5,-1)$; the bar sends it to $\operatorname{diag}(5,-1)$ (the entries are real), the natural sign to $\operatorname{diag}(-1,5)$, and the star to the same $\operatorname{diag}(-1,5)$. For $T=2+i+3j$ the image is $\operatorname{diag}(5+i,-1+i)$, whose bar is $\operatorname{diag}(5-i,-1-i)$ and whose natural sign is $\operatorname{diag}(-1+i,5+i)$.

## The Matrices

**The images of the basis and of the four elements of the standard table.**

| element of $\mathbb{B}_{\mathrm{r}}$ | matrix $\varphi$ | determinant | trace |
|---|---|---|---|
| $1$ | $\mathrm I_{2}$ | $1$ | $2$ |
| $i$ | $i\,\mathrm I_{2}$ | $-1$ | $2i$ |
| $j$ | $\sigma_{3}=\operatorname{diag}(1,-1)$ | $-1$ | $0$ |
| $ij$ | $i\sigma_{3}=\operatorname{diag}(i,-i)$ | $1$ | $0$ |
| $A+Bj$ | $\operatorname{diag}(A+B,A-B)$ | $A^{2}-B^{2}$ | $2A$ |
| $\Pi_{1}$ | $E_{11}$ | $0$ | $1$ |
| $\Pi_{2}$ | $E_{22}$ | $0$ | $1$ |

The table exhibits the two features of the model: the four real basis elements span the real four-dimensional space of the diagonal matrices, and the two idempotents are the two matrix units, with no off-diagonal partner. The comparison with the biquaternion $2\times2$ model, whose images are $\mathrm I_{2}$ and $-i\sigma_{1},-i\sigma_{2},-i\sigma_{3}$ and which span the whole of $M_{2}(\mathbb{C})$, is the content of *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*.

## Summary

The general plain algebra is realised as the algebra of the complex diagonal $2\times2$ matrices by the isomorphism $\varphi(T)=\operatorname{diag}(A+B,A-B)$ on $T=A+Bj$, with the images $\mathrm I_{2}$, $i\mathrm I_{2}$, $\sigma_{3}$ and $i\sigma_{3}$ on the basis. In the model the multiplication is the matrix product and the norm is the determinant, $\langle T\rangle_{\natural}=q_1q_2=\det\varphi(T)$, so the units are the invertible diagonal matrices and the zero divisors are the nonzero singular ones; the idempotents are the four diagonal matrices with entries $0,1$, the two nontrivial ones being the matrix units $E_{11}$ and $E_{22}$. The bar is the conjugate transpose, the natural sign is the transposition of the two diagonal entries, equivalently the conjugation by $\sigma_{1}$, and the star is their composite. The two minimal ideals are the two coordinate lines, and the Peirce decomposition is the pair of diagonal entries with vanishing mixed spaces, because the image contains the diagonal matrix units and no off-diagonal one. The general quaternionic sesquilinear form is half the Hilbert–Schmidt form, positive definite, with the norm half the squared Frobenius norm, and the other three forms are its companions. The realisation is the diagonal analogue of the biquaternion realisation $\mathbb{B}\cong M_{2}(\mathbb{C})$: there the algebra is the whole matrix algebra, here it is the diagonal subalgebra, and the difference is the presence or absence of the off-diagonal matrix units.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\varphi(T)=\operatorname{diag}(q_1,q_2)$ | the $2\times2$ matrix element representation, $q_1=A+B$, $q_2=A-B$ |
| $\mathcal D_{2}(\mathbb{C})$ | the algebra of the complex diagonal $2\times2$ matrices |
| $\mathrm I_{2},\ \sigma_{3},\ i\sigma_{3}$ | the images of $1,j,ij$; $i\mathrm I_{2}$ the image of $i$ |
| $E_{11},E_{22}$ | the diagonal matrix units, the images of $\Pi_{1},\Pi_{2}$ |
| $\det\varphi(T)=q_1q_2=\langle T\rangle_{\natural}$ | the norm as the determinant |
| $\operatorname{Tr}\varphi(T)=2A$ | the trace of the element |
| $\dagger$ | the conjugate transpose, the image of the bar |
| $\sigma_{1}(\cdot)\sigma_{1}$ | the transposition of the diagonal entries, the image of the natural sign |
| $\tfrac12\operatorname{Tr}(\varphi(T)\varphi(W)^{\dagger})$ | the Hilbert–Schmidt form, the general quaternionic sesquilinear form |

## Further Reading

- *Introduction to the General Plain Algebra of the Reduced Biquaternions* (`articles_maths/introduction-to-the-general-plain-algebra-of-the-reduced-biquaternions.md`), for the multiplication and the idempotent coordinates.
- *Norm and Invertibility in the General Plain Algebra of the Reduced Biquaternions* (`articles_maths/norm-and-invertibility-in-the-general-plain-algebra-of-the-reduced-biquaternions.md`), for the norm and the determinant.
- *Ideals and Peirce Decomposition of the General Plain Algebra of the Reduced Biquaternions* (`articles_maths/ideals-and-peirce-decomposition-of-the-general-plain-algebra-of-the-reduced-biquaternions.md`), for the ideals and the Peirce spaces in the model.
- *The Multiplication Operators of the General Plain Algebra of the Reduced Biquaternions* (`articles_maths/the-multiplication-operators-of-the-general-plain-algebra-of-the-reduced-biquaternions.md`), for the diagonalisation of the operators in these coordinates.
- *The Forms of the General Plain Algebra of the Reduced Biquaternions* (`articles_maths/the-forms-of-the-general-plain-algebra-of-the-reduced-biquaternions.md`), for the four forms read in the model.
- *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* (`articles_maths/introduction-to-the-2x2-matrix-element-representation-of-biquaternions.md`), for the non-commutative companion realising the whole matrix algebra.
