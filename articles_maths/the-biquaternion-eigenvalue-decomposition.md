# __The Biquaternion Eigenvalue Decomposition__

## Introduction

The biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ is the Clifford algebra $\mathrm{Cl}_{3,0}$ in the dictionary of *The Number Systems as Clifford Algebras*: the quaternion units are the bivectors, the central scalar imaginary is the volume element, and the whole algebra is the complex $2\times2$ matrix algebra. The **eigenvalue decomposition** of a biquaternion is therefore an instance of *The Eigenvalue Decomposition in a Clifford Algebra*, and it is the instance in which the non-scalar eigenvalue is **internal**: the imaginary unit that the eigenvalues involve is the volume element of the algebra itself, of grade $3$, not an external scalar adjoined to it.

A biquaternion $\tilde Q=Q_{t}e_{t}+\vec Q$ has the eigenvalue decomposition

$$
\tilde Q=\lambda_{+}\tilde\Pi_{+}+\lambda_{-}\tilde\Pi_{-},
\qquad
\lambda_{\pm}=Q_{t}\pm iB,
\qquad
B^{2}=Q_{x}^{2}+Q_{y}^{2}+Q_{z}^{2},
$$

with the two primitive idempotents $\tilde\Pi_{\pm}=\tfrac12(1\pm\vec\Xi)$ of the pure root $\vec\Xi=-i\vec Q/B$. In the Clifford reading, $i$ is the volume element $\omega$, the biquaternion vector part $\vec Q$ is a bivector, the root $\vec\Xi$ is a unit vector, and the idempotents are the standard vector idempotents of grades $0$ and $1$. The eigenvalues are central elements of grades $0$ and $3$. The article develops this reading, records the Peirce and spinor structure that it makes visible, and treats the two degenerate regimes.

The algebra and its four conjugations are from *The Biquaternion Algebra and Its Vector Spaces*; the spectrum, the characteristic polynomial and the spectral theorem are *Biquaternion Spectral Theory*; the roots of one and the idempotents are *Square Roots of One and the Idempotents of the Biquaternion Algebra*; the Peirce decomposition is *Ideals and Peirce Decomposition of the Biquaternion Algebra*; the eigenvalue decomposition in coordinates is *Eigenvalue Decomposition and Eigenbasis of a Biquaternion*; the Clifford dictionary is *The Number Systems as Clifford Algebras*, §*The Biquaternion Algebra*; the general Clifford theory is *The Eigenvalue Decomposition in a Clifford Algebra*; and the grade decomposition is *The Geometric Product and the Grade Decomposition*.

## The Clifford Dictionary

### The Generators and the Volume Element

Let $V=\mathbb{R}^{3}$ with the positive definite form $Q=\operatorname{diag}(1,1,1)$, and let $\gamma_{1},\gamma_{2},\gamma_{3}$ be the Clifford generators:

$$
\gamma_{\mu}^{2}=1, \qquad \gamma_{\mu}\gamma_{\nu}+\gamma_{\nu}\gamma_{\mu}=0 \quad (\mu\neq\nu).
$$

The volume element is

$$
\omega=\gamma_{1}\gamma_{2}\gamma_{3}, \qquad \omega^{2}=-1,
$$

and it is central because the dimension is odd. The isomorphism of *The Number Systems as Clifford Algebras*, §*The Biquaternion Algebra*, is

$$
\gamma_{\mu}\longmapsto i\vec e_{\mu},
$$

where $\vec e_{x},\vec e_{y},\vec e_{z}$ are the quaternion units and $i$ is the central scalar imaginary of $\mathbb{B}$. Under it,

$$
\omega=\gamma_{1}\gamma_{2}\gamma_{3}\longmapsto i^{3}\vec e_{x}\vec e_{y}\vec e_{z}=i,
$$

so the central imaginary unit of the biquaternions **is** the volume element. The inverse images of the quaternion units are the bivectors

$$
\vec e_{x}\longmapsto-\gamma_{2}\gamma_{3}, \qquad
\vec e_{y}\longmapsto-\gamma_{3}\gamma_{1}, \qquad
\vec e_{z}\longmapsto-\gamma_{1}\gamma_{2}.
$$

### The Grades of the Biquaternion Components

The grade decomposition of $\mathrm{Cl}_{3,0}$ is

$$
\mathrm{Cl}_{3,0}=\mathrm{Cl}^{0}\oplus\mathrm{Cl}^{1}\oplus\mathrm{Cl}^{2}\oplus\mathrm{Cl}^{3},
$$

of dimensions $1,3,3,1$. The biquaternion basis is read on it as follows.

| Biquaternion component | Clifford grade | Example |
|---|---|---|
| scalar part $Q_{t}e_{t}$ | $0$ | $e_{t}$ |
| vector part $\vec Q$ (real coefficients) | $2$ | $\vec e_{x}$ |
| imaginary scalar $iQ_{t}$ | $3$ | $i=\omega$ |
| imaginary vector $i\vec Q$ | $1$ | $i\vec e_{x}=\gamma_{1}$ |

A general biquaternion has complex coefficients, so it has components in all four grades: the real part of the scalar is grade $0$, the imaginary part of the scalar is grade $3$, the real part of the vector is grade $2$, and the imaginary part of the vector is grade $1$. The complex structure $i=\omega$ acts as the Hodge star on the grades, exchanging $0\leftrightarrow3$ and $1\leftrightarrow2$, which is the content of *The Volume Element, Duality and the Hodge Star*, §*The Biquaternion Case*.

**Remark.** The biquaternion norm $\langle\tilde Q\rangle_{\natural}=Q_{t}^{2}+Q_{x}^{2}+Q_{y}^{2}+Q_{z}^{2}$ is the reduced norm of the matrix algebra $M_{2}(\mathbb{C})$, not the Clifford quadratic form. The Clifford form is $Q(\gamma_{\mu})=+1$ on the generators, while the quaternion units have square $-1$. The two forms are related by the identification $\gamma_{\mu}=i\vec e_{\mu}$ and the sign $i^{2}=-1$; the norm governs invertibility, and the Clifford form governs the grade structure. This is the sign dictionary of *The Number Systems as Clifford Algebras*, §*The Dictionary*.

## The Eigenvalue Decomposition

### The Pure Root

Let $\tilde Q=Q_{t}e_{t}+\vec Q$ with $\vec Q=Q_{x}\vec e_{x}+Q_{y}\vec e_{y}+Q_{z}\vec e_{z}$ and complex coefficients. The square of the vector part is central,

$$
\vec Q^{2}=-(Q_{x}^{2}+Q_{y}^{2}+Q_{z}^{2})e_{t},
$$

as in *Biquaternion Spectral Theory*, §*The Biquaternion Spectrum*. Let $B$ be a square root of $Q_{x}^{2}+Q_{y}^{2}+Q_{z}^{2}$ and assume $B\neq0$. Put

$$
\vec U=\frac{\vec Q}{B}, \qquad \vec\Xi=-i\vec U=-\frac{i\vec Q}{B}.
$$

In the Clifford dictionary, $\vec Q$ is a bivector, $i=\omega$ is the volume element, and $\omega\vec Q$ is a vector; hence $\vec\Xi$ is a **Clifford vector**. Its square is

$$
\vec\Xi^{2}=(-i)^{2}\frac{\vec Q^{2}}{B^{2}}=(-1)\frac{-B^{2}}{B^{2}}=1,
$$

so $\vec\Xi$ is a unit vector, and it is a pure root of $+1$ in the sense of *Square Roots of One and the Idempotents of the Biquaternion Algebra*, §*The Roots of One*. The choice of $B$ is two-fold, and the replacement $B\mapsto-B$ replaces $\vec\Xi$ by $-\vec\Xi$; only the unordered pair is determined by $\tilde Q$.

### The Eigenvalues

Since $\vec Q=iB\vec\Xi$,

$$
(\tilde Q-Q_{t}e_{t})^{2}=\vec Q^{2}=-B^{2}e_{t},
$$

and the characteristic polynomial is

$$
\boxed{\;p_{\tilde Q}(X)=X^{2}-2Q_{t}X+\langle\tilde Q\rangle_{\natural}=(X-Q_{t})^{2}+B^{2}\;},
$$

with the roots

$$
\lambda_{\pm}=Q_{t}\pm iB=Q_{t}\pm B\omega .
$$

In the Clifford reading, the eigenvalues are **central elements of grades $0$ and $3$**: $Q_{t}$ is grade $0$, and $B\omega$ is the top grade. They are internal non-scalar eigenvalues in the sense of *The Eigenvalue Decomposition in a Clifford Algebra*, §*Internal and External Non-Scalar Eigenvalues*: the imaginary unit is the volume element of the algebra, not an external scalar. The discriminant is

$$
(\lambda_{+}-\lambda_{-})^{2}=(2iB)^{2}=-4B^{2}\neq0,
$$

so the eigenvalues are distinct exactly when $B\neq0$, and the minimal polynomial is then $p_{\tilde Q}$.

### The Eigenprojectors

Put

$$
\tilde\Pi_{+}=\tfrac12(e_{t}+\vec\Xi), \qquad \tilde\Pi_{-}=\tfrac12(e_{t}-\vec\Xi).
$$

These are the two idempotents of the root $\vec\Xi$ under the halving map of *Square Roots of One and the Idempotents of the Biquaternion Algebra*, §*The Idempotents*. In the Clifford reading they are the **standard vector idempotents** of the unit vector $\vec\Xi$: they are idempotent, orthogonal and complete, and their grade support is $\{0,1\}$. They are primitive, and the pair is the complete orthogonal pair of *Ideals and Peirce Decomposition of the Biquaternion Algebra*, §*Idempotents and Orthogonal Idempotents*.

The eigenvalue relations are

$$
\tilde Q\tilde\Pi_{+}=\lambda_{+}\tilde\Pi_{+}, \qquad
\tilde Q\tilde\Pi_{-}=\lambda_{-}\tilde\Pi_{-}.
$$

Indeed, since $\tilde Q=Q_{t}+\vec Q=Q_{t}+iB\vec\Xi$ and $\vec\Xi^{2}=1$,

$$
\tilde Q\tilde\Pi_{+}
=(Q_{t}+iB\vec\Xi)\tfrac12(1+\vec\Xi)
=\tfrac12(Q_{t}+iB)(1+\vec\Xi)
=\lambda_{+}\tilde\Pi_{+},
$$

and the other relation is the same with $iB$ replaced by $-iB$ and $\vec\Xi$ by $-\vec\Xi$. Equivalently, by the Lagrange–Sylvester formula of *The Lagrange–Sylvester Eigenprojector Formula*, §*The Eigenprojector Formula*,

$$
\tilde\Pi_{+}=\frac{\tilde Q-\lambda_{-}}{\lambda_{+}-\lambda_{-}}, \qquad
\tilde\Pi_{-}=\frac{\tilde Q-\lambda_{+}}{\lambda_{-}-\lambda_{+}}, \qquad
\lambda_{+}-\lambda_{-}=2iB .
$$

### The Decomposition

Summing the two eigenvalue relations,

$$
\boxed{\;\tilde Q=\lambda_{+}\tilde\Pi_{+}+\lambda_{-}\tilde\Pi_{-}
=(Q_{t}+iB)\tilde\Pi_{+}+(Q_{t}-iB)\tilde\Pi_{-}\;}.
$$

This is the eigenvalue decomposition of *Eigenvalue Decomposition and Eigenbasis of a Biquaternion*, §*The Eigenvalue Decomposition*, read in the Clifford algebra. The eigenvalues are distinct, the idempotents are nonzero, orthogonal and complete, and the resolution is unique up to the swap of the two signs. The scalar-vector form is

$$
\tilde Q=Q_{t}e_{t}+B\vec U=Q_{t}e_{t}+iB\vec\Xi,
$$

and the grade decomposition reads $Q_{t}$ in grade $0$, $B\vec U$ in grade $2$, and the eigenvalue $iB$ in grade $3$ when $Q_{t}$ and $B$ are real; for complex coefficients the four grades are read as in §*The Grades of the Biquaternion Components*. The idempotents are of grades $0$ and $1$, and the grade-$1$ parts cancel in the sum.

**Remark.** The decomposition is the Clifford case of the **internal** non-scalar eigenvalue: the coefficient field is the centre $Z(\mathbb{B})=\mathbb{C}=\mathbb{R}[\omega]$, the eigenvalues are central, and the projectors are standard idempotents. In an even-dimensional Clifford algebra the same formulas would require an external imaginary unit and would produce projectors of grade $0$ and $2$; in $\mathrm{Cl}_{3,0}$ the volume element supplies the unit internally and the projectors are of grade $0$ and $1$. This is the structural difference between the biquaternion case and the plane case of *The Eigenvalue Decomposition in a Clifford Algebra*, §*The External Case: A Bivector in the Plane*.

## The Peirce and Spinor Structure

### The Peirce Decomposition

Let $\mathbb{B}_{st}=\tilde\Pi_{s}\mathbb{B}\tilde\Pi_{t}$ for $s,t\in\{+,-\}$, the Peirce corners of the pair. The Peirce decomposition is

$$
\mathbb{B}=\mathbb{B}_{++}\oplus\mathbb{B}_{+-}\oplus\mathbb{B}_{-+}\oplus\mathbb{B}_{--},
$$

and each corner is one complex line: the diagonal corners are $\mathbb{C}\tilde\Pi_{+}$ and $\mathbb{C}\tilde\Pi_{-}$, and the mixed corners are square-zero. This is the decomposition of *Ideals and Peirce Decomposition of the Biquaternion Algebra*, §*The Biquaternion Case*, attached to the root $\vec\Xi=-i\vec Q/B$.

The diagonal part is

$$
\boxed{\;\mathbb{B}_{++}\oplus\mathbb{B}_{--}=\mathbb{C}\tilde\Pi_{+}\oplus\mathbb{C}\tilde\Pi_{-}
=\mathbb{C}[\tilde Q]=\operatorname{span}_{\mathbb{C}}\{e_{t},\tilde Q\}\;},
$$

a commutative subalgebra isomorphic to $\mathbb{C}\times\mathbb{C}$. It is the centraliser of $\tilde Q$ by *The Centraliser and the Diagonal Peirce Part*, §*The theorem*, and the mixed part is $[\tilde\Pi_{+},\mathbb{B}]$ by *Off-Diagonal Peirce Components and Noncentral Idempotents*, §*The Commutator Interpretation*. The element $\tilde Q$ lies in the diagonal part, with the diagonal coordinates $\lambda_{\pm}$; the mixed corners are the directions that fail to commute with $\tilde Q$.

### The Left Ideals

The left ideals

$$
I_{\pm}=\mathbb{B}\tilde\Pi_{\pm}
$$

are the two minimal left ideals of the algebra, and they are the spinor spaces of *Spinors as Minimal Left Ideals with Inner Conjugation*, §*Three Dimensions*, transported to the biquaternion notation. The even part of $\mathrm{Cl}_{3,0}$ is $\mathrm{Cl}^{0}\cong M_{2}(\mathbb{R})$, and the two ideals are the two columns of the matrix model; in the biquaternion algebra they are the two two-dimensional complex spaces on which the diagonal part acts by the two eigenvalues.

**Remark.** The Peirce and spinor structures are the same structure read twice: the Peirce corners are the matrix units of the $2\times2$ matrix model, and the left ideals are its columns. The Clifford reading adds the grades: the idempotents are of grades $0$ and $1$, and the mixed corners are spanned by products of an idempotent with an off-diagonal element, with the grades determined by the grade theorem. The grade table of §*The Grades of the Biquaternion Components* is the bookkeeping of the Peirce table.

## The Degenerate Regimes

### The Nilpotent Regime

Let $B=0$ and $\vec Q\neq0$. Then $\vec Q^{2}=0$, so $\vec\Upsilon=\vec Q$ is a pure nilpotent, written with the arrow and without the tilde by §*The Nilpotent Convention* of *Conventions in Mathematics*, and

$$
\tilde Q=Q_{t}e_{t}+\vec\Upsilon, \qquad \vec\Upsilon^{2}=0.
$$

The element is a unit exactly when $Q_{t}\neq0$, since $\langle\tilde Q\rangle_{\natural}=Q_{t}^{2}$, and its minimal polynomial is $(X-Q_{t})^{2}$, which is not squarefree. By *The Eigenvalue Decomposition of an Element*, §*Existence and Uniqueness*, there is no eigenvalue decomposition. In the Clifford reading, $\vec Q$ is a null bivector: its Hodge dual $i\vec Q$ is a null vector, and the grade structure degenerates. The element is a single Jordan block in the matrix model, and its centraliser is

$$
\{ae_{t}+b\vec\Upsilon:\ a,b\in\mathbb{C}\},
$$

whose only idempotents are $0$ and $e_{t}$; there is no pair of nonzero orthogonal idempotents summing to the identity in the centraliser.

### The Scalar Regime

Let $\vec Q=0$, so $\tilde Q=Q_{t}e_{t}$. The element is central and semisimple, with the single eigenvalue $Q_{t}$ and minimal polynomial $X-Q_{t}$. Its centraliser is all of $\mathbb{B}$. The eigenvalue decomposition in the sense of the general theory has one term, $\tilde Q=Q_{t}e_{t}$, with the single eigenprojector $e_{t}$, and it is unique. A decomposition into two primitive idempotents with the repeated coefficient $Q_{t}$ is a different object: every complete orthogonal pair $\tilde\Pi_{1},\tilde\Pi_{2}$ gives

$$
\tilde Q=Q_{t}\tilde\Pi_{1}+Q_{t}\tilde\Pi_{2},
$$

and the pair is not determined by $\tilde Q$. The two-projector writing is therefore non-unique, and the eigenvalue data determine nothing beyond the scalar.

## The Hermitian Case

### The Hermitian Projectors

Hermitian conjugation is the star, and normality is $\tilde Q\tilde Q^{*}=\tilde Q^{*}\tilde Q$, as in *Biquaternion Spectral Theory*, §*Hermitian and Normal Elements*; the conjugations are those of *Conventions in Mathematics*, §*The Conjugations*. In the Clifford reading, the star is the Clifford conjugation composed with the appropriate grade operations, and a Hermitian biquaternion is a normal element whose spectral projectors are fixed by the star.

**Proposition.** Let $B\neq0$. The following are equivalent: (i) $\tilde\Pi_{\pm}$ are Hermitian; (ii) $\vec U$ is real; (iii) $\vec\Xi$ is purely imaginary; (iv) $\tilde Q$ is normal.

*Proof.* The equivalence of (i), (ii) and (iv) is *Eigenvalue Decomposition and Eigenbasis of a Biquaternion*, §*The Hermitian Case*, Proposition. The equivalence of (ii) and (iii) is the Clifford dictionary: $\vec U$ is a bivector and $\vec\Xi=-i\vec U=-\omega\vec U$ is its Hodge dual vector; the relation is multiplication by $-i$, so $\vec U$ is real exactly when $\vec\Xi$ is purely imaginary.

When the conditions hold, the projectors are the standard idempotents of the pure root $\vec\Xi=-i\vec u$ over a real unit vector $\vec u$, and the resolution is the spectral theorem of *Biquaternion Spectral Theory*, §*The Spectral Theorem*, read in the Clifford algebra. For a Hermitian $\tilde Q$ the eigenvalues are real, $\lambda_{\pm}=Q_{t}\mp\lvert\vec q'\rvert$ with $\vec Q=i\vec q'$, and the two idempotents are Hermitian and orthogonal for the Hermitian form.

### The Grade Reading of the Hermitian Case

The Hermitian condition has a grade reading. The biquaternion star fixes the real scalar part and the imaginary vector part, and negates the real vector part and the imaginary scalar part; in the Clifford grading, it fixes grades $0$ and $1$ and negates grades $2$ and $3$ up to the appropriate conjugation. A Hermitian element therefore has its grade-$0$ and grade-$1$ components real and its grade-$2$ and grade-$3$ components imaginary, which is the statement that $\vec Q=i\vec q'$ with $\vec q'$ real. The pure root $\vec\Xi=-\omega\vec U$ is then purely imaginary, equal to $-i\vec u$ for a real unit vector $\vec u$, and the projectors $\frac12(1\pm\vec\Xi)$ are the Hermitian idempotents of that pure root. The spectral resolution is the orthogonal decomposition of the Hermitian form.

**Remark.** The Hermitian case is the case in which the internal eigenvalue is real. The eigenvalues $\lambda_{\pm}=Q_{t}\mp\lvert\vec q'\rvert$ lie in $\mathbb{R}\subset\mathbb{C}=Z(\mathbb{B})$, and the projectors are Hermitian. The general internal case, with complex $\vec U$, has complex eigenvalues in $Z$ and non-Hermitian projectors; the spectral theorem still holds in the complex algebra, but the projectors are not fixed by the star.

## Summary

The biquaternion algebra is the Clifford algebra $\mathrm{Cl}_{3,0}$: the quaternion units are the bivectors, the central imaginary unit is the volume element $\omega$, and the grade decomposition has dimensions $1,3,3,1$. A biquaternion $\tilde Q=Q_{t}+\vec Q$ has the eigenvalue decomposition

$$
\tilde Q=\lambda_{+}\tilde\Pi_{+}+\lambda_{-}\tilde\Pi_{-},
\qquad
\lambda_{\pm}=Q_{t}\pm iB=Q_{t}\pm B\omega,
\qquad
\tilde\Pi_{\pm}=\tfrac12(1\pm\vec\Xi),
$$

with $\vec\Xi=-i\vec Q/B$ a unit vector and $B^{2}=Q_{x}^{2}+Q_{y}^{2}+Q_{z}^{2}$. The eigenvalues are central elements of grades $0$ and $3$; the projectors are standard vector idempotents of grades $0$ and $1$. The decomposition is the internal non-scalar case of the Clifford spectral theory: the imaginary unit is the volume element, not an external scalar.

The Peirce corners of the pair are the four one-dimensional complex spaces of the matrix model; the diagonal part is $\mathbb{C}[\tilde Q]$, and the mixed part is the commutator with $\tilde\Pi_{+}$. The left ideals $\mathbb{B}\tilde\Pi_{\pm}$ are the two minimal left ideals, the spinor spaces. In the nilpotent regime $B=0$, $\vec Q\neq0$, there is no eigenvalue decomposition; in the scalar regime $\vec Q=0$, the one-term decomposition is unique but the two-projector refinement is not. In the Hermitian case the projectors are Hermitian, the root is purely imaginary, of the form $\vec\Xi=-i\vec u$ for a real unit vector $\vec u$, and the resolution is the spectral theorem of the biquaternion algebra.

The coordinate formulas are *Eigenvalue Decomposition and Eigenbasis of a Biquaternion*; the spectral theory is *Biquaternion Spectral Theory*; the roots and idempotents are *Square Roots of One and the Idempotents of the Biquaternion Algebra*; the Peirce decomposition is *Ideals and Peirce Decomposition of the Biquaternion Algebra*; the Clifford dictionary is *The Number Systems as Clifford Algebras*; and the general theory is *The Eigenvalue Decomposition in a Clifford Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra |
| $\gamma_{\mu}$ | the Clifford generators of $\mathrm{Cl}_{3,0}$, $\gamma_{\mu}^{2}=1$ |
| $\omega=\gamma_{1}\gamma_{2}\gamma_{3}$ | the volume element, $\omega^{2}=-1$, central |
| $i=\omega$ | the central scalar imaginary of $\mathbb{B}$ |
| $\vec e_{x},\vec e_{y},\vec e_{z}$ | the quaternion units, the bivectors $-\gamma_{\nu}\gamma_{\rho}$ |
| $\tilde Q=Q_{t}e_{t}+\vec Q$ | a biquaternion, with $\vec Q=Q_{x}\vec e_{x}+Q_{y}\vec e_{y}+Q_{z}\vec e_{z}$ |
| $B^{2}=Q_{x}^{2}+Q_{y}^{2}+Q_{z}^{2}$ | the square of the vector norm |
| $\vec U=\vec Q/B$ | the unit bivector |
| $\vec\Xi=-i\vec U$ | the pure root, a unit vector |
| $\lambda_{\pm}=Q_{t}\pm iB$ | the eigenvalues, central of grades $0$ and $3$ |
| $\tilde\Pi_{\pm}=\tfrac12(1\pm\vec\Xi)$ | the eigenprojectors, grades $0$ and $1$ |
| $\mathbb{B}_{st}=\tilde\Pi_{s}\mathbb{B}\tilde\Pi_{t}$ | the Peirce corners |
| $I_{\pm}=\mathbb{B}\tilde\Pi_{\pm}$ | the minimal left ideals, the spinor spaces |

## Further Reading

- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the identification of the biquaternions with $\mathrm{Cl}_{3,0}$ and the volume element.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2001), for the bivectors, the volume element and the spinor ideals.
- The biquaternion articles of this corpus: *The Biquaternion Algebra and Its Vector Spaces*, *Biquaternion Spectral Theory*, *Square Roots of One and the Idempotents of the Biquaternion Algebra*, *Ideals and Peirce Decomposition of the Biquaternion Algebra* and *Eigenvalue Decomposition and Eigenbasis of a Biquaternion*.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the Peirce decomposition and the matrix model.
