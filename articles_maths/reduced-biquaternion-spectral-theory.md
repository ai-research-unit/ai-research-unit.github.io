# __Reduced Biquaternion Spectral Theory__

## Introduction

The reduced biquaternion algebra $\mathbb{B}_{\mathrm{r}}\cong\mathbb{C}\times\mathbb{C}$ is commutative, associative and unital, and it is **not** a division algebra; both facts simplify the spectral theory and separate it from the two non-commutative members of the family. In this article **spectrum** without qualification means the spectrum of the linear map of left multiplication, computed as a complex spectrum by complexifying that real operator; because the algebra is commutative and the coefficients are complex, the intrinsic spectrum with scalars in $\mathbb{C}$ and the operator spectrum agree, and there is no separate quaternionic spectrum as in the split biquaternion case.

The treatment is mathematically honest: every claim is either proved or stated as a definition. The algebra, its idempotents and the decomposition $Q_\pm=Q_{++}\Pi_++Q_{--}\Pi_-$ are assumed from *Ideals and Peirce Decomposition of the Algebra of the Reduced Biquaternions*; the norm and the invertibility criterion from *Norm and Invertibility in the Algebra of the Reduced Biquaternions*; the elementary functions as needed from *Reduced Biquaternion Elementary Functions*. Throughout $Q_\pm=Q_++jQ_-$ with $Q_+=q_++iq'_+$, $Q_-=q_-+iq'_-$, the idempotent coordinates are $Q_{++}=Q_++Q_-$ and $Q_{--}=Q_+-Q_-$, and the multiplication is componentwise.

## The Spectrum of an Element

**Definition.** The **spectrum** of $Q_\pm$ is the set of complex $\lambda$ for which $\lambda L_{1}-L_{Q_\pm}$ is not invertible, $L_{Q_\pm}$ being the operator of left multiplication on the complex two-dimensional space $\mathbb{B}_{\mathrm{r}}$ with basis $1,j$. The element is **regular** as an element of the algebra when it is a unit, and **singular** otherwise.

**Theorem (the spectrum is the coordinate pair).** The characteristic polynomial of $L_{Q_\pm}$ is
$$
\chi_{Q_\pm}(\lambda)=\det(\lambda L_{1}-L_{Q_\pm})=(\lambda-Q_{++})(\lambda-Q_{--})=\lambda^{2}-\operatorname{tr}(Q_\pm)\,\lambda+\det(Q_\pm),
$$
so
$$
\sigma(Q_\pm)=\{Q_{++},Q_{--}\},
$$
with the two values counted with multiplicity, where
$$
\operatorname{tr}(Q_\pm)=Q_{++}+Q_{--}=2Q_+,\qquad \det(Q_\pm)=\langle Q_\pm\rangle_{\natural}=Q_{++}Q_{--}=Q_+^{2}-Q_-^{2}
$$
are the **reduced trace** and the **reduced determinant**. The element is singular exactly when $0\in\sigma(Q_\pm)$, that is when $Q_{++}=0$ or $Q_{--}=0$, which is the zero-divisor condition $\langle Q_\pm\rangle_{\natural}=0$.

*Proof.* In the basis $1,j$ the matrix of $L_{Q_\pm}$ is $\begin{smallmatrix}Q_+&Q_-\\ Q_-&Q_+\end{smallmatrix}$, whose characteristic polynomial is $(\lambda-Q_+)^{2}-Q_-^{2}=(\lambda-Q_+-Q_-)(\lambda-Q_++Q_-)=(\lambda-Q_{++})(\lambda-Q_{--})$; the trace is $2Q_+$ and the determinant $Q_+^{2}-Q_-^{2}=\langle Q_\pm\rangle_{\natural}=Q_{++}Q_{--}$, and the algebra is commutative, so left and right multiplications coincide.

**Corollary (the diagonal model).** In the idempotent basis $\Pi_+,\Pi_-$ the operator $L_{Q_\pm}$ is diagonal,
$$
L_{Q_\pm}=\operatorname{diag}(Q_{++},Q_{--}),
$$
so the spectrum is read directly on the two coordinates and no triangular or Jordan structure appears.

*Proof.* $Q_\pm\Pi_+=Q_{++}\Pi_+$ and $Q_\pm\Pi_-=Q_{--}\Pi_-$, because the idempotents are orthogonal and $Q_{++},Q_{--}$ are the two characters.

## Left and Right Eigenvalues

**Theorem (the two spectra coincide).** For every $Q_\pm$, a vector $w$ is a left eigenvector with eigenvalue $\lambda$ if and only if it is a right eigenvector with the same eigenvalue; the left and the right spectra are equal to the spectrum $\sigma(Q_\pm)$ of the preceding section.

*Proof.* The algebra is commutative, so $Q_\pm w=\lambda w$ and $wQ_\pm=\lambda w$ are the same equation; and the right spectrum is the spectrum of right multiplication, whose matrix is the transpose of $\begin{smallmatrix}Q_+&Q_-\\ Q_-&Q_+\end{smallmatrix}$, with the same characteristic polynomial.

**Corollary (no asymmetry).** The asymmetry between the left and the right spectrum of the split biquaternion algebra, and the split between the left spectrum and the S-spectrum there, do not occur: the reduced biquaternion element has one spectrum, the coordinate pair, and it is the same for the left and the right action.

*Proof.* Commutativity makes the two actions identical, and the conjugate classes that distinguish the quaternionic spectra degenerate to single points in $\mathbb{C}$.

## Cayley–Hamilton and the Trace and Determinant Functionals

**Theorem (the reduced Cayley–Hamilton identity).** Every element satisfies
$$
Q_\pm^{2}-\operatorname{tr}(Q_\pm)\,Q_\pm+\det(Q_\pm)\,1=0,\qquad \operatorname{tr}(Q_\pm)=2Q_+,\quad \det(Q_\pm)=\langle Q_\pm\rangle_{\natural},
$$
and the same identity holds for the operator, $L_{Q_\pm}^{2}-2Q_+\,L_{Q_\pm}+\langle Q_\pm\rangle_{\natural}\,L_{1}=0$.

*Proof.* In the idempotent coordinates the left side is $Q_{++}^{2}-(Q_{++}+Q_{--})Q_{++}+Q_{++}Q_{--}$ in the first component and $Q_{--}^{2}-(Q_{++}+Q_{--})Q_{--}+Q_{++}Q_{--}$ in the second, both zero; the operator statement follows by applying the identity to the regular module.

**Theorem (additivity and multiplicativity).** The reduced trace is $\mathbb{C}$-linear and additive, $\operatorname{tr}(Q_{\pm,1}+Q_{\pm,2})=\operatorname{tr}(Q_{\pm,1})+\operatorname{tr}(Q_{\pm,2})$; the reduced determinant is multiplicative, $\det(Q_{\pm,1}Q_{\pm,2})=\det(Q_{\pm,1})\det(Q_{\pm,2})$; and $\det(Q_\pm)$ vanishes exactly on the zero-divisor set.

*Proof.* $\operatorname{tr}(Q_\pm)=2Q_+$ is linear in the complex coordinate $Q_+$; $\det(Q_\pm)=\langle Q_\pm\rangle_{\natural}=Q_{++}Q_{--}$ is multiplicative, the coordinates multiplying componentwise; and the vanishing of the product is the unit criterion.

**Corollary (the inverse).** On the complement of the zero-divisor set,
$$
Q_\pm^{-1}=Q_{++}^{-1}\Pi_++Q_{--}^{-1}\Pi_-=\frac{Q_+-jQ_-}{\langle Q_\pm\rangle_{\natural}},
$$
the second expression being the companion formula in the basis $1,j$.

*Proof.* The coordinate inverse $Q_{++}^{-1}\Pi_++Q_{--}^{-1}\Pi_-$ multiplies $Q_\pm=Q_{++}\Pi_++Q_{--}\Pi_-$ to $\Pi_++\Pi_-=1$; and $Q_+-jQ_-=(Q_+-Q_-)\Pi_++(Q_++Q_-)\Pi_-=Q_{--}\Pi_++Q_{++}\Pi_-$, whose product with $Q_{++}^{-1}\Pi_++Q_{--}^{-1}\Pi_-$ is again $1$.

## Similarity and the Classification

**Definition.** Two elements are **similar**, written $Q_{\pm,1}\sim Q_{\pm,2}$, when $PQ_{\pm,1}P^{-1}=Q_{\pm,2}$ for some unit $P$.

**Theorem (the classification).** $Q_{\pm,1}\sim Q_{\pm,2}$ if and only if $Q_{1++}=Q_{2++}$ and $Q_{1--}=Q_{2--}$, that is if and only if the two elements have the same ordered pair of idempotent coordinates; the reduced trace and the reduced determinant alone fix only the unordered pair. The similarity classes are therefore the ordered pairs $(Q_{++},Q_{--})\in\mathbb{C}^{2}$, and there is no Jordan pathology: every element is diagonal, and the only nilpotent element is $0$.

*Proof.* A unit $P$ has coordinates $(p,q)$ with $p,q\neq0$ and conjugates $Q_{\pm,1}$ to $(pQ_{1++}p^{-1},qQ_{1--}q^{-1})=(Q_{1++},Q_{1--})$, so similarity does not change the coordinates; conversely, if the coordinates agree, the identity is a conjugating unit. No permutation of the two coordinates is induced by a unit, since the unit group acts diagonally, so the pair is ordered. Finally $Q_\pm^{n}=Q_{++}^{n}\Pi_++Q_{--}^{n}\Pi_-$, which vanishes for some $n$ exactly when $Q_{++}=Q_{--}=0$.

**Corollary (the commutant).** The centraliser of a non-scalar element $Q_\pm$, that is the set of $Q_{\pm,2}$ with $Q_\pm Q_{\pm,2}=Q_{\pm,2}Q_\pm$, is the whole algebra, since the algebra is commutative; and the automorphisms of the algebra act on the coordinates by the permutations and the coordinatewise conjugations rather than by an inner action.

*Proof.* Commutativity makes every element commute with every other; the automorphisms act on the pair $(Q_{++},Q_{--})$ by the swaps and conjugations induced by the bar, the natural sign and the star, described in *The Two Involutions and the Group of Involutions*.

## Eigenspaces and Their Dimensions

**Theorem (the eigenspaces).** If $Q_{++}\neq Q_{--}$, the eigenvalue $Q_{++}$ has the one-dimensional eigenspace $\mathbb{C}\Pi_+$ and the eigenvalue $Q_{--}$ the one-dimensional eigenspace $\mathbb{C}\Pi_-$, each of complex dimension one, and the two span the algebra. If $Q_{++}=Q_{--}$, that is if $Q_-=0$ and $Q_\pm=Q_+\cdot1$, then $Q_\pm$ is the scalar $Q_+$, the spectrum is the single value $Q_+$ with multiplicity two, and the eigenspace is the whole algebra.

*Proof.* $Q_\pm\Pi_+=Q_{++}\Pi_+$ and $Q_\pm\Pi_-=Q_{--}\Pi_-$, and the two idempotent lines are the coordinate axes; when $Q_{++}=Q_{--}$ the operator $L_{Q_\pm}$ is the scalar $Q_+$ and every vector is an eigenvector.

**Corollary (the spectral projections).** The spectral projection onto the eigenspace of $Q_{++}$ is $\Pi_+$ and onto that of $Q_{--}$ is $\Pi_-$, and they are the idempotents of the algebra. The **minimal polynomial** of $Q_\pm$ is $(\lambda-Q_{++})(\lambda-Q_{--})$ when $Q_{++}\neq Q_{--}$ and $\lambda-Q_{++}$ when $Q_{++}=Q_{--}$, that is the product of the distinct linear factors of the characteristic polynomial.

*Proof.* The projections are the coordinate projections of the Peirce decomposition, and the minimal polynomial is the product of the distinct linear factors of the characteristic polynomial.

## The Resolvent

**Definition.** For $\lambda\notin\sigma(Q_\pm)$ the **resolvent** is $R(\lambda,Q_\pm)=(\lambda L_{1}-L_{Q_\pm})^{-1}$, read on the algebra as $(\lambda-Q_\pm)^{-1}$.

**Theorem (the closed form and the identity).** The resolvent is
$$
R(\lambda,Q_\pm)=\frac{\Pi_+}{\lambda-Q_{++}}+\frac{\Pi_-}{\lambda-Q_{--}},
$$
it is analytic in $\lambda$ on the complement of the two points $Q_{++},Q_{--}$, and it satisfies the resolvent identity $R(\lambda,Q_\pm)-R(\mu,Q_\pm)=(\mu-\lambda)R(\lambda,Q_\pm)R(\mu,Q_\pm)$.

*Proof.* In the idempotent basis the operator is diagonal with diagonal entries $\lambda-Q_{++}$ and $\lambda-Q_{--}$, and the inverse is diagonal with the reciprocal entries; the identity is algebra in the commutative algebra.

**Corollary (the resolvent at infinity).** For large $\lambda$ one has $R(\lambda,Q_\pm)=\lambda^{-1}1+\lambda^{-2}Q_\pm+\lambda^{-3}Q_\pm^{2}+\cdots$, the Neumann series of the algebra, convergent for $|\lambda|>\rho(Q_\pm)$.

*Proof.* Expanding $(\lambda-Q_\pm)^{-1}=\lambda^{-1}(1-Q_\pm/\lambda)^{-1}$ and summing the geometric series in the finite-dimensional commutative algebra gives the displayed series, which converges for $|\lambda|>\rho(Q_\pm)$ and sums to the closed form $(\lambda-Q_{++})^{-1}\Pi_++(\lambda-Q_{--})^{-1}\Pi_-$; the terms satisfy the recurrence $Q_\pm^{n+1}=\operatorname{tr}(Q_\pm)Q_\pm^{n}-\det(Q_\pm)Q_\pm^{n-1}$ read from Cayley–Hamilton, so the series is that of the two geometric series in the coordinates.

## The Spectral Radius

**Definition.** The **spectral radius** of $Q_\pm$ is $\rho(Q_\pm)=\max\{|\lambda|:\lambda\in\sigma(Q_\pm)\}$.

**Theorem (the value and the operator norm).** $\rho(Q_\pm)=\max(\lvert Q_{++}\rvert,\lvert Q_{--}\rvert)$; it equals the operator norm of $L_{Q_\pm}$ for the Euclidean norm of the algebra, $\rho(Q_\pm)=\lVert L_{Q_\pm}\rVert$; it vanishes exactly at $Q_\pm=0$; and it is bounded by the two coordinates through
$$
\frac{\lvert Q_{++}\rvert^{2}+\lvert Q_{--}\rvert^{2}}{4}\le\rho(Q_\pm)^{2}\le\lvert Q_{++}\rvert^{2}+\lvert Q_{--}\rvert^{2}.
$$

*Proof.* The operator is diagonal with entries $Q_{++},Q_{--}$, so its norm and its spectral radius are both the maximum of the two moduli; the vanishing of the maximum forces both coordinates to zero, hence $Q_\pm=0$, the algebra having no non-zero nilpotent. The left inequality compares the maximum with twice the mean and the right compares it with the sum of squares, and $\lvert Q_{++}\rvert^{2}+\lvert Q_{--}\rvert^{2}=2K(Q_\pm)$.

**Corollary (the Gelfand formula is finite).** Because the powers are $Q_\pm^{n}=Q_{++}^{n}\Pi_++Q_{--}^{n}\Pi_-$ and obey the two-term recurrence $Q_\pm^{n+2}=\operatorname{tr}(Q_\pm)\,Q_\pm^{n+1}-\det(Q_\pm)\,Q_\pm^{n}$ of Cayley–Hamilton, the Gelfand limit is the maximum of the two moduli,
$$
\rho(Q_\pm)=\lim_{n}\lVert Q_\pm^{n}\rVert^{1/n}=\max\bigl(\lvert Q_{++}\rvert,\lvert Q_{--}\rvert\bigr),
$$
computed from the two coordinates alone, and there is no nilpotent block.

*Proof.* Cayley–Hamilton gives the recurrence for the powers, whence the closed form $Q_\pm^{n}=Q_{++}^{n}\Pi_++Q_{--}^{n}\Pi_-$; with $\lVert Q_\pm^{n}\rVert=\sqrt{\tfrac12(\lvert Q_{++}\rvert^{2n}+\lvert Q_{--}\rvert^{2n})}$ the $n$-th root tends to $\max(\lvert Q_{++}\rvert,\lvert Q_{--}\rvert)$ as $n\to\infty$, the larger of the two powers dominating.

## The Exponential and the Logarithm

**Theorem (the exponential).** The exponential is componentwise,
$$
\exp Q_\pm=e^{Q_{++}}\Pi_++e^{Q_{--}}\Pi_-,
$$
it maps the algebra into the unit group, and the reduced determinant is $\det(\exp Q_\pm)=e^{Q_{++}+Q_{--}}=e^{\operatorname{tr}(Q_\pm)}$. The exponential is never zero, so every element of the image is a unit; it is not injective, its kernel being the elements with $Q_{++},Q_{--}\in2\pi i\mathbb{Z}$.

*Proof.* The exponential of a diagonal operator is diagonal with the exponentials of the entries, and the coordinates are the characters, so $\exp(Q_\pm)$ has coordinates $e^{Q_{++}},e^{Q_{--}}$; the determinant is the product, $e^{Q_{++}}e^{Q_{--}}=e^{Q_{++}+Q_{--}}$; the kernel is the preimage of $1$, that is $e^{Q_{++}}=e^{Q_{--}}=1$.

**Theorem (the logarithm).** An element $Q_\pm$ has a logarithm, that is a solution of $\exp Q_{\pm,2}=Q_\pm$, if and only if it is a unit, and then
$$
\log Q_\pm=\log Q_{++}\,\Pi_++\log Q_{--}\,\Pi_-
$$
for a choice of the two complex branches; the solution is determined modulo the kernel, which is $2\pi i\,\mathbb{Z}^{2}$ read in the two coordinates.

*Proof.* Each coordinate equation $e^{s}=Q_{++}$ has a solution exactly when $Q_{++}\neq0$, and the solutions differ by $2\pi i$; the two coordinates decouple.

## The Relation to the Biquaternion and Split-Biquaternion Spectral Theories

The biquaternion algebra $\mathbb{B}=M_{2}(\mathbb{C})$ is simple, with a single complex eigenvalue of multiplicity two for a generic element and the S-spectrum to repair the failure of the naive definition. The split biquaternion algebra $\mathbb{H}_{\mathbb{D}}\cong\mathbb{H}\oplus\mathbb{H}$ has a four-value complex spectrum $\{q_{0}^{+}\pm i|\vec Q_{+}|\}\cup\{q_{0}^{-}\pm i|\vec Q_{-}|\}$ with doubled multiplicities, a quaternionic left spectrum $\{\tilde Q_{+},\tilde Q_{-}\}$ and a right spectrum that is a union of two conjugacy classes. The reduced biquaternion algebra is the commutative case: the spectrum is the two complex coordinates $Q_{++},Q_{--}$ with multiplicity one, the left and the right spectra coincide, the reduced trace and determinant are $\mathbb{C}$-valued and are the ordinary trace and determinant of the diagonal model, the Cayley–Hamilton identity is the ordinary one, and the resolvent is the pair of one-variable resolvents. What is lost against the quaternion cases is the conjugate-class structure; what is gained is that the two coordinates classify the element completely, with no Jordan blocks and no nilpotents beyond $0$.

## Summary

The reduced biquaternion element $Q_\pm$ has the spectrum $\sigma(Q_\pm)=\{Q_{++},Q_{--}\}$, the pair of its idempotent coordinates, which are the eigenvalues of left multiplication in the basis $1,j$ with matrix $\begin{smallmatrix}Q_+&Q_-\\ Q_-&Q_+\end{smallmatrix}$. Left and right eigenvalues coincide, because the algebra is commutative, and the intrinsic spectrum over $\mathbb{C}$ is the operator spectrum; there is no quaternionic or S-spectrum. The reduced trace $\operatorname{tr}(Q_\pm)=2Q_+=Q_{++}+Q_{--}$ is additive and the reduced determinant $\det(Q_\pm)=\langle Q_\pm\rangle_{\natural}=Q_{++}Q_{--}$ is multiplicative and vanishes exactly on the zero-divisor set, and Cayley–Hamilton reads $Q_\pm^{2}-\operatorname{tr}(Q_\pm)Q_\pm+\det(Q_\pm)1=0$, the minimal polynomial having degree at most two. Similarity changes neither coordinate, so the classes are the ordered pairs $(Q_{++},Q_{--})$; the eigenspaces are the two idempotent lines when $Q_{++}\neq Q_{--}$ and the whole algebra when $Q_\pm$ is a scalar; the resolvent is $(\lambda-Q_{++})^{-1}\Pi_++(\lambda-Q_{--})^{-1}\Pi_-$, analytic off the two points and satisfying the resolvent identity; and the spectral radius is $\max(|Q_{++}|,|Q_{--}|)$, equal to the operator norm of left multiplication and vanishing only at $0$, there being no non-zero nilpotent. The exponential is $e^{Q_{++}}\Pi_++e^{Q_{--}}\Pi_-$, its determinant is $e^{\operatorname{tr}(Q_\pm)}$, and the logarithm exists exactly on the units for a branch choice in each coordinate. Against the biquaternion and split biquaternion theories the finite complex spectrum, the field-valued trace and determinant and the diagonal model replace the S-spectrum, the quaternionic trace and norm functionals and the conjugate-class structure, the whole theory being the pair of the complex one-variable spectral theories of the two coordinates.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_{Q_\pm}$ | Operator of left multiplication by $Q_\pm$ |
| $Q_{++}=Q_++Q_-$, $Q_{--}=Q_+-Q_-$ | Idempotent coordinates, the eigenvalues |
| $\sigma(Q_\pm)=\{Q_{++},Q_{--}\}$ | Spectrum |
| $\operatorname{tr}(Q_\pm)=2Q_+=Q_{++}+Q_{--}$ | Reduced trace |
| $\det(Q_\pm)=\langle Q_\pm\rangle_{\natural}=Q_{++}Q_{--}=Q_+^{2}-Q_-^{2}$ | Reduced determinant |
| $\chi_{Q_\pm}(\lambda)=\lambda^{2}-\operatorname{tr}(Q_\pm)\lambda+\det(Q_\pm)$ | Characteristic polynomial |
| $R(\lambda,Q_\pm)=(\lambda-Q_{++})^{-1}\Pi_++(\lambda-Q_{--})^{-1}\Pi_-$ | Resolvent |
| $\rho(Q_\pm)=\max(\lvert Q_{++}\rvert,\lvert Q_{--}\rvert)$ | Spectral radius |
| $\exp Q_\pm=e^{Q_{++}}\Pi_++e^{Q_{--}}\Pi_-$ | Exponential |
| $\log Q_\pm=\log Q_{++}\,\Pi_++\log Q_{--}\,\Pi_-$ | Logarithm on the units |

## Further Reading

- F. F. Bonsall and J. Duncan, *Complete Normed Algebras* (Springer, 1973), for the spectral theory of elements and operators in a commutative Banach algebra.
- W. Rudin, *Functional Analysis*, 2nd edition (McGraw-Hill, 1991), for the resolvent, the spectral radius and the Gelfand theory.
- G. Baley Price, *An Introduction to Multicomplex Spaces and Functions* (Marcel Dekker, 1991), for the trace, the norm and the idempotent decomposition of the multicomplex algebra.
- M. Elena Luna-Elizarrarás, Michael Shapiro, Daniele C. Struppa and Adrian Vajiac, *Bicomplex Holomorphic Functions* (Birkhäuser, 2015), for the holomorphic functional calculus and the spectral properties of the commutative algebra.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the trace, the determinant and the Cayley–Hamilton theorem in a finite-dimensional algebra.
