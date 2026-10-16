# __Reduced Biquaternion Spectral Theory__

## Introduction

The reduced biquaternion algebra $\mathbb{B}_{\mathrm{r}}\cong\mathbb{C}\times\mathbb{C}$ is commutative, associative and unital, and it is **not** a division algebra; both facts simplify the spectral theory and separate it from the two non-commutative members of the family. In this article **spectrum** without qualification means the spectrum of the linear map of left multiplication, computed as a complex spectrum by complexifying that real operator; because the algebra is commutative and the coefficients are complex, the intrinsic spectrum with scalars in $\mathbb{C}$ and the operator spectrum agree, and there is no separate quaternionic spectrum as in the split biquaternion case.

The treatment is mathematically honest: every claim is either proved or stated as a definition. The algebra, its idempotents and the decomposition $T=q_1\Pi_{1}+q_2\Pi_{2}$ are assumed from *Ideals and Peirce Decomposition of the General Plain Algebra of the Reduced Biquaternions*; the norm and the invertibility criterion from *Norm and Invertibility in the General Plain Algebra of the Reduced Biquaternions*; the elementary functions as needed from *Reduced Biquaternion Elementary Functions*. Throughout $T=A+Bj$ with $A=a+ia'$, $B=b+ib'$, the idempotent coordinates are $q_1=A+B$ and $q_2=A-B$, and the multiplication is componentwise.

## The Spectrum of an Element

**Definition.** The **spectrum** of $T$ is the set of complex $\lambda$ for which $\lambda L_{1}-L_{T}$ is not invertible, $L_{T}$ being the operator of left multiplication on the complex two-dimensional space $\mathbb{B}_{\mathrm{r}}$ with basis $1,j$. The element is **regular** as an element of the algebra when it is a unit, and **singular** otherwise.

**Theorem (the spectrum is the coordinate pair).** The characteristic polynomial of $L_{T}$ is
$$
\chi_{T}(\lambda)=\det(\lambda L_{1}-L_{T})=(\lambda-q_1)(\lambda-q_2)=\lambda^{2}-\operatorname{tr}(T)\,\lambda+\det(T),
$$
so
$$
\sigma(T)=\{q_1,q_2\},
$$
with the two values counted with multiplicity, where
$$
\operatorname{tr}(T)=q_1+q_2=2A,\qquad \det(T)=\langle T\rangle_{\natural}=q_1q_2=A^{2}-B^{2}
$$
are the **reduced trace** and the **reduced determinant**. The element is singular exactly when $0\in\sigma(T)$, that is when $q_1=0$ or $q_2=0$, which is the zero-divisor condition $\langle T\rangle_{\natural}=0$.

*Proof.* In the basis $1,j$ the matrix of $L_{T}$ is $\begin{smallmatrix}A&B\\ B&A\end{smallmatrix}$, whose characteristic polynomial is $(\lambda-A)^{2}-B^{2}=(\lambda-A-B)(\lambda-A+B)=(\lambda-q_1)(\lambda-q_2)$; the trace is $2A$ and the determinant $A^{2}-B^{2}=\langle T\rangle_{\natural}=q_1q_2$, and the algebra is commutative, so left and right multiplications coincide.

**Corollary (the diagonal model).** In the idempotent basis $\Pi_{1},\Pi_{2}$ the operator $L_{T}$ is diagonal,
$$
L_{T}=\operatorname{diag}(q_1,q_2),
$$
so the spectrum is read directly on the two coordinates and no triangular or Jordan structure appears.

*Proof.* $T\Pi_{1}=q_1\Pi_{1}$ and $T\Pi_{2}=q_2\Pi_{2}$, because the idempotents are orthogonal and $q_1,q_2$ are the two characters.

## Left and Right Eigenvalues

**Theorem (the two spectra coincide).** For every $T$, a vector $w$ is a left eigenvector with eigenvalue $\lambda$ if and only if it is a right eigenvector with the same eigenvalue; the left and the right spectra are equal to the spectrum $\sigma(T)$ of the preceding section.

*Proof.* The algebra is commutative, so $Tw=\lambda w$ and $wT=\lambda w$ are the same equation; and the right spectrum is the spectrum of right multiplication, whose matrix is the transpose of $\begin{smallmatrix}A&B\\ B&A\end{smallmatrix}$, with the same characteristic polynomial.

**Corollary (no asymmetry).** The asymmetry between the left and the right spectrum of the split biquaternion algebra, and the split between the left spectrum and the S-spectrum there, do not occur: the reduced biquaternion element has one spectrum, the coordinate pair, and it is the same for the left and the right action.

*Proof.* Commutativity makes the two actions identical, and the conjugate classes that distinguish the quaternionic spectra degenerate to single points in $\mathbb{C}$.

## Cayley–Hamilton and the Trace and Determinant Functionals

**Theorem (the reduced Cayley–Hamilton identity).** Every element satisfies
$$
T^{2}-\operatorname{tr}(T)\,T+\det(T)\,1=0,\qquad \operatorname{tr}(T)=2A,\quad \det(T)=\langle T\rangle_{\natural},
$$
and the same identity holds for the operator, $L_{T}^{2}-2A\,L_{T}+\langle T\rangle_{\natural}\,L_{1}=0$.

*Proof.* In the idempotent coordinates the left side is $q_1^{2}-(q_1+q_2)q_1+q_1q_2$ in the first component and $q_2^{2}-(q_1+q_2)q_2+q_1q_2$ in the second, both zero; the operator statement follows by applying the identity to the regular module.

**Theorem (additivity and multiplicativity).** The reduced trace is $\mathbb{C}$-linear and additive, $\operatorname{tr}(T+W)=\operatorname{tr}(T)+\operatorname{tr}(W)$; the reduced determinant is multiplicative, $\det(TW)=\det(T)\det(W)$; and $\det(T)$ vanishes exactly on the zero-divisor set.

*Proof.* $\operatorname{tr}(T)=2A$ is linear in the complex coordinate $A$; $\det(T)=\langle T\rangle_{\natural}=q_1q_2$ is multiplicative, the coordinates multiplying componentwise; and the vanishing of the product is the unit criterion.

**Corollary (the inverse).** On the complement of the zero-divisor set,
$$
T^{-1}=q_1^{-1}\Pi_{1}+q_2^{-1}\Pi_{2}=\frac{A-Bj}{\langle T\rangle_{\natural}},
$$
the second expression being the companion formula in the basis $1,j$.

*Proof.* The coordinate inverse $q_1^{-1}\Pi_{1}+q_2^{-1}\Pi_{2}$ multiplies $T=q_1\Pi_{1}+q_2\Pi_{2}$ to $\Pi_{1}+\Pi_{2}=1$; and $A-Bj=(A-B)\Pi_{1}+(A+B)\Pi_{2}=q_2\Pi_{1}+q_1\Pi_{2}$, whose product with $q_1^{-1}\Pi_{1}+q_2^{-1}\Pi_{2}$ is again $1$.

## Similarity and the Classification

**Definition.** Two elements are **similar**, written $T\sim S$, when $PTP^{-1}=S$ for some unit $P$.

**Theorem (the classification).** $T\sim S$ if and only if $q_{1,T}=q_{1,S}$ and $q_{2,T}=q_{2,S}$, that is if and only if the two elements have the same reduced trace and the same reduced determinant. The similarity classes are therefore the ordered pairs $(q_1,q_2)\in\mathbb{C}^{2}$, and there is no Jordan pathology: every element is diagonal, and the only nilpotent element is $0$.

*Proof.* A unit $P$ has coordinates $(p,q)$ with $p,q\neq0$ and conjugates $T$ to $(pu p^{-1},qv q^{-1})=(q_1,q_2)$, so similarity does not change the coordinates; conversely, if the coordinates agree, the identity is a conjugating unit. No permutation of the two coordinates is induced by a unit, since the unit group acts diagonally, so the pair is ordered. Finally $T^{n}=q_1^{n}\Pi_{1}+q_2^{n}\Pi_{2}$, which vanishes for some $n$ exactly when $q_1=q_2=0$.

**Corollary (the commutant).** The centraliser of a non-scalar element $T$, that is the set of $W$ with $TW=WT$, is the whole algebra, since the algebra is commutative; and the automorphisms of the algebra act on the coordinates by the idempotent-preserving involutions rather than by an inner action.

*Proof.* Commutativity makes every element commute with every other; the automorphisms act on the pair $(q_1,q_2)$ by the swaps and conjugations induced by the bar, the natural sign and the star, described in *The Two Involutions and the Group of Involutions*.

## Eigenspaces and Their Dimensions

**Theorem (the eigenspaces).** If $q_1\neq q_2$, the eigenvalue $q_1$ has the one-dimensional eigenspace $\mathbb{C}\Pi_{1}$ and the eigenvalue $q_2$ the one-dimensional eigenspace $\mathbb{C}\Pi_{2}$, each of complex dimension one, and the two span the algebra. If $q_1=q_2$, that is if $B=0$ and $T=A\cdot1$, then $T$ is the scalar $A$, the spectrum is the single value $A$ with multiplicity two, and the eigenspace is the whole algebra.

*Proof.* $T\Pi_{1}=q_1\Pi_{1}$ and $T\Pi_{2}=q_2\Pi_{2}$, and the two idempotent lines are the coordinate axes; when $q_1=q_2$ the operator $L_{T}$ is the scalar $A$ and every vector is an eigenvector.

**Corollary (the spectral projections).** The spectral projection onto the eigenspace of $q_1$ is $\Pi_{1}$ and onto that of $q_2$ is $\Pi_{2}$, and they are the idempotents of the algebra. The **minimal polynomial** of $T$ is $(\lambda-q_1)(\lambda-q_2)$ when $q_1\neq q_2$ and $\lambda-q_1$ when $q_1=q_2$, that is the product of the distinct linear factors of the characteristic polynomial.

*Proof.* The projections are the coordinate projections of the Peirce decomposition, and the minimal polynomial is the product of the distinct linear factors of the characteristic polynomial.

## The Resolvent

**Definition.** For $\lambda\notin\sigma(T)$ the **resolvent** is $R(\lambda,T)=(\lambda L_{1}-L_{T})^{-1}$, read on the algebra as $(\lambda-T)^{-1}$.

**Theorem (the closed form and the identity).** The resolvent is
$$
R(\lambda,T)=\frac{\Pi_{1}}{\lambda-q_1}+\frac{\Pi_{2}}{\lambda-q_2},
$$
it is analytic in $\lambda$ on the complement of the two points $q_1,q_2$, and it satisfies the resolvent identity $R(\lambda,T)-R(\mu,T)=(\mu-\lambda)R(\lambda,T)R(\mu,T)$.

*Proof.* In the idempotent basis the operator is diagonal with diagonal entries $\lambda-q_1$ and $\lambda-q_2$, and the inverse is diagonal with the reciprocal entries; the identity is algebra in the commutative algebra.

**Corollary (the resolvent at infinity).** For large $\lambda$ one has $R(\lambda,T)=\lambda^{-1}1+\lambda^{-2}T+\lambda^{-3}T^{2}+\cdots$, the Neumann series of the algebra, convergent for $|\lambda|>\rho(T)$.

*Proof.* Expanding $(\lambda-T)^{-1}=\lambda^{-1}(1-T/\lambda)^{-1}$ and summing the geometric series in the finite-dimensional commutative algebra gives the displayed series, which converges for $|\lambda|>\rho(T)$ and sums to the closed form $(\lambda-q_1)^{-1}\Pi_{1}+(\lambda-q_2)^{-1}\Pi_{2}$; the terms satisfy the recurrence $T^{n+1}=\operatorname{tr}(T)T^{n}-\det(T)T^{n-1}$ read from Cayley–Hamilton, so the series is that of the two geometric series in the coordinates.

## The Spectral Radius

**Definition.** The **spectral radius** of $T$ is $\rho(T)=\max\{|\lambda|:\lambda\in\sigma(T)\}$.

**Theorem (the value and the operator norm).** $\rho(T)=\max(|q_1|,|q_2|)$; it equals the operator norm of $L_{T}$ for the Euclidean norm of the algebra, $\rho(T)=\lVert L_{T}\rVert$; it vanishes exactly at $T=0$; and it is bounded by the two coordinates through
$$
\frac{\lvert q_1\rvert^{2}+\lvert q_2\rvert^{2}}{4}\le\rho(T)^{2}\le\lvert q_1\rvert^{2}+\lvert q_2\rvert^{2}.
$$

*Proof.* The operator is diagonal with entries $q_1,q_2$, so its norm and its spectral radius are both the maximum of the two moduli; the vanishing of the maximum forces both coordinates to zero, hence $T=0$, the algebra having no non-zero nilpotent. The left inequality compares the maximum with twice the mean and the right compares it with the sum of squares, and $\lvert q_1\rvert^{2}+\lvert q_2\rvert^{2}=2K(T)$.

**Corollary (the Gelfand formula is finite).** Because the powers are $T^{n}=q_1^{n}\Pi_{1}+q_2^{n}\Pi_{2}$ and obey the two-term recurrence $T^{n+2}=\operatorname{tr}(T)\,T^{n+1}-\det(T)\,T^{n}$ of Cayley–Hamilton, the Gelfand limit is the maximum of the two moduli,
$$
\rho(T)=\lim_{n}\lVert T^{n}\rVert^{1/n}=\max\bigl(\lvert q_1\rvert,\lvert q_2\rvert\bigr),
$$
computed from the two coordinates alone, and there is no nilpotent block.

*Proof.* Cayley–Hamilton gives the recurrence for the powers, whence the closed form $T^{n}=q_1^{n}\Pi_{1}+q_2^{n}\Pi_{2}$; with $\lVert T^{n}\rVert=\sqrt{\tfrac12(\lvert q_1\rvert^{2n}+\lvert q_2\rvert^{2n})}$ the $n$-th root tends to $\max(\lvert q_1\rvert,\lvert q_2\rvert)$ as $n\to\infty$, the larger of the two powers dominating.

## The Exponential and the Logarithm

**Theorem (the exponential).** The exponential is componentwise,
$$
\exp T=e^{q_1}\Pi_{1}+e^{q_2}\Pi_{2},
$$
it maps the algebra into the unit group, and the reduced determinant is $\det(\exp T)=e^{q_1+q_2}=e^{\operatorname{tr}(T)}$. The exponential is never zero, so every element of the image is a unit; it is not injective, its kernel being the elements with $q_1,q_2\in2\pi i\mathbb{Z}$.

*Proof.* The exponential of a diagonal operator is diagonal with the exponentials of the entries, and the coordinates are the characters, so $\exp(T)$ has coordinates $e^{q_1},e^{q_2}$; the determinant is the product, $e^{q_1}e^{q_2}=e^{q_1+q_2}$; the kernel is the preimage of $1$, that is $e^{q_1}=e^{q_2}=1$.

**Theorem (the logarithm).** An element $T$ has a logarithm, that is a solution of $\exp S=T$, if and only if it is a unit, and then
$$
\log T=\log q_1\,\Pi_{1}+\log q_2\,\Pi_{2}
$$
for a choice of the two complex branches; the solution is determined modulo the kernel, which is $2\pi i\,\mathbb{Z}^{2}$ read in the two coordinates.

*Proof.* Each coordinate equation $e^{s}=q_1$ has a solution exactly when $q_1\neq0$, and the solutions differ by $2\pi i$; the two coordinates decouple.

## The Relation to the Biquaternion and Split-Biquaternion Spectral Theories

The biquaternion algebra $\mathbb{B}=M_{2}(\mathbb{C})$ is simple, with a single complex eigenvalue of multiplicity two for a generic element and the S-spectrum to repair the failure of the naive definition. The split biquaternion algebra $\mathbb{H}_{\mathbb{D}}\cong\mathbb{H}\oplus\mathbb{H}$ has a four-value complex spectrum $\{q_{0}^{+}\pm i|\vec Q_{+}|\}\cup\{q_{0}^{-}\pm i|\vec Q_{-}|\}$ with doubled multiplicities, a quaternionic left spectrum $\{\tilde Q_{+},\tilde Q_{-}\}$ and a right spectrum that is a union of two conjugacy classes. The reduced biquaternion algebra is the commutative case: the spectrum is the two complex coordinates $q_1,q_2$ with multiplicity one, the left and the right spectra coincide, the reduced trace and determinant are $\mathbb{C}$-valued and are the ordinary trace and determinant of the diagonal model, the Cayley–Hamilton identity is the ordinary one, and the resolvent is the pair of one-variable resolvents. What is lost against the quaternion cases is the conjugate-class structure; what is gained is that the two coordinates classify the element completely, with no Jordan blocks and no nilpotents beyond $0$.

## Summary

The reduced biquaternion element $T$ has the spectrum $\sigma(T)=\{q_1,q_2\}$, the pair of its idempotent coordinates, which are the eigenvalues of left multiplication in the basis $1,j$ with matrix $\begin{smallmatrix}A&B\\ B&A\end{smallmatrix}$. Left and right eigenvalues coincide, because the algebra is commutative, and the intrinsic spectrum over $\mathbb{C}$ is the operator spectrum; there is no quaternionic or S-spectrum. The reduced trace $\operatorname{tr}(T)=2A=q_1+q_2$ is additive and the reduced determinant $\det(T)=\langle T\rangle_{\natural}=q_1q_2$ is multiplicative and vanishes exactly on the zero-divisor set, and Cayley–Hamilton reads $T^{2}-\operatorname{tr}(T)T+\det(T)1=0$, the minimal polynomial having degree at most two. Similarity changes neither coordinate, so the classes are the ordered pairs $(q_1,q_2)$; the eigenspaces are the two idempotent lines when $q_1\neq q_2$ and the whole algebra when $T$ is a scalar; the resolvent is $(\lambda-q_1)^{-1}\Pi_{1}+(\lambda-q_2)^{-1}\Pi_{2}$, analytic off the two points and satisfying the resolvent identity; and the spectral radius is $\max(|q_1|,|q_2|)$, equal to the operator norm of left multiplication and vanishing only at $0$, there being no non-zero nilpotent. The exponential is $e^{q_1}\Pi_{1}+e^{q_2}\Pi_{2}$, its determinant is $e^{\operatorname{tr}(T)}$, and the logarithm exists exactly on the units for a branch choice in each coordinate. Against the biquaternion and split biquaternion theories the finite complex spectrum, the field-valued trace and determinant and the diagonal model replace the S-spectrum, the quaternionic trace and norm functionals and the conjugate-class structure, the whole theory being the pair of the complex one-variable spectral theories of the two coordinates.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_{T}$ | Operator of left multiplication by $T$ |
| $q_1=A+B$, $q_2=A-B$ | Idempotent coordinates, the eigenvalues |
| $\sigma(T)=\{q_1,q_2\}$ | Spectrum |
| $\operatorname{tr}(T)=2A=q_1+q_2$ | Reduced trace |
| $\det(T)=\langle T\rangle_{\natural}=q_1q_2=A^{2}-B^{2}$ | Reduced determinant |
| $\chi_{T}(\lambda)=\lambda^{2}-\operatorname{tr}(T)\lambda+\det(T)$ | Characteristic polynomial |
| $R(\lambda,T)=(\lambda-q_1)^{-1}\Pi_{1}+(\lambda-q_2)^{-1}\Pi_{2}$ | Resolvent |
| $\rho(T)=\max(|q_1|,|q_2|)$ | Spectral radius |
| $\exp T=e^{q_1}\Pi_{1}+e^{q_2}\Pi_{2}$ | Exponential |
| $\log T=\log q_1\,\Pi_{1}+\log q_2\,\Pi_{2}$ | Logarithm on the units |

## Further Reading

- F. F. Bonsall and J. Duncan, *Complete Normed Algebras* (Springer, 1973), for the spectral theory of elements and operators in a commutative Banach algebra.
- W. Rudin, *Functional Analysis*, 2nd edition (McGraw-Hill, 1991), for the resolvent, the spectral radius and the Gelfand theory.
- G. Baley Price, *An Introduction to Multicomplex Spaces and Functions* (Marcel Dekker, 1991), for the trace, the norm and the idempotent decomposition of the multicomplex algebra.
- M. Elena Luna-Elizarrarás, Michael Shapiro, Daniele C. Struppa and Adrian Vajiac, *Bicomplex Holomorphic Functions* (Birkhäuser, 2015), for the holomorphic functional calculus and the spectral properties of the commutative algebra.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the trace, the determinant and the Cayley–Hamilton theorem in a finite-dimensional algebra.
