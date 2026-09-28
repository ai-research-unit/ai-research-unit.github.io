
# __Quaternion Spectral Theory__

## Introduction

Because the quaternion algebra is a division algebra, every non-zero element is invertible and the spectrum of a single quaternion is easy to describe; but because it is non-commutative, the left and right eigenvalue problems for quaternionic matrices differ, and the word "spectrum" splits into several inequivalent sets. This article fixes the definitions, describes the spectrum of a quaternion and of a quaternionic matrix, proves the Cayley–Hamilton identity and describes the trace and determinant functionals, classifies the similarity classes and states the eigenvalue dichotomy, computes the eigenspaces, treats the resolvent and the spectral radius, and presents the S-spectrum and the quaternionic spectral theorem. It is the quaternion member of the family's spectral pair; its counterpart is the biquaternion case, where the scalars are central and the spectrum is an ordinary complex two-point set, and the relation between the two is that the biquaternion spectrum is the slice of the quaternion S-sphere.

The article uses *Quaternion Algebra* and *Quaternion Norm and Invertibility* for the algebra, the quaternion norm and invertibility, *Quaternion Roots of Minus One* for the sphere of imaginary units, *Quaternion Automorphisms and Derivations* for conjugation and similarity, and *Quaternion Exponential and Lie Group Structure* for the exponential. The standard results on quaternionic matrices that are not computed here are quoted from the literature and named as standard.

The corpus's default base is a commutative ring with identity; the spectrum requires a division ring and a topology, so scalars lie in $\mathbb{H}$ or $\mathbb{C}$ and everything below is over $\mathbb{R}$.

Throughout, $\mathbb{H}$ is the quaternion algebra over $\mathbb{R}$ with basis $e_0 = 1, e_1, e_2, e_3$, $e_k^2 = -e_0$; a quaternion is $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3 = q_0+q_1e_1+q_2e_2+q_3e_3$, with conjugate $\bar{\tilde q}$, scalar part $\mathrm{Sc}\tilde q = q_0$, vector part $\mathrm{Vect}\tilde q = \mathbf{q}$, norm $N(\tilde q) = \tilde q\bar{\tilde q}$ and modulus $|\tilde q| = \sqrt{N(\tilde q)}$. The unit group is $\mathbb{H}^{\times} = \mathbb{H}\setminus\{0\}$, and $M_n(\mathbb{H})$ acts on column vectors in $\mathbb{H}^n$.

## The Spectrum of a Quaternion

**Definition.** The **spectrum** of a quaternion $\tilde q$ in the algebra is $\sigma_{\mathbb{H}}(\tilde q) = \{\lambda\in\mathbb{H} : \tilde q-\lambda \text{ is not invertible}\}$.

**Theorem.** For every quaternion $\tilde q$, $\sigma_{\mathbb{H}}(\tilde q) = \{\tilde q\}$; the algebra is a division algebra, so $\tilde q-\lambda$ fails to be invertible only when $\tilde q-\lambda = 0$.

*Proof.* $\tilde q-\lambda$ is invertible for every $\lambda\neq \tilde q$, since $N(\tilde q-\lambda) > 0$ when $\tilde q\neq\lambda$, and equals $0$ when $\lambda = \tilde q$.

Thus a single quaternion has no interesting algebra spectrum; the structure appears in the eigenvector problems of the operators it defines. The following two notions, well defined for matrices over any division ring, are the source of the whole subject.

**Definition.** Let $M\in M_n(\mathbb{H})$ and $\lambda\in\mathbb{H}$. Then $\lambda$ is a **right eigenvalue** of $M$ if $Mv = v\lambda$ for some non-zero $v\in\mathbb{H}^n$, and a **left eigenvalue** if $Mv = \lambda v$ for some non-zero $v$. The sets of such $\lambda$ are the **right spectrum** $\sigma_R(M)$ and the **left spectrum** $\sigma_L(M)$.

**Proposition.** $\lambda\in\sigma_L(M)$ if and only if $M-\lambda I$ is singular; for the $1\times1$ matrix $M = [\tilde q]$ this gives $\sigma_L([\tilde q]) = \{\tilde q\}$.

*Proof.* $Mv = \lambda v\iff(M-\lambda I)v = 0$, so a left eigenvalue is exactly a scalar for which the operator has non-trivial kernel; a square matrix over a division ring is invertible exactly when its kernel vanishes.

**Proposition.** The right spectrum is invariant under conjugation: if $Mv = v\lambda$ and $w\neq0$, then $M(vw) = (vw)(w^{-1}\lambda w)$, so $\sigma_R(M)$ is a union of conjugacy classes of $\mathbb{H}$.

*Proof.* $M(vw) = (Mv)w = v\lambda w$, and $v\lambda w = (vw)(w^{-1}\lambda w)$.

## The Sphere of Eigenvalues

**Theorem.** For the $1\times1$ matrix $M = [\tilde q]$ the two spectra are

$$
\sigma_L([\tilde q]) = \{\tilde q\}, \qquad \sigma_R([\tilde q]) = \{v^{-1}qv : v\in\mathbb{H}^{\times}\},
$$

and the right spectrum is the **similarity class** of $\tilde q$,

$$
\sigma_R([\tilde q]) = \{q_0+\mathbf{w} : \mathbf{w}\in\operatorname{Im}\mathbb{H},\ |\mathbf{w}| = |\mathrm{Vect}\tilde q|\},
$$

a point $\{q_0\}$ when $\tilde q$ is real and a two-sphere of radius $|\mathrm{Vect}\tilde q|$ about the real point $q_0$ otherwise.

*Proof.* $qv = \lambda v$ with $v = 1$ gives $\lambda = \tilde q$, and conversely $(\tilde q-\lambda)v = 0$ with $v\neq0$ forces $\tilde q = \lambda$ because $\mathbb{H}$ has no zero divisors; this is the left spectrum. For the right spectrum, $qv = v\lambda$ gives $\lambda = v^{-1}qv$, and the map $v\mapsto v^{-1}qv$ is the conjugacy action, which fixes the real part and rotates the vector part; the vector part of $v^{-1}qv$ has the same modulus as $\mathrm{Vect}\tilde q$, and every vector of that modulus is attained.

**Corollary.** For a non-real quaternion the left and right spectra differ: the left spectrum is a single point, the right spectrum a two-sphere. For a real quaternion both are the point $\{q_0\}$.

*Proof.* The left spectrum is $\{\tilde q\}$, which is one point of the class $\sigma_R([\tilde q])$; the class is a two-sphere exactly when $\tilde q$ is non-real.

**Remark.** The right spectrum of $[\tilde q]$ is the sphere of *Quaternion Roots of Minus One*: for $\tilde q$ of the form $q_0+\mu$ with $\mu$ a pure unit, the right spectrum is $q_0+S^2$, where $S^2$ is the sphere of imaginary units. The two notions of "spectrum" are thus connected through the geometry of the imaginary sphere.

## The Standard Spectrum of a Quaternionic Matrix

For $n\geq2$ the two spectra are studied through complex scalars. A complex scalar commutes with every quaternion, so a complex number $\lambda$ may be written on either side, and the left and right problems then agree for complex eigenvalues.

**Theorem (standard form).** Every $M\in M_n(\mathbb{H})$ is similar over $\mathbb{H}$ to an upper triangular matrix whose diagonal entries are complex numbers $\lambda_1,\dots,\lambda_n$ with $\operatorname{Im}\lambda_i\geq0$. The **right spectrum** is the union of the corresponding similarity classes,

$$
\sigma_R(M) = \bigcup_{i=1}^{n}[\lambda_i], \qquad [\lambda] = \{v^{-1}\lambda v : v\in\mathbb{H}^{\times}\},
$$

which is a finite union of at most $n$ spheres or points.

*Proof.* The standard form and the eigenvalue statement are standard in quaternionic linear algebra (Zhang 1997; Rodman 2014); the classes $[\lambda_i]$ are the right eigenvalues, and every right eigenvalue lies in one of them by the invariance of $\sigma_R$ under conjugation.

**Definition.** The **standard spectrum** of $M$ is the multiset $\{\lambda_1,\dots,\lambda_n\}$ of complex numbers with non-negative imaginary part given by the standard form; it is a set of representatives, one for each right eigenvalue class, and depends only on $M$ up to a simultaneous choice of slice.

**Proposition.** For a complex scalar $\lambda$ the left and right eigenvalue problems coincide: $\lambda\in\sigma_L(M)$ if and only if $\lambda\in\sigma_R(M)$. In general the two spectra are incomparable, and neither is contained in the other.

*Proof.* A complex scalar commutes with every quaternion, so $Mv = \lambda v$ and $Mv = v\lambda$ are the same equation whenever $\lambda$ is complex; this is the equivalence. For the incomparability, take $n = 2$. For $M = \operatorname{diag}(e_1,e_2)$ the right spectrum is the whole sphere of pure units, since every conjugate of $e_1$ and of $e_2$ is a right eigenvalue, while the only left eigenvalues are $e_1$ and $e_2$, because $(e_1-\lambda)v_1 = 0$ forces $\lambda = e_1$ or $v_1 = 0$; hence $\sigma_R(M)\not\subseteq\sigma_L(M)$. For $M = \begin{pmatrix}0&e_1\\-4e_1&0\end{pmatrix}$ the standard eigenvalues are the real numbers $2$ and $-2$, so $\sigma_R(M) = \{2,-2\}$, while the left spectrum is infinite (Huang and So), namely the two-sphere $\{\tilde q\in\operatorname{span}(1,e_2,e_3) : |\tilde q| = 2\}$; hence $\sigma_L(M)\not\subseteq\sigma_R(M)$.

**Remark.** Unlike the right spectrum, the left spectrum of a quaternionic matrix need not be a finite union of spheres: for $n\geq2$ it can be infinite, a union of continua of spheres. This is a genuine phenomenon of non-commutative linear algebra, established by Huang and So, and it is the reason that the right spectrum and the S-spectrum, not the left spectrum, are the objects of the functional calculus. For $n = 1$ the left spectrum is finite, a single point.

## Cayley–Hamilton and the Trace and Norm Functionals

**Definition.** The **trace functional** and **determinant functional** — more precisely the **reduced trace** and **reduced norm** — of a quaternion are

$$
T(\tilde q) = 2\mathrm{Sc}\tilde q = 2q_0, \qquad D(\tilde q) = N(\tilde q) = \tilde q\bar{\tilde q} = q_0^2+|\mathbf{q}|^2 .
$$

**Theorem (Cayley–Hamilton for a quaternion).** Every quaternion satisfies

$$
\tilde q^2-T(\tilde q)\,\tilde q+D(\tilde q) = 0, \qquad \text{that is} \qquad \tilde q^2-2q_0\tilde q+N(\tilde q) = 0 .
$$

*Proof.* With $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$ and $\mathbf{q}^2 = -|\mathbf{q}|^2$,

$$
\tilde q^2 = q_0^2+2q_0\mathbf{q}+\mathbf{q}^2 = q_0^2+2q_0\mathbf{q}-|\mathbf{q}|^2 = 2q_0\tilde q-(q_0^2+|\mathbf{q}|^2) = T(\tilde q)\tilde q-D(\tilde q).
$$

**Corollary.** A non-zero quaternion is a root of its own quadratic $x^2-T(\tilde q)x+D(\tilde q)$, which has the **non-positive** discriminant

$$
T(\tilde q)^2-4D(\tilde q) = 4q_0^2-4(q_0^2+|\mathbf{q}|^2) = -4|\mathbf{q}|^2\leq0;
$$

over the quaternions a negative discriminant is not a failure of existence but the statement that the two roots are the conjugate pair $q_0\pm\mu|\mathbf{q}|$ for any imaginary unit $\mu$.

**Proposition.** The functionals satisfy

$$
T(p+\tilde q) = T(p)+T(\tilde q), \quad T(\lambda \tilde q) = \lambda T(\tilde q)\ (\lambda\in\mathbb{R}), \quad T(e_0) = 2, \quad T(\tilde q) = T(\tilde q^{-1})N(\tilde q),
$$

$$
D(pq) = D(p)D(\tilde q), \quad D(\lambda \tilde q) = \lambda^2D(\tilde q)\ (\lambda\in\mathbb{R}), \quad D(e_0) = 1,
$$

and both are invariant under similarity, $T(v^{-1}qv) = T(\tilde q)$ and $D(v^{-1}qv) = D(\tilde q)$ for $v\neq0$. The determinant functional is multiplicative, the trace functional is real-linear but not multiplicative, and $T(\tilde q^{-1}) = T(\tilde q)/N(\tilde q)$.

*Proof.* The scalar part and the quaternion norm are additive and multiplicative as stated; similarity preserves the scalar part because $v^{-1}qv$ has the same real part, and preserves the quaternion norm by multiplicativity of $N$.

**Remark.** For matrices the corresponding statements are more delicate. The trace $\operatorname{tr}M = \sum_iM_{ii}$ is not similarity-invariant, since trace is not cyclic over a non-commutative ring; only its real part is, $\mathrm{Sc}\operatorname{tr}(M) = \mathrm{Sc}\operatorname{tr}(S^{-1}MS)$. The determinant is replaced by the **Dieudonné determinant** $\det M$, with values in the abelianisation $\mathbb{H}^{\times}/[\mathbb{H}^{\times},\mathbb{H}^{\times}]\cong\mathbb{R}_{>0}$; it is multiplicative, and $|\det M| = \prod_{i=1}^{n}|\lambda_i|$ for the standard spectrum. These are the correct replacements for the commutative trace and determinant, and their use is standard (Rodman 2014).

## Similarity Classes and the Eigenvalue Dichotomy

**Definition.** Two quaternions $\tilde q,\tilde q'$ are **similar** if $\tilde q' = v^{-1}qv$ for some $v\in\mathbb{H}^{\times}$; two matrices are similar if $M' = S^{-1}MS$ for some invertible $S$.

**Theorem (classification).** Two quaternions are similar if and only if they have the same trace and determinant functionals,

$$
\tilde q'\sim \tilde q\iff T(\tilde q') = T(\tilde q)\ \text{and}\ D(\tilde q') = D(\tilde q),
$$

equivalently if and only if they have the same real part and the same modulus of the vector part. Consequently the similarity class of $\tilde q$ is a point when $\tilde q$ is real and a two-sphere otherwise, and the classes are parametrised by the half-plane $\{(t,d) : d\geq t^2/4\}$ through $(T,D)$.

*Proof.* A conjugation $v^{-1}qv$ preserves the real part and the modulus of the vector part, hence $(T,D)$; conversely two quaternions with equal $(q_0,|\mathbf{q}|)$ are carried one to the other by conjugation by a unit quaternion, which preserves both invariants; this is the transitivity of the adjoint action in *Quaternion Rotations and Reflections*. The class is a point for real $\tilde q$, where $|\mathbf{q}| = 0$.

**Theorem (eigenvalue dichotomy).** For a quaternionic matrix the right spectrum is a finite union of similarity classes, each of which is of exactly one of two kinds: a **real point** $\{t\}$ or a non-degenerate **two-sphere** $[t+\mu s]$ with $s > 0$ and $\mu$ a pure unit. The two kinds cannot mix within one class.

*Proof.* Each class $[\lambda_i]$ of the standard spectrum is a point if $\lambda_i$ is real and a two-sphere if it is not, by the classification of the previous theorem.

**Corollary.** For the standard spectrum $\{\lambda_1,\dots,\lambda_n\}$ the multiset of real classes is exactly the set of real eigenvalues, and the non-real classes are the genuine spheres; the sum of the sizes of the classes is not finite unless every eigenvalue is real, which is why multiplicity is counted on the standard representatives rather than on the spherical classes.

## Eigenspaces and Their Dimensions

**Definition.** For a right eigenvalue class $[\lambda]$ of $M$ the **right eigenspace** is

$$
V_{[\lambda]} = \{v\in\mathbb{H}^n : Mv = v\mu \text{ for some } \mu\in[\lambda]\},
$$

and the **geometric multiplicity** of the class is its dimension as a right $\mathbb{H}$-vector space.

**Proposition.** $V_{[\lambda]}$ is a right $\mathbb{H}$-subspace; for a single quaternion, $V_{[\tilde q]} = \mathbb{H}$, of dimension one over $\mathbb{H}$; and the set $\{v : qv = v\lambda\}$ for one fixed non-real representative $\lambda$ is not a right $\mathbb{H}$-subspace but a right $\mathbb{R}[\lambda]$-module of real dimension two.

*Proof.* If $Mv = v\mu$ and $Mw = w\nu$ with $\mu,\nu\in[\lambda]$, then $M(v\alpha+w\beta) = v\mu\alpha+w\nu\beta$ for any quaternions $\alpha,\beta$, and $\mu\alpha,\nu\beta\in[\lambda]$ for $\alpha,\beta\neq0$; for $\alpha = \beta = 0$ the vector is zero. Hence $V_{[\lambda]}$ is a right $\mathbb{H}$-subspace. For $n = 1$ every non-zero $v$ satisfies $qv = v(v^{-1}qv)$, so $V_{[\tilde q]} = \mathbb{H}$. For a fixed non-real $\lambda$, closure under right scaling by $\alpha$ requires $\lambda\alpha = \alpha\lambda$, that is $\alpha\in\mathbb{R}[\lambda]\cong\mathbb{C}$, giving a complex line of real dimension two.

**Proposition (left eigenspace).** For $\lambda\in\sigma_L(M)$ the **left eigenspace** $\{v : Mv = \lambda v\}$ is a right $\mathbb{H}$-subspace; for a single quaternion with $\lambda = \tilde q$ it is all of $\mathbb{H}$.

*Proof.* If $Mv = \lambda v$ and $Mw = \lambda w$, then $M(v\alpha+w\beta) = \lambda v\alpha+\lambda w\beta = \lambda(v\alpha+w\beta)$, so the set is a right $\mathbb{H}$-subspace; for $[\tilde q]$ and $\lambda = \tilde q$ every $v$ satisfies $qv = qv$.

**Corollary.** For a single quaternion the left eigenspace is all of $\mathbb{H}$ (dimension one over $\mathbb{H}$) while the right eigenspace attached to the fixed representative $\tilde q$ is a complex line (real dimension two); this is the eigenspace reflection of the fact that the left spectrum is a point and the right spectrum a sphere.

## The Resolvent and the Spectral Radius

**Definition.** The **left resolvent** of $M$ is $R_L(s) = (M-sI)^{-1}$, defined for $s\notin\sigma_L(M)$. The **S-resolvent** of $M$ is

$$
\mathcal{R}_s(M) = \bigl(M^2-2\operatorname{Re}(s)M+|s|^2I\bigr)^{-1}, \qquad s\notin\sigma_S(M),
$$

where $\sigma_S(M)$ is the S-spectrum defined below.

**Theorem.** For a single quaternion $\tilde q$ and $s\notin[\tilde q]$ the S-resolvent is

$$
\mathcal{R}_s(\tilde q) = \frac{a-2(q_0-s_0)\mathbf{v}}{a^2+4(q_0-s_0)^2|\mathbf{v}|^2}, \qquad a = (q_0-s_0)^2-|\mathbf{v}|^2+|\mathbf{w}|^2,
$$

with $\tilde q = q_0+\mathbf{v}$ and $s = s_0+\mathbf{w}$; it has a simple pole on the two-sphere $[\tilde q]$ and is analytic off it.

*Proof.* Writing $\tilde q^2-2\operatorname{Re}(s)\tilde q+|s|^2 = a+2(q_0-s_0)\mathbf{v}$ with $a$ real and $2(q_0-s_0)\mathbf{v}$ pure, the inverse is $(a-2(q_0-s_0)\mathbf{v})/(a^2+4(q_0-s_0)^2|\mathbf{v}|^2)$. The denominator vanishes exactly when $a = 0$ and $s_0 = q_0$, that is when $s\in[\tilde q]$, which is the S-spectrum.

**Definition.** The **spectral radius** is $\rho(M) = \max\{|s| : s\in\sigma_S(M)\}$.

**Proposition.** For a single quaternion the spectral radius is the modulus, $\rho(\tilde q) = |\tilde q|$; the S-spectrum $[\tilde q]$ consists of elements all of the same modulus $|\tilde q|$, so the maximum is attained everywhere on it.

*Proof.* Every element of the class $[\tilde q]$ has the same norm $N(\tilde q)$ as $\tilde q$, hence the same modulus; the S-spectrum is the class.

**Theorem (spectral radius formula).** For any quaternionic matrix and any submultiplicative norm, $\rho(M) = \lim_{k\to\infty}\|M^k\|^{1/k}$; for a normal matrix $\rho(M)$ equals the operator norm $\|M\|$.

*Proof.* The limit formula is the Gelfand-type statement for quaternionic matrices, and the normal case is part of the quaternionic spectral theorem; both are standard (Rodman 2014).

## The S-Spectrum and the Quaternionic Spectral Theorem

**Definition.** For $M\in M_n(\mathbb{H})$ the **S-spectrum** is

$$
\sigma_S(M) = \{s\in\mathbb{H} : M^2-2\operatorname{Re}(s)M+|s|^2I \text{ is not invertible}\}.
$$

The definition rests on the identity $s^2-2\operatorname{Re}(s)s+|s|^2 = 0$, which holds because $s-\operatorname{Re}(s)$ is pure.

**Theorem.** For every $M\in M_n(\mathbb{H})$ the S-spectrum equals the right spectrum, $\sigma_S(M) = \sigma_R(M)$; hence it is a finite union of similarity classes. For a single quaternion, $\sigma_S([\tilde q]) = [\tilde q]$, a point for real $\tilde q$ and a two-sphere otherwise.

*Proof.* If $Mv = vs$ then $(M^2-2\operatorname{Re}(s)M+|s|^2I)v = v(s^2-2\operatorname{Re}(s)s+|s|^2) = 0$, so $\sigma_R(M)\subseteq\sigma_S(M)$; the reverse inclusion and the identification with the classes are standard (Rodman 2014). The single-quaternion statement is the sphere of eigenvalues computed above.

**Definition.** $M$ is **normal** if $MM^{*} = M^{*}M$, where ${}^{*}$ is the entrywise quaternion conjugation combined with transposition; **Hermitian** if $M^{*} = M$, and **unitary** if $M^{*}M = I$.

**Theorem (quaternionic spectral theorem).** If $M\in M_n(\mathbb{H})$ is normal then there is a unitary $U$ and complex numbers $\lambda_1,\dots,\lambda_n$ in a fixed slice with

$$
M = U\,\operatorname{diag}(\lambda_1,\dots,\lambda_n)\,U^{*},
$$

so the S-spectrum is the union of the classes, $\sigma_S(M) = \bigcup_{i=1}^{n}[\lambda_i]$; for Hermitian $M$ the $\lambda_i$ are real, and for unitary $M$ they have modulus one, in which case every $s\in\sigma_S(M)$ has modulus one.

*Proof.* The diagonalisation is the spectral theorem for normal quaternionic matrices; it is stated and proved in the references (Rodman 2014; Colombo, Sabadini and Struppa 2011).

**Corollary.** For a normal matrix the S-spectrum determines the operator up to unitary equivalence, the spectral radius equals the operator norm, and a Hermitian matrix has real S-spectrum, a unitary one has S-spectrum contained in the unit sphere $S^3$.

## Relation to the Biquaternion Spectral Theory

Viewing a quaternion as a biquaternion with real coefficients, the complex spectrum of the biquaternion theory and the S-spectrum of this article are related by slicing: for any pure unit $\mu$ the complex line $q_0+\mathbb{R}[\mu] = q_0+(\mathbb{R}+\mu\mathbb{R})$ through the real point $q_0$ meets the S-sphere $[\tilde q]$ in exactly the two points $q_0\pm\mu|\mathrm{Vect}\tilde q|$, so the biquaternion spectrum is the two-point slice of the quaternion sphere, obtained by identifying the slice unit $\mu$ with the central imaginary unit $i$ of $\mathbb{B}$,

$$
[\tilde q]\cap\bigl(q_0+\mathbb{R}[\mu]\bigr) = \{q_0\pm\mu|\mathrm{Vect}\tilde q|\}, \qquad
\sigma_{\mathbb{B}}(\tilde q) = \{q_0\pm i|\mathrm{Vect}\tilde q|\} .
$$

| Feature | Quaternion case $\mathbb{H}$ | Biquaternion case $\mathbb{B}$ |
|---|---|---|
| Scalars central? | no | yes |
| Spectrum of a single element | $\sigma_S([\tilde q]) = [\tilde q]$, a $2$-sphere (or a point) | $\sigma(\tilde Q) = \{Q_0\pm iB\}$, two complex points |
| Left and right spectra | differ; $\sigma_L([\tilde q]) = \{\tilde q\}$, $\sigma_R([\tilde q]) = [\tilde q]$ | agree as sets when eigenvalues are complex |
| Trace and determinant functionals | reduced trace $2q_0$, reduced norm $N(\tilde q)$, real | trace $2Q_0$, determinant $N(\tilde Q)$, complex |
| Matrix determinant | Dieudonné determinant, valued in $\mathbb{R}_{>0}$ | ordinary determinant, valued in $\mathbb{C}$ |
| Spectral theorem | $M = U\operatorname{diag}(\lambda_i)U^{*}$, $\sigma_S(M) = \bigcup[\lambda_i]$ | $\tilde Q = \lambda_1P_1+\lambda_2P_2$, complex eigenvalues |
| Reason for the difference | non-commuting scalars | central complex scalars |

The essential difference is the non-commutativity of the scalars. Because the centre of $\mathbb{B}$ is $\mathbb{C}$, the left and right problems for a biquaternion coincide when eigenvalues are taken complex, and the spectral theorem can use complex eigenvalues directly; because the centre of $\mathbb{H}$ is $\mathbb{R}$, the eigenvalues of a quaternion fill a sphere, the left and right spectra are genuinely different, and the correct substitute for the complex spectrum is the S-spectrum, which equals the right spectrum and is a finite union of similarity classes. For a real quaternion viewed as a biquaternion, the two points of the biquaternion spectrum are the slice of the single quaternion sphere, so the two theories agree exactly on the complex line. The biquaternion account is in *Biquaternion Spectral Theory*.

## Summary

The spectrum of a single quaternion in the algebra is the single point $\{\tilde q\}$, but the eigenvector problems of the operator $[\tilde q]$ give two different sets: the left spectrum $\sigma_L([\tilde q]) = \{\tilde q\}$ and the right spectrum $\sigma_R([\tilde q]) = $ the similarity class $[\tilde q]$, which is a point for real $\tilde q$ and a two-sphere of fixed modulus for non-real $\tilde q$. For a quaternionic matrix the right spectrum is a finite union of at most $n$ similarity classes, described by the standard form with complex representatives of non-negative imaginary part; the left spectrum is not invariant under similarity and need not be a finite union of classes, and the two spectra are in general incomparable, agreeing when the eigenvalue is complex.

The Cayley–Hamilton identity $\tilde q^2-T(\tilde q)\tilde q+D(\tilde q) = 0$ holds with the reduced trace $T(\tilde q) = 2q_0$ and reduced norm $D(\tilde q) = N(\tilde q)$, both similarity-invariant, the former real-linear and the latter multiplicative; for matrices the trace is replaced by its real part and the determinant by the Dieudonné determinant, with $|\det M| = \prod_i|\lambda_i|$. Similarity of quaternions is classified by $(T,D)$, so the classes are points or spheres, and the eigenvalue dichotomy separates each class as a real point or a non-degenerate two-sphere.

The right eigenspace attached to a class is a right $\mathbb{H}$-subspace, of dimension one over $\mathbb{H}$ for a single quaternion, whereas the eigenspace of a fixed non-real representative is only a complex line; the left eigenspace for a single quaternion is all of $\mathbb{H}$. The S-resolvent and the left resolvent have explicit closed forms, and the spectral radius of a single quaternion is its modulus; in general the spectral radius obeys the Gelfand-type limit formula and, for normal matrices, equals the operator norm.

The S-spectrum $\sigma_S(M) = \{s : M^2-2\operatorname{Re}(s)M+|s|^2I \text{ singular}\}$ equals the right spectrum, and the quaternionic spectral theorem diagonalises a normal matrix as $M = U\operatorname{diag}(\lambda_i)U^{*}$ with $\sigma_S(M) = \bigcup_i[\lambda_i]$; Hermitian matrices have real S-spectrum and unitary ones S-spectrum on $S^3$. The biquaternion spectrum is the slice of the quaternion sphere on the complex line, and the difference between the two theories is exactly the centrality of the scalars.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | Quaternion algebra, a division algebra; scalars non-central |
| $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$ | Quaternion; $q_0 = \mathrm{Sc}\tilde q$, $\mathbf{q} = \mathrm{Vect}\tilde q$ |
| $N(\tilde q) = \tilde q\bar{\tilde q}$, $\lvert \tilde q\rvert = \sqrt{N(\tilde q)}$ | Quaternion norm and modulus |
| $\sigma_{\mathbb{H}}(\tilde q) = \{\tilde q\}$ | Algebra spectrum of a single quaternion |
| $\sigma_L(M)$, $\sigma_R(M)$ | Left and right spectra |
| $[\lambda] = \{v^{-1}\lambda v : v\neq0\}$ | Similarity class; a point or a two-sphere |
| $\sigma_R([\tilde q]) = [\tilde q]$ | Spectrum of a single quaternion, a two-sphere for non-real $\tilde q$ |
| $\lambda_1,\dots,\lambda_n$ | Standard spectrum, complex with $\operatorname{Im}\lambda_i\geq0$ |
| $T(\tilde q) = 2q_0$, $D(\tilde q) = N(\tilde q)$ | Reduced trace and reduced norm functionals |
| $\tilde q^2-T(\tilde q)\tilde q+D(\tilde q) = 0$ | Cayley–Hamilton identity for a quaternion |
| $\operatorname{tr}M$, $\det M$ | Matrix trace (not similarity-invariant) and Dieudonné determinant |
| $V_{[\lambda]}$ | Right eigenspace of a class, a right $\mathbb{H}$-subspace |
| $R_L(s) = (M-sI)^{-1}$ | Left resolvent, defined off $\sigma_L(M)$ |
| $\mathcal{R}_s(M) = (M^2-2\operatorname{Re}(s)M+\lvert s\rvert^2I)^{-1}$ | S-resolvent |
| $\rho(M)$ | Spectral radius; $\rho(\tilde q) = \lvert \tilde q\rvert$ |
| $\sigma_S(M) = \sigma_R(M)$ | S-spectrum |
| $M = U\operatorname{diag}(\lambda_i)U^{*}$ | Quaternionic spectral theorem for normal $M$ |
| $\sigma_{\mathbb{B}}(\tilde q) = \{q_0\pm i\lvert\mathbf{q}\rvert\}$ | Biquaternion spectrum, the two-point slice of the quaternion sphere $[\tilde q]$ |

## Further Reading

- Fuzhen Zhang, "Quaternions and matrices of quaternions", *Linear Algebra and its Applications* **251** (1997) 21–57, for left and right quaternionic eigenvalues and the standard form.
- Vladimir V. Rodman, *Topics in Quaternion Linear Algebra* (Princeton University Press, 2014), for the S-spectrum, the spectral theorem and the spectral radius formula.
- Fabrizio Colombo, Irene Sabadini and Daniele C. Struppa, *Noncommutative Functional Calculus* (Birkhäuser, 2011), for the S-functional calculus and the quaternionic spectral theorem.
- Liping Huang and Wasin So, "On left eigenvalues of a quaternionic matrix", *Linear Algebra and its Applications* **323** (2001) 105–116, for the infinite left spectrum.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 2nd ed. 2013), for the complex spectral theorem transported to the quaternionic normal case.
- Israel Gohberg, Peter Lancaster and Leiba Rodman, *Indefinite Linear Algebra and Applications* (Birkhäuser, 2005), for the Dieudonné determinant and similarity over division rings.
- Nathan Jacobson, *The Theory of Rings* (American Mathematical Society, 1943), for the Cayley–Hamilton identity and the reduced norm in a division algebra.
