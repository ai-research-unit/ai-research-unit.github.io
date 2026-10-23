# __The Eigenvalue Decomposition in a Clifford Algebra__

## Introduction

A Clifford algebra is an associative algebra with a **grade decomposition**, and its centre is larger than the scalars in odd dimension: the volume element is central and may supply a non-scalar coefficient. The **eigenvalue decomposition** of an element $a$,

$$
a=\sum_{i=1}^{r}\lambda_{i}e_{i},
$$

therefore depends on a choice of **coefficient field** $K$. The eigenvalues $\lambda_{i}$ lie in $K$; the eigenprojectors $e_{i}$ are idempotents of the Clifford algebra, or of its scalar extension; and the grade decomposition records the grades of both. The article develops the existence theorem in this setting, identifies the role of the centre and the volume element, and separates the two kinds of non-scalar eigenvalue: the **internal** ones, which are central multivectors of the algebra, and the **external** ones, which are scalars of a field extension. The internal case is the characteristic phenomenon of odd dimension; the external case is the characteristic phenomenon of even dimension and of the division algebras.

The base is a field $F$ of characteristic not two, $V$ is a finite-dimensional $F$-space, $Q$ is a non-degenerate quadratic form on $V$, and $\mathrm{Cl}=\mathrm{Cl}(V,Q)$ is the Clifford algebra with $v^{2}=Q(v)1$. The grade decomposition, the volume element $\omega$, the reversion and the grade involution are from *The Geometric Product and the Grade Decomposition* and *Clifford Algebras in Finite Dimensions*; the centre is from *Clifford Algebras in Finite Dimensions*, §*16. The Centre*; the volume element and the Hodge star are from *The Volume Element, Duality and the Hodge Star*, §*Multiplication by the Volume Element*; the idempotents and the minimal left ideals are from *Spinors as Minimal Left Ideals with Inner Conjugation*; the matrix classification is from *The Low-Dimensional Classification* and *The Number Systems as Clifford Algebras*; the associative original is *The Eigenvalue Decomposition of an Element*; and the application to the biquaternion algebra is *The Biquaternion Eigenvalue Decomposition*.

## Coefficient Fields and the Existence Theorem

### Coefficient Fields

**Definition.** A **coefficient field** for $a\in\mathrm{Cl}$ is a field $K$ together with a $K$-algebra $\mathrm{Cl}_{K}$ that is one of the following:

1. $K=F$ and $\mathrm{Cl}_{K}=\mathrm{Cl}$;
2. $K$ is a subfield of the centre $Z(\mathrm{Cl})$ and $\mathrm{Cl}_{K}=\mathrm{Cl}$, viewed as a $K$-algebra;
3. $K$ is a field extension of $F$ and $\mathrm{Cl}_{K}=\mathrm{Cl}\otimes_{F}K$.

In each case $a$ is viewed in $\mathrm{Cl}_{K}$, the algebra $K[a]$ is a finite-dimensional commutative $K$-algebra, and the grade decomposition of $\mathrm{Cl}$ extends to $\mathrm{Cl}_{K}$ by $K$-linearity. The case 1 is the **scalar** case, the case 2 is the **internal** case, and the case 3 is the **external** case.

**Remark.** The internal and the external cases are different even when the field $K$ is the same. In the internal case the algebra is the given Clifford algebra, with $K$ sitting inside its centre; in the external case the algebra is the scalar extension $\mathrm{Cl}\otimes_{F}K$, of larger dimension. For $\mathrm{Cl}_{3,0}$ over $\mathbb{R}$ and $K=\mathbb{C}$ the internal algebra is the four-dimensional $\mathbb{C}$-algebra $M_{2}(\mathbb{C})$, while the external algebra is the eight-dimensional $\mathbb{C}$-algebra $M_{2}(\mathbb{C})\times M_{2}(\mathbb{C})$; the internal eigenvalues $\pm\omega$ live in the first, the external ones would live in a scalar extension and have grade $0$.

**Definition.** A **$K$-eigenvalue** of $a$ is a scalar $\lambda\in K$ for which $a-\lambda1$ is not invertible in $K[a]$. The **$K$-spectrum** $\sigma_{K}(a)$ is the set of the $K$-eigenvalues. A **$K$-eigenvalue decomposition** is a writing

$$
a=\sum_{i=1}^{r}\lambda_{i}e_{i}
$$

with $\lambda_{i}\in K$ pairwise distinct, $e_{i}\in\mathrm{Cl}_{K}$ nonzero idempotents satisfying $e_{i}e_{j}=\delta_{ij}e_{i}$ and $\sum_{i}e_{i}=1$, and $\lambda_{i}$ commuting with $e_{i}$ for every $i$.

**Remark.** The definition reduces to the associative one of *The Eigenvalue Decomposition of an Element* when $K=F$ and to the scalar extension of that article when $K/F$ is an extension. The internal case is the new one: $K$ is a subfield of the centre, so the eigenvalues are elements of the Clifford algebra itself, and their grade decomposition is available. The requirement that the eigenvalues commute with the projectors is automatic when $K\subseteq Z(\mathrm{Cl})$, and it is the condition that makes the eigenvalue equation $ae_{i}=\lambda_{i}e_{i}$ meaningful in the noncommutative algebra.

### The Existence Theorem

**Theorem.** Let $K$ be a coefficient field for $a$ and let $m_{a,K}\in K[t]$ be the minimal polynomial of $a$ over $K$. The following are equivalent:

1. $a$ has a $K$-eigenvalue decomposition;
2. $m_{a,K}$ splits over $K$ with distinct roots;
3. $m_{a,K}(t)=\prod_{i=1}^{r}(t-\lambda_{i})$ with $\lambda_{i}\in K$ pairwise distinct.

When they hold, the eigenvalues are the $\lambda_{i}$, the eigenprojectors are the Lagrange polynomials

$$
\boxed{\;e_{i}=\prod_{j\neq i}\frac{a-\lambda_{j}}{\lambda_{i}-\lambda_{j}}\;},
$$

and the decomposition is unique.

*Proof.* The algebra $K[a]$ is finite dimensional, commutative and associative, and its product is the product of $\mathrm{Cl}_{K}$. The theorem is *The Eigenvalue Decomposition of an Element*, §*Existence and Uniqueness*, applied to the element $a$ of $K[a]$: the idempotents produced there lie in $K[a]$, hence in $\mathrm{Cl}_{K}$, and the Lagrange formula is the one of that article. The eigenvalue criterion is the same: $a-\lambda$ is not invertible in $K[a]$ exactly when $m_{a,K}(\lambda)=0$.

**Corollary.** The eigenprojectors lie in $K[a]$, they commute with $a$ and with one another, and their sum is $1$. In the internal case they are elements of the Clifford algebra with a grade decomposition; in the external case they are elements of the scalar extension, and their grade decomposition is the extension of the grade decomposition of $\mathrm{Cl}$.

**Remark.** The theorem is coefficient-dependent in a strong sense. The same element may have no eigenvalue over $F$, a full set of eigenvalues over an extension $K$, and a different set of eigenvalues over the centre. The spectrum is not a property of $a$ alone; it is a property of the pair $(a,K)$.

## The Centre and the Volume Element

### The Centre

**Theorem.** Let $\omega=u_{1}\cdots u_{n}$ be the volume element of an orthogonal basis.

1. If $n$ is even, the centre of $\mathrm{Cl}$ is $F$.
2. If $n$ is odd, the centre is $F[\omega]$, a quadratic algebra over $F$ with $\omega\notin F$; it is a field when $\omega^{2}$ is not a square in $F$, and it is isomorphic to $F\times F$ when $\omega^{2}$ is a nonzero square.
3. In both cases
    $$
    \omega^{2}=(-1)^{n(n-1)/2}Q(u_{1})\cdots Q(u_{n}).
    $$

*Proof.* The volume element is central in odd dimension because it has grade $n$ and $n-1$ is even; in even dimension it commutes with the even part and anticommutes with the odd part, so it is not central. The centre is spanned by $1$ and, in odd dimension, by $\omega$; this is *Clifford Algebras in Finite Dimensions*, §*16. The Centre*. The formula for the square is the computation of *The Volume Element, Duality and the Hodge Star*, §*Multiplication by the Volume Element*.

**Corollary.** For the definite real forms, $\omega^{2}=(-1)^{n(n-1)/2}$ and the centre is $\mathbb{R}\times\mathbb{R}$ for $n\equiv1\pmod4$ and $\mathbb{C}$ for $n\equiv3\pmod4$. In particular $\mathrm{Cl}_{1,0}\cong\mathbb{R}\times\mathbb{R}$ and $\mathrm{Cl}_{3,0}\cong M_{2}(\mathbb{C})$.

**Remark.** In even dimension there is no internal non-scalar eigenvalue: the centre is the scalar field, and every eigenvalue over $F$ is a scalar. The non-scalar eigenvalues of an even-dimensional Clifford algebra are necessarily external, obtained by extending the scalars. In odd dimension the centre is a quadratic algebra, and an internal non-scalar eigenvalue is a central multivector $\lambda_{0}+\lambda_{n}\omega$ with grades $0$ and $n$, not a scalar.

### The Grade of a Central Eigenvalue

**Proposition.** Let $n$ be odd and let $\lambda\in Z(\mathrm{Cl})$ be written $\lambda=\lambda_{0}+\lambda_{n}\omega$ with $\lambda_{0},\lambda_{n}\in F$. Then $\lambda$ has grade support in $\{0,n\}$. If $\lambda\notin F$, then $\lambda_{n}\neq0$ and the eigenvalue has a nonzero top-grade part.

*Proof.* The volume element is homogeneous of grade $n$, and the scalars are of grade $0$; a linear combination has the grade support of its terms. The top-grade part is $\lambda_{n}\omega$.

**Remark.** This is the sense in which an internal eigenvalue is a **multivector eigenvalue**: it is not a scalar of the base field, but a central element with a top-grade component. The eigenprojectors, by contrast, can have grades spread over several degrees; the grade decomposition of the pair is the subject of §*The Grade Decomposition of the Spectral Data*.

### The Centre as a Coefficient Field

When $Z(\mathrm{Cl})$ is a field, it is a coefficient field in the sense of case 2, and the algebra $\mathrm{Cl}$ is a $Z$-algebra. The eigenvalues in $Z$ are the **internal non-scalar** eigenvalues. When $Z(\mathrm{Cl})\cong F\times F$, it is not a field; choosing $r\in F$ with $\omega^{2}=r^{2}$, the two central idempotents

$$
\pi_{\pm}=\tfrac12(1\pm\omega/r)
$$

split $\mathrm{Cl}$ into two ideals, and the spectral theory over $F$ is the spectral theory of the two components. The split case is the algebra-level analogue of a scalar with two eigenvalues; the non-split case is the algebra-level analogue of a quadratic extension.

## Internal and External Non-Scalar Eigenvalues

### The Two Kinds

**Definition.** An eigenvalue of $a$ is **scalar** when it lies in $F$. It is **internally non-scalar** when it lies in $Z(\mathrm{Cl})\setminus F$ and $Z(\mathrm{Cl})$ is a field. It is **externally non-scalar** when it lies in $K\setminus F$ for a field extension $K/F$ with $\mathrm{Cl}_{K}=\mathrm{Cl}\otimes_{F}K$.

**Remark.** The distinction is not terminological. An internal eigenvalue is an element of the Clifford algebra, with a grade decomposition; an external eigenvalue is a scalar of the extended field, with grade $0$ in the extended algebra. The internal eigenvalue can be multiplied by the projectors inside the algebra; the external one can only be adjoined. The examples below show the two mechanisms side by side.

### The Internal Case: A Bivector in Three Dimensions

Let $\mathrm{Cl}=\mathrm{Cl}_{3,0}$ over $\mathbb{R}$, with $\omega=u_{1}u_{2}u_{3}$, $\omega^{2}=-1$, and $Z=\mathbb{R}[\omega]\cong\mathbb{C}$. Let

$$
a=u_{1}u_{2}=\omega u_{3}.
$$

The element is a bivector of grade $2$, and

$$
a^{2}=u_{1}u_{2}u_{1}u_{2}=-u_{1}^{2}u_{2}^{2}=-1=\omega^{2}.
$$

The minimal polynomial over $Z$ is

$$
m_{a,Z}(t)=t^{2}+1=(t-\omega)(t+\omega),
$$

so the internal eigenvalues are $\pm\omega$. The eigenprojectors are

$$
e_{\pm}=\tfrac12(1\pm u_{3}),
$$

the standard idempotents of the unit vector $u_{3}$; they are idempotent, orthogonal and complete, and

$$
a=u_{1}u_{2}=\omega u_{3}=\omega e_{+}-\omega e_{-}.
$$

The eigenvalues are $\pm\omega$, of grade $3$; the projectors have grades $0$ and $1$. The element $a$ has grade $2$, and the grade-$1$ parts of the projectors cancel in the sum $e_{+}+e_{-}=1$. The resolution is the Peirce decomposition of the algebra relative to the idempotent $e_{+}$ (equivalently, to $e_{-}$), and the left ideals $\mathrm{Cl}e_{\pm}$ are the two minimal left ideals, the spinor spaces of *Spinors as Minimal Left Ideals with Inner Conjugation*, §*Three Dimensions*.

**Remark.** The same element over $F=\mathbb{R}$ has minimal polynomial $t^{2}+1$, which is irreducible; it has no scalar eigenvalue and no decomposition over $\mathbb{R}$. The internal eigenvalue exists only because the centre is larger than $\mathbb{R}$. In this sense the volume element of an odd-dimensional algebra is a built-in complex structure, and the internal non-scalar eigenvalues are the eigenvalues that it makes available.

### The External Case: A Bivector in the Plane

Let $\mathrm{Cl}=\mathrm{Cl}_{2,0}$ over $\mathbb{R}$, with $u_{1}^{2}=u_{2}^{2}=1$ and $a=u_{1}u_{2}$. Then $a^{2}=-1$, and the minimal polynomial over $\mathbb{R}$ is $t^{2}+1$, irreducible. There is no real eigenvalue decomposition. Over the extension $K=\mathbb{C}$,

$$
m_{a,\mathbb{C}}(t)=t^{2}+1=(t-i)(t+i),
$$

and the eigenprojectors are

$$
e_{\pm}=\tfrac12(1\mp i u_{1}u_{2}).
$$

They are idempotent, orthogonal and complete, and $a=i e_{+}-i e_{-}$. The eigenvalues $\pm i$ are external scalars of grade $0$; the projectors have grades $0$ and $2$. The element $a$ has grade $2$, and the decomposition lives in $\mathrm{Cl}_{2,0}\otimes_{\mathbb{R}}\mathbb{C}\cong M_{2}(\mathbb{C})$.

**Remark.** The contrast with the previous example is the whole content of the internal/external distinction. In $\mathrm{Cl}_{3,0}$ the imaginary unit is the central volume element, of grade $3$, and the projectors have grades $0$ and $1$; in $\mathrm{Cl}_{2,0}$ the imaginary unit is an external scalar, of grade $0$, and the projectors have grades $0$ and $2$. The two algebras have different complexifications, $\mathrm{Cl}_{3,0}\otimes\mathbb{C}\cong M_{2}(\mathbb{C})\times M_{2}(\mathbb{C})$ and $\mathrm{Cl}_{2,0}\otimes\mathbb{C}\cong M_{2}(\mathbb{C})$, and the grade of the imaginary unit is what distinguishes the two readings.

### The Division Case

Let $\mathrm{Cl}=\mathrm{Cl}_{0,2}\cong\mathbb{H}$ over $\mathbb{R}$, with $u_{1}^{2}=u_{2}^{2}=-1$ and $a=u_{1}u_{2}$. The algebra is a division algebra, so its only idempotents are $0$ and $1$; it has no nontrivial spectral resolution. The element $a$ has $a^{2}=-1$ and no real eigenvalue. Over $\mathbb{C}$ the algebra becomes $M_{2}(\mathbb{C})$, and the decomposition of the previous subsection applies, with the same formulas and the same external eigenvalues $\pm i$. The real algebra has no decomposition for $a$, not because the polynomial fails to split in some extension, but because there are no idempotents to receive the eigenvalues.

**Remark.** The example is the Clifford case of *The Number Systems as Algebras with and without Nontrivial Idempotents*, §*Division Algebras Have None*. A division algebra can have a scalar extension that is a matrix algebra and can have a full spectral theory there; the theory does not descend to the division algebra, because the projectors do not descend. The obstruction is the absence of idempotents, not the absence of eigenvalues in an extension.

## The Grade Decomposition of the Spectral Data

### The Standard Idempotents

The idempotents that occur in the spectral resolutions above are the standard ones of the Clifford algebra.

1. **The vector idempotent.** For a unit vector $u\in V$, $u^{2}=1$, the element
    $$
    \pi_{u}=\tfrac12(1+u)
    $$
    is an idempotent of grades $0$ and $1$. Its left ideal $\mathrm{Cl}\pi_{u}$ is a spinor module when the form is definite, and the Peirce decomposition relative to $\pi_{u}$ has the diagonal part $\pi_{u}\mathrm{Cl}\pi_{u}\oplus(1-\pi_{u})\mathrm{Cl}(1-\pi_{u})$ and the mixed part.
2. **The central idempotent.** When $\omega^{2}=1$, the element
    $$
    \pi_{\pm}=\tfrac12(1\pm\omega)
    $$
    is a central idempotent of grades $0$ and $n$. The two split the algebra, $\mathrm{Cl}=\mathrm{Cl}\pi_{+}\oplus\mathrm{Cl}\pi_{-}$, and each factor is an ideal.
3. **The Witt idempotent.** For an orthogonal basis of isotropic vectors $a_{1},a_{1}^{\dagger},\dots,a_{m},a_{m}^{\dagger}$ with the Witt normalisation of *Spinors as Minimal Left Ideals with Inner Conjugation*, §*The Witt Basis*, the product
    $$
    \pi=a_{1}a_{1}^{\dagger}\cdots a_{m}a_{m}^{\dagger}
    $$
    is a primitive idempotent whose grade support is spread over the even grades; the left ideal $\mathrm{Cl}\pi$ is the exterior algebra of the creation operators.

**Remark.** The grade support of an idempotent is not arbitrary. The idempotent equation compares the grades of $\pi^{2}$ and $\pi$; the scalar part of $\pi$ is an idempotent of the base field, hence $0$ or $1$, and the top-grade part is constrained by the top-grade part of the product. The standard idempotents saturate the two extreme cases: the vector idempotent has the smallest positive grade, and the central idempotent has the largest.

### The Cancellation of the Higher Grades

**Proposition.** Let $a=\sum_{i=1}^{r}\lambda_{i}e_{i}$ be a $K$-eigenvalue decomposition and let $e_{i}=\sum_{k=0}^{n}e_{i,k}$ be the grade decomposition of the projectors. Then for every $k>0$,

$$
\boxed{\;\sum_{i=1}^{r}e_{i,k}=0\;} .
$$

In particular the top-grade parts of the projectors cancel, and the scalar parts sum to $1$.

*Proof.* The sum of the projectors is $1$, which has grade $0$; comparing the grade components gives the identities. The scalar part of $1$ is $1$ and its positive-grade parts are $0$.

**Remark.** The cancellation is the grade-level form of the resolution of the identity. In the example $a=u_{1}u_{2}$ of $\mathrm{Cl}_{3,0}$, the projectors $e_{\pm}=\frac12(1\pm u_{3})$ have vector parts $\pm\frac12 u_{3}$, which cancel; the scalar parts sum to $1$. In the external example of $\mathrm{Cl}_{2,0}$, the projectors $e_{\pm}=\frac12(1\mp i u_{1}u_{2})$ have bivector parts $\mp\frac12 i u_{1}u_{2}$, which cancel. The cancellation is the reason a pair of conjugate idempotents can sum to the identity while each carries a nonzero multivector part.

### The Grade of the Eigenvalue Equation

**Remark.** The eigenvalue equation is a grade equation as well as a scalar equation, but the grade bookkeeping is not a simple shift. The product of a homogeneous element of grade $k$ with a homogeneous element of grade $j$ has the grades

$$
\lvert k-j\rvert,\ \lvert k-j\rvert+2,\ \dots,\ k+j,
$$

by the grade theorem of *The Geometric Product and the Grade Decomposition*. If the eigenprojector $e$ is not homogeneous, its product with $a$ spreads over all the grades obtained from the grades of $e$, and the eigenvalue equation says that the resulting multivector equals the scalar multiple $\lambda e$ grade by grade. The equation therefore constrains the support of $e$, but it does not pair the grades one to one.

**Example.** In $\mathrm{Cl}_{3,0}$ with $a=u_{1}u_{2}$ of grade $2$, the projector $e_{+}=\frac12(1+u_{3})$ has grades $0$ and $1$. The product $a e_{+}=\frac12(u_{1}u_{2}+\omega)$ has grades $2$ and $3$; the eigenvalue $\omega$ has grade $3$, and $\omega e_{+}=\frac12(\omega+u_{1}u_{2})$ has the same grades $2$ and $3$. The product of the grade $3$ of the eigenvalue with the grade $0$ of the projector gives grade $3$; its product with the grade $1$ of the projector gives grade $2$, because the grades $3$ and $1$ multiply to the grades $2$ and $4$, and grade $4$ is absent in dimension three. The two contributions reproduce the product.

**Example.** In $\mathrm{Cl}_{2,0}$ over $\mathbb{C}$ with $a=u_{1}u_{2}$ of grade $2$, the projector $e_{+}=\frac12(1-i u_{1}u_{2})$ has grades $0$ and $2$. The product $a e_{+}=\frac12(u_{1}u_{2}+i)$ has grades $2$ and $0$; the external eigenvalue $i$ has grade $0$, and $i e_{+}=\frac12(i+u_{1}u_{2})$ has the same grades $2$ and $0$. The projector is not homogeneous, and the two grades are exchanged by the multiplication.

**Remark.** The examples show why the projectors of a homogeneous element are not usually homogeneous. The scalar part of a projector is an idempotent of the base field, hence $0$ or $1$; the higher-grade parts are constrained by the eigenvalue equation and by the resolution of the identity, and they cancel in the sum of a complete family.

## The Matrix Model and the Reduced Spectrum

### The Algebraic Closure

Over an algebraic closure $\bar F$, the Clifford algebra is a full matrix algebra or a product of two copies:

$$
\boxed{\;\mathrm{Cl}\otimes_{F}\bar F\cong
\begin{cases}
M_{N}(\bar F), & n\text{ even},\\[2pt]
M_{N}(\bar F)\times M_{N}(\bar F), & n\text{ odd},
\end{cases}
\qquad N=2^{n/2}\text{ or }2^{(n-1)/2}\;},
$$

by *The Low-Dimensional Classification*. The eigenvalue decomposition over $\bar F$ is the matrix eigenvalue decomposition of *The Eigenvalue Decomposition of a Matrix*; the Clifford-specific content is the grade of the eigenvalues and the projectors.

### The Reduced Characteristic Polynomial

When $Z(\mathrm{Cl})$ is a field and $\mathrm{Cl}$ is central simple over $Z$ of degree $N$, the **reduced characteristic polynomial** of $a$ is

$$
\operatorname{Nrd}(t-a)=\det\mathsf{M}_{N}(t-a)\in Z[t],
$$

where $\mathsf{M}_{N}$ is a matrix model over $Z$. Its roots in $Z$, with multiplicities, are the internal eigenvalues of $a$. The model over $Z$ is not the scalar extension $\mathrm{Cl}\otimes_{F}\bar F$ of the previous subsection: for $\mathrm{Cl}_{3,0}$ the model over $Z=\mathbb{C}$ is $M_{2}(\mathbb{C})$, while the complexification is $M_{2}(\mathbb{C})\times M_{2}(\mathbb{C})$. In $\mathrm{Cl}_{3,0}$ the reduced characteristic polynomial of $a=u_{1}u_{2}$ is $t^{2}+1=(t-\omega)(t+\omega)$. In $\mathrm{Cl}_{2,0}$ over $Z=\mathbb{R}$, the model is $M_{2}(\mathbb{R})$ and the reduced characteristic polynomial is again $t^{2}+1$, with no real root; the roots $\pm i$ appear only after the external extension.

**Remark.** The reduced characteristic polynomial is the Clifford analogue of the characteristic polynomial of a matrix. Its coefficients lie in the centre, so its roots are internal when the centre is a field; the external eigenvalues are the roots after extending the scalars. The minimal polynomial of the existence theorem is the squarefree part of the reduced characteristic polynomial when the element is semisimple; the two coincide when in addition all the eigenvalues are distinct.

## Examples and the Low-Dimensional Table

### The Split Line

Let $\mathrm{Cl}=\mathrm{Cl}_{1,0}$ over $F$, with $u_{1}^{2}=1$. The centre is $F[u_{1}]\cong F\times F$, and the algebra is split. For $a=u_{1}$ the minimal polynomial is $t^{2}-1=(t-1)(t+1)$, and the spectral resolution is

$$
u_{1}=1\cdot\pi_{+}+(-1)\cdot\pi_{-}, \qquad \pi_{\pm}=\tfrac12(1\pm u_{1}).
$$

The projectors are central idempotents of grades $0$ and $1$; the eigenvalues $\pm1$ are scalars. The resolution is the decomposition of the algebra into its two ideals.

### The Split Plane

Let $\mathrm{Cl}=\mathrm{Cl}_{1,1}$ over $F$, with $u_{1}^{2}=1$, $u_{2}^{2}=-1$, and $a=u_{1}u_{2}$. Then $a^{2}=1$, the minimal polynomial is $t^{2}-1$, and

$$
a=1\cdot\pi_{+}+(-1)\cdot\pi_{-}, \qquad \pi_{\pm}=\tfrac12(1\pm u_{1}u_{2}).
$$

The projectors have grades $0$ and $2$, and the eigenvalues are scalars. The algebra is $\mathrm{Cl}_{1,1}\cong M_{2}(F)$, and the resolution is the matrix spectral resolution of a split involution.

### The Definite Plane

Let $\mathrm{Cl}=\mathrm{Cl}_{2,0}$ over $\mathbb{R}$, with $a=u_{1}u_{2}$. Over $\mathbb{R}$ the minimal polynomial is $t^{2}+1$, irreducible; there is no real resolution. Over $\mathbb{C}$ the eigenvalues are $\pm i$ and the projectors are $\tfrac12(1\mp i u_{1}u_{2})$, of grades $0$ and $2$. The algebra is $M_{2}(\mathbb{R})$ over $\mathbb{R}$ and $M_{2}(\mathbb{C})$ over $\mathbb{C}$.

### The Definite Three-Space

Let $\mathrm{Cl}=\mathrm{Cl}_{3,0}$ over $\mathbb{R}$, with $a=u_{1}u_{2}=\omega u_{3}$. The centre is $\mathbb{C}$, the eigenvalues are $\pm\omega$, and the projectors are $\tfrac12(1\pm u_{3})$, of grades $0$ and $1$. The algebra is $M_{2}(\mathbb{C})$ over $\mathbb{C}$.

### The Table

| Algebra | Centre | Element | Coefficient field | Eigenvalues | Grades of projectors |
|---|---|---|---|---|---|
| $\mathrm{Cl}_{1,0}$ | $\mathbb{R}\times\mathbb{R}$ | $u_{1}$ | $\mathbb{R}$ | $\pm1$ | $0,1$ |
| $\mathrm{Cl}_{1,1}$ | $\mathbb{R}$ | $u_{1}u_{2}$ | $\mathbb{R}$ | $\pm1$ | $0,2$ |
| $\mathrm{Cl}_{2,0}$ | $\mathbb{R}$ | $u_{1}u_{2}$ | $\mathbb{R}$ | none | --- |
| $\mathrm{Cl}_{2,0}\otimes\mathbb{C}$ | $\mathbb{C}$ | $u_{1}u_{2}$ | $\mathbb{C}$ | $\pm i$ | $0,2$ |
| $\mathrm{Cl}_{3,0}$ | $\mathbb{C}$ | $u_{1}u_{2}$ | $\mathbb{C}$ | $\pm\omega$ | $0,1$ |
| $\mathrm{Cl}_{0,2}\cong\mathbb{H}$ | $\mathbb{R}$ | $u_{1}u_{2}$ | $\mathbb{R}$ | none | --- |
| $\mathrm{Cl}_{0,2}\otimes\mathbb{C}$ | $\mathbb{C}$ | $u_{1}u_{2}$ | $\mathbb{C}$ | $\pm i$ | $0,2$ |

**Remark.** The table exhibits the two mechanisms. In $\mathrm{Cl}_{3,0}$ the imaginary unit is internal, of grade $3$, and the eigenvalues are central multivectors; in $\mathrm{Cl}_{2,0}$ and $\mathrm{Cl}_{0,2}$ the imaginary unit is external, of grade $0$, and the eigenvalues are scalars of the extension. In $\mathrm{Cl}_{1,0}$ and $\mathrm{Cl}_{1,1}$ the eigenvalues are scalar from the start, and the projectors are central or matrix idempotents according to the splitness of the algebra.

## Summary

The **eigenvalue decomposition** of an element $a$ of a Clifford algebra is taken over a **coefficient field** $K$: the base field, a subfield of the centre, or a scalar extension. It exists exactly when the minimal polynomial $m_{a,K}$ splits over $K$ with distinct roots; the eigenprojectors are the Lagrange polynomials in $a$, and the decomposition is unique. The spectrum depends on $K$, not on $a$ alone.

The centre is $F$ in even dimension and $F[\omega]$ in odd dimension, with $\omega$ the volume element and $\omega^{2}=(-1)^{n(n-1)/2}Q(u_{1})\cdots Q(u_{n})$. An **internal** non-scalar eigenvalue is a central element of grade $0$ and $n$; an **external** non-scalar eigenvalue is a scalar of a field extension, of grade $0$. In even dimension only the external kind occurs; in odd dimension both occur, and the internal kind is the characteristic feature.

The eigenprojectors are idempotents with a grade decomposition. The vector idempotent $\tfrac12(1+u)$ has grades $0$ and $1$; the central idempotent $\tfrac12(1+\omega)$, when $\omega^{2}=1$, has grades $0$ and $n$; the Witt idempotent has a spread support. The positive-grade parts of a complete family of projectors cancel, because their sum is the identity. The eigenvalue equation pairs the grades of the element with those of the projectors.

A division Clifford algebra, such as $\mathrm{Cl}_{0,2}\cong\mathbb{H}$, has no nontrivial idempotents, so it has no nontrivial eigenvalue decomposition even when a scalar extension has one. A split Clifford algebra, such as $\mathrm{Cl}_{1,0}$ or $\mathrm{Cl}_{1,1}$, has the idempotents and the decomposition. The biquaternion algebra is the case $\mathrm{Cl}_{3,0}$, where the volume element is the central imaginary unit; its eigenvalue decomposition is *The Biquaternion Eigenvalue Decomposition*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $F$ | a field of characteristic not two |
| $V$, $Q$ | a finite-dimensional $F$-space and a non-degenerate quadratic form |
| $\mathrm{Cl}=\mathrm{Cl}(V,Q)$ | the Clifford algebra, $v^{2}=Q(v)1$ |
| $n$ | the dimension of $V$ |
| $u_{1},\dots,u_{n}$ | an orthogonal basis of $V$ |
| $\mathrm{Cl}^{k}$ | the grade-$k$ part of the algebra |
| $\omega$ | the volume element, a product of an orthogonal basis |
| $Z(\mathrm{Cl})$ | the centre |
| $K$ | a coefficient field |
| $\mathrm{Cl}_{K}$ | the algebra $\mathrm{Cl}$ or $\mathrm{Cl}\otimes_{F}K$ |
| $m_{a,K}$ | the minimal polynomial of $a$ over $K$ |
| $\sigma_{K}(a)$ | the $K$-spectrum |
| $a=\sum_{i}\lambda_{i}e_{i}$ | the $K$-eigenvalue decomposition |
| $e_{i}$ | the eigenprojectors, $e_{i}e_{j}=\delta_{ij}e_{i}$, $\sum_{i}e_{i}=1$ |
| $e_{i,k}$ | the grade-$k$ component of $e_{i}$ |
| $\pi_{u}=\tfrac12(1+u)$ | the idempotent of a unit vector |
| $\pi_{\pm}=\tfrac12(1\pm r)$, $r^{2}=1$ | the idempotents of a root of $1$; central when $r$ is central |

## Further Reading

- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the centre, the volume element and the classification.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2001), for the grade decomposition and the idempotents.
- Rafał Abłamowicz and Bertfried Fauser (eds.), *Clifford Algebras and Their Applications in Mathematical Physics* (Birkhäuser, 2000), for the multivector idempotents and the spinor ideals.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the eigenvalue decomposition and the Peirce decomposition in an associative algebra.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the central simple algebras and their reduced characteristic polynomials.
