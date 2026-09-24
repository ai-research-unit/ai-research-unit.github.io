# __Biquaternion Exponential and Lie Group Structure__

## Introduction

This article develops the Lie theory of the biquaternion algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$. The basic algebra article defined $\mathbb{B}$ and its six distinguished subspaces $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$, $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$, $\mathbb{M}_-$; the article on norm and invertibility identified the norm form $N(\tilde{Q})$ with the determinant and the units $\mathbb{B}^\times$ with $GL(2,\mathbb{C})$; and the elementary-functions article computed the exponential and logarithm by power series. Here these are assembled into the standard theory of $\mathbb{B}^\times$ as a Lie group, of its Lie algebra $\mathfrak{gl}(2,\mathbb{C})$, and of the exponential map. Every statement is a special case of the standard theory of $GL(2,\mathbb{C})$ and $SL(2,\mathbb{C})$, transported across the isomorphism $\mathbb{B} \cong M_2(\mathbb{C})$ of the algebraic-representations article.

One point governs everything below. The algebra $\mathbb{B}$ is simultaneously **eight-dimensional over $\mathbb{R}$** and **four-dimensional over $\mathbb{C}$**; each complex dimension counts two real dimensions. Every dimension statement therefore names the field concerned.

Throughout, a biquaternion is written

$$
\tilde{Q} = Q_0 e_0 + \mathbf{Q}, \qquad \mathbf{Q} = \sum_{k=1}^{3} Q_k e_k, \qquad Q_\mu \in \mathbb{C}.
$$

The quaternion units satisfy $e_0 = 1$ and $e_k^2 = -e_0$; the scalar imaginary $i$ satisfies $i^2 = -1$ and commutes with every $e_k$. The quaternion conjugate is $\bar{\tilde{Q}} = Q_0 e_0 - \mathbf{Q}$, and the norm form is

$$
N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2.
$$

For a biquaternion with nonzero vector part we write $B = \sqrt{Q_1^2 + Q_2^2 + Q_3^2}$ for the complex norm of the vector part and $\hat{n} = \mathbf{Q}/B$, so that $\hat{n}^2 = -e_0$ and $\mathbf{Q} = B\hat{n}$.

---

# Part I: The Group of Units and the Exponential Map

## 1. The Algebra as the Lie Algebra $\mathfrak{gl}(2,\mathbb{C})$

The companion article gives an algebra isomorphism $\mathbb{B} \cong M_2(\mathbb{C})$ under which the matrix trace and determinant are

$$
\mathrm{Tr}(\tilde{Q}) = 2Q_0, \qquad \det(\tilde{Q}) = N(\tilde{Q}).
$$

**Dimension.** As a complex vector space, $\mathbb{B} \cong \mathbb{C}^4$ has complex dimension $4$; as a real vector space it has real dimension $8$. The trace-free part has complex dimension $3$ and real dimension $6$.

The set $\mathbb{B}$ carries the **commutator bracket**

$$
[\tilde{P}, \tilde{Q}] = \tilde{P}\tilde{Q} - \tilde{Q}\tilde{P},
$$

under which it is the Lie algebra $\mathfrak{gl}(2,\mathbb{C})$ of all $2 \times 2$ complex matrices. As a complex Lie algebra $\mathfrak{gl}(2,\mathbb{C})$ is four-dimensional, and as a real Lie algebra it is eight-dimensional. Its center is the scalar line

$$
\mathfrak{z}(\mathfrak{gl}(2,\mathbb{C})) = \mathbb{C}e_0,
$$

of complex dimension $1$ and real dimension $2$; every scalar multiple of $e_0$ commutes with all of $\mathbb{B}$. Removing the center gives the decomposition

$$
\mathfrak{gl}(2,\mathbb{C}) = \mathfrak{sl}(2,\mathbb{C}) \oplus \mathbb{C}e_0,
$$

with complex dimensions $4 = 3 + 1$ and real dimensions $8 = 6 + 2$, where $\mathfrak{sl}(2,\mathbb{C})$ is the subspace $\{Q_0 = 0\}$ of elements with vanishing scalar part.

## 2. The Group of Units

The **group of units** of $\mathbb{B}$ is the set of invertible elements,

$$
\mathbb{B}^\times = \{\tilde{Q} \in \mathbb{B} : N(\tilde{Q}) \neq 0\},
$$

a group under multiplication with identity $e_0$. By the isomorphism above it is

$$
\mathbb{B}^\times \cong GL(2,\mathbb{C}) = \{M \in M_2(\mathbb{C}) : \det M \neq 0\}.
$$

**Dimension.** $GL(2,\mathbb{C})$ has complex dimension $4$ and real dimension $8$; the units are exactly the nonzero-determinant elements, and the determinant is the norm form.

The group $\mathbb{B}^\times$ is open (it is $N^{-1}(\mathbb{C}\setminus\{0\})$), connected but not compact, and its center is $Z(\mathbb{B}^\times) = \mathbb{C}^\times e_0 \cong \mathbb{C}^\times$, a real Lie group of dimension $2$. Its Lie algebra is $\mathbb{B}$ itself with the commutator bracket, i.e. $\mathfrak{gl}(2,\mathbb{C})$: the tangent space at the identity is the whole algebra because the units are open. The inverse map has differential $-\mathrm{id}$ at the identity, the infinitesimal reason the bracket is antisymmetric.

## 3. The Exponential: Series and Closed Form

The **exponential** of a biquaternion is defined by the power series

$$
\exp(\tilde{Q}) = \sum_{n=0}^{\infty} \frac{\tilde{Q}^n}{n!}.
$$

In the Euclidean norm on $\mathbb{B} \cong \mathbb{R}^8$ one has $\|\tilde{Q}^n\|_E \leq \|\tilde{Q}\|_E^n$, so the series converges absolutely and uniformly on bounded sets, and the exponential is an entire function on the real vector space $\mathbb{B}$. Under the isomorphism $\mathbb{B} \cong M_2(\mathbb{C})$ it becomes the ordinary matrix exponential, so every identity of the matrix exponential carries over with $\det$ read as $N$ and $\mathrm{tr}$ read as twice the scalar part.

**Closure of the formula.** The series sums in closed form in the two regimes of the elementary-functions article. Writing $\tilde{Q} = Q_0 e_0 + \mathbf{Q}$, with $B = \sqrt{Q_1^2 + Q_2^2 + Q_3^2}$ and $\hat{n} = \mathbf{Q}/B$, one has

$$
\exp(\tilde{Q}) =
\begin{cases}
e^{Q_0}\bigl(\cos B\, e_0 + \sin B\, \hat{n}\bigr), & B \neq 0, \\[2mm]
e^{Q_0}\bigl(e_0 + \mathbf{Q}\bigr), & B = 0.
\end{cases}
$$

The first line is the oscillatory regime (nonzero complex norm, alternating powers); the second is the nilpotent regime ($\mathbf{Q}^2 = 0$, series truncating after the linear term). Since the scalar part is central,

$$
\exp(\tilde{Q}) = e^{Q_0}\exp(\mathbf{Q}) = e^{Q_0}\exp(\tilde{Q} - Q_0 e_0).
$$

**Basic properties.** The exponential takes values in $\mathbb{B}^\times$ (the exhibited factors are invertible), so it is never zero and never a zero divisor; its norm form is

$$
N(\exp \tilde{Q}) = e^{2Q_0} = e^{\mathrm{Tr}(\tilde{Q})},
$$

the matrix identity $\det(e^M) = e^{\mathrm{tr}(M)}$; and $d\exp_0 = \mathrm{id}_{\mathfrak{gl}(2,\mathbb{C})}$, so $\exp$ is a local diffeomorphism near $0$ and provides exponential coordinates near the identity.

## 4. The Group Law: $\exp(a)\exp(b)$ versus $\exp(a+b)$

The exponential is not a homomorphism from the additive group of the Lie algebra to the multiplicative group of the units. Its failure to be one is measured by the bracket.

**Commuting case.** If $[a,b] = 0$, then

$$
\exp(a)\exp(b) = \exp(a+b) = \exp(b)\exp(a).
$$

In particular, this holds when $a$ and $b$ lie in a common commutative subalgebra. For a single biquaternion $\tilde{Q}$, all elementary functions lie in the commutative subalgebra $\mathbb{C}[\tilde{Q}]$ generated by $e_0$ and $\tilde{Q}$, so the usual addition formula holds there.

**General case.** The Baker–Campbell–Hausdorff theorem gives, for sufficiently small $a, b$,

$$
\exp(a)\exp(b) = \exp\!\left(a + b + \frac{1}{2}[a,b] + \frac{1}{12}\bigl[a,[a,b]\bigr] - \frac{1}{12}\bigl[b,[a,b]\bigr] + \cdots\right),
$$

a convergent series of iterated brackets. Thus $\exp(a)\exp(b)$ differs from $\exp(a+b)$ by the term $\tfrac{1}{2}[a,b]$ and higher brackets, and the difference is invisible exactly when $[a,b] = 0$. For instance, with $a = e_1$ and $b = e_2$ the product $\exp(e_1)\exp(e_2)$ carries a term $\sin^2 1\, e_3$ that is absent from $\exp(e_1+e_2)$.

## 5. Surjectivity on $GL(2,\mathbb{C})$

**Theorem.** Every invertible complex $2 \times 2$ matrix has a complex logarithm, so $\exp : \mathfrak{gl}(2,\mathbb{C}) \to GL(2,\mathbb{C})$ is surjective. Equivalently,

$$
\mathbb{B}^\times = \exp(\mathbb{B}) = \{\exp(\tilde{L}) : \tilde{L} \in \mathbb{B}\}.
$$

The proof is the standard one: put the matrix in Jordan form and, for each Jordan block with nonzero eigenvalue $\lambda$, take a branch of $\log\lambda$ and the finite series for the logarithm of a unipotent block. This is the complex case of the general fact that $\exp$ is surjective onto $GL(n,\mathbb{C})$; it is special to the complex ground field. The biquaternion logarithm of the elementary-functions article, with its three closed-form branches ($B \neq 0$; $B = 0$, $\mathbf{Q} \neq 0$; $\mathbf{Q} = 0$), exhibits the surjectivity case by case. Thus $\exp(\mathbb{B})$ is the whole of $\mathbb{B}^\times$, not merely a neighbourhood of the identity.

## 6. The Kernel of the Exponential

Since $\exp$ is surjective onto $\mathbb{B}^\times$ but not injective, the fibre over the identity measures the ambiguity of the logarithm.

**Theorem.** For $\tilde{X} \in \mathfrak{gl}(2,\mathbb{C})$ one has $\exp(\tilde{X}) = e_0$ if and only if $\tilde{X}$ is diagonalizable over $\mathbb{C}$ and every eigenvalue of $\tilde{X}$ lies in $2\pi i\mathbb{Z}$.

**Proof.** If $\tilde{X}$ is diagonalizable with eigenvalues $\lambda_1, \lambda_2$, then $\exp(\tilde{X})$ is diagonalizable with eigenvalues $e^{\lambda_1}, e^{\lambda_2}$, and equals $I$ exactly when $e^{\lambda_1} = e^{\lambda_2} = 1$. Conversely, write $\tilde{X} = S + N$ with $S$ semisimple and $N$ nilpotent commuting. Then $\exp(\tilde{X}) = \exp(S)\exp(N)$ is the product of a semisimple and a unipotent factor; if it equals $I$, the unipotent factor is semisimple, hence trivial, so $N = 0$. $\square$

**Concrete description.** A $2 \times 2$ complex matrix lies in the kernel exactly when it is conjugate to $\mathrm{diag}(2\pi i m, 2\pi i n)$ with $m, n \in \mathbb{Z}$. The kernel is thus an infinite subset of $\mathfrak{gl}(2,\mathbb{C})$, not an additive subgroup, since $\exp$ is not a homomorphism. It contains the scalars $2\pi i k\, e_0$ but much more: $\mathrm{diag}(0, 2\pi i)$ also exponentiates to the identity.

**In biquaternion terms.** The eigenvalues of the matrix representing $\tilde{X}$ are $\lambda_\pm = Q_0 \pm iB$, with $B = \sqrt{Q_1^2 + Q_2^2 + Q_3^2}$. So $\exp(\tilde{X}) = e_0$ exactly when either $\mathbf{Q} = 0$ and $\tilde{X} = Q_0 e_0$ is a scalar with $Q_0 \in 2\pi i\mathbb{Z}$, or $B \neq 0$ and both $Q_0 \pm iB$ lie in $2\pi i\mathbb{Z}$. The second condition is equivalent to

$$
Q_0 = \pi i k, \qquad B = \pi j, \qquad k, j \in \mathbb{Z}, \quad k \equiv j \pmod 2,
$$

the eigenvalues then being $2\pi i(k\pm j)/2$. If $B = 0$ but $\mathbf{Q} \neq 0$, the matrix is a nonzero nilpotent, hence not diagonalizable and not in the kernel: $\exp(\mathbf{Q}) = e_0 + \mathbf{Q} \neq e_0$.

**Example.** The biquaternion $\tilde{X} = \pi i\, e_0 + \pi\, e_3$ has $Q_0 = \pi i$, $B = \pi$, so $k = j = 1$ and $\exp(\tilde{X}) = e^{\pi i}(\cos\pi\, e_0 + \sin\pi\, e_3) = e_0$. Since $N(\tilde{X}) = 0$, this kernel element is a zero divisor: the kernel is not contained in the group of units.

**On the phrase "eigenvalues differ by a multiple of $2\pi i$".** The condition implies such a difference, but the difference alone is weaker: $\tilde{X} = e_0$ has equal eigenvalues yet $\exp(e_0) \neq e_0$. Each eigenvalue must be a multiple of $2\pi i$.

## 7. Polar and Exponential Parametrisation of a Nonzero Biquaternion

Both parametrisations below apply to an element of $\mathbb{B}^\times$, i.e. to a nonzero biquaternion of nonzero norm form; a nonzero zero divisor has none, being no exponential.

**Hamilton polar form.** If $B \neq 0$, set $R = \sqrt{N(\tilde{Q})}$, $\hat{n} = \mathbf{Q}/B$, $\cos\Theta = Q_0/R$, $\sin\Theta = B/R$. Then

$$
\tilde{Q} = R\exp(\Theta\hat{n}) = R\bigl(\cos\Theta\, e_0 + \sin\Theta\, \hat{n}\bigr),
$$

with $R$ the complex modulus, $\Theta$ the complex angle, and $\hat{n}$ a root of $-1$ parallel to the vector part. The form is unique up to the correlated replacements $\hat{n} \mapsto -\hat{n}$, $\Theta \mapsto -\Theta$ and $R \mapsto -R$, $\Theta \mapsto \Theta + \pi$.

**Exponential parametrisation.** By the surjectivity of §5, every $\tilde{Q} \in \mathbb{B}^\times$ is

$$
\tilde{Q} = \exp(\tilde{L})
$$

for some $\tilde{L} \in \mathbb{B}$, with $\tilde{L}$ given by the branches of the biquaternion logarithm:

$$
\tilde{L} =
\begin{cases}
\log R\, e_0 + \Theta\hat{n}, & B \neq 0, \\[2mm]
\log Q_0\, e_0 + \dfrac{\mathbf{Q}}{Q_0}, & B = 0, \; \mathbf{Q} \neq 0, \\[2mm]
\log Q_0\, e_0, & \mathbf{Q} = 0.
\end{cases}
$$

The parametrisation is many-to-one, with the ambiguity of §6. The two constructions must not be confused: the Hamilton polar form uses the axis and angle **of $\tilde{Q}$**, whereas the closed form for $\exp(\tilde{Q})$ in §3 uses those of $\tilde{Q}$ read as an exponent; they agree only in special cases, such as $\tilde{Q}$ a scalar.

---

# Part II: Subgroups, Rotations and Hyperbolic Rotations, and the Lorentz Group

## 8. The Unit Quaternions and Their Complexification

The **unit quaternions** are the elements of $\mathbb{H}_{\mathbb{B}}$ of norm form $1$:

$$
S^3 = \{q \in \mathbb{H}_{\mathbb{B}} : N(q) = 1\} \cong SU(2) \cong Sp(1),
$$

a compact, connected, simply connected real Lie group of real dimension $3$. Every such $q$ is $\cos\theta\, e_0 + \sin\theta\, \hat{n}$ with $\hat{n}$ a real unit vector part, the quaternion exponential.

Complexifying the coefficients turns $N(q) = 1$ into the same equation over $\mathbb{C}$, giving the **unit-norm-form subgroup**

$$
SL(2,\mathbb{C}) = \{\tilde{Q} \in \mathbb{B} : N(\tilde{Q}) = 1\} = \{\tilde{Q} \in \mathbb{B}^\times : \det(\tilde{Q}) = 1\}.
$$

**Dimension.** The level set $N = 1$ has complex dimension $3$ and real dimension $6$, the norm form being a submersion wherever $N(\tilde{Q}) \neq 0$. The group $SL(2,\mathbb{C})$ is connected, simply connected, and non-compact, and it is the **complexification of the unit quaternions**: $\mathfrak{sl}(2,\mathbb{C}) = \mathfrak{su}(2) \otimes_{\mathbb{R}} \mathbb{C}$, and $SL(2,\mathbb{C})$ complexifies the compact group $SU(2) \cong S^3$. Its center is

$$
Z(SL(2,\mathbb{C})) = \{\pm e_0\} \cong \mathbb{Z}/2.
$$

## 9. The Lie Algebra $\mathfrak{sl}(2,\mathbb{C})$: Rotations and Hyperbolic Rotations

The Lie algebra of $SL(2,\mathbb{C})$ is the trace-free subalgebra

$$
\mathfrak{sl}(2,\mathbb{C}) = \{\tilde{Q} \in \mathbb{B} : Q_0 = 0\} = \mathrm{span}_\mathbb{C}\{e_1, e_2, e_3\},
$$

of complex dimension $3$ and real dimension $6$, closed under the bracket $[e_j,e_k] = 2\sum_l \epsilon_{jkl} e_l$. Over the reals it splits into two three-dimensional real subspaces,

$$
\mathfrak{sl}(2,\mathbb{C}) = \mathrm{span}_\mathbb{R}\{e_1,e_2,e_3\} \;\oplus\; \mathrm{span}_\mathbb{R}\{ie_1, ie_2, ie_3\},
$$

with real dimensions $6 = 3 + 3$. The first summand is the compact form $\mathfrak{su}(2) \cong \mathrm{span}_\mathbb{R}\{e_1,e_2,e_3\}$, the Lie algebra of spatial rotations, on which the bracket is (twice) the cross product; the second, $\mathrm{span}_\mathbb{R}\{ie_1,ie_2,ie_3\}$, consists of the generators of the hyperbolic rotations. The two are non-isomorphic real Lie algebras: one compact, one not.

In the fixed-point subspaces of the basic algebra article the rotation directions are $e_k \in \mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_-$ and the hyperbolic-rotation directions are $ie_k \in \mathbb{M}_+$. This is why pure spatial rotations have rotors in $\mathbb{H}_{\mathbb{B}}$ while pure hyperbolic rotations have rotors in $\mathbb{M}_+$: these are exactly the two real three-dimensional pieces into which $\mathfrak{sl}(2,\mathbb{C})$ splits. The central direction $\mathbb{C}e_0$ completes the picture, $\mathfrak{gl}(2,\mathbb{C}) = \mathfrak{sl}(2,\mathbb{C}) \oplus \mathbb{C}e_0$.

## 10. The Exponential of a Rotation and of a Hyperbolic Rotation

The two real summands of §9 exponentiate to two geometric families, with trigonometric and hyperbolic closed forms respectively. Let $\hat{n}$ be a real unit vector part, so that $\hat{n}^2 = -e_0$.

**Rotations (the bivector directions).** For real $\theta$,

$$
\exp(\theta\hat{n}) = \cos\theta\, e_0 + \sin\theta\, \hat{n},
$$

a unit quaternion in $\mathbb{H}_{\mathbb{B}} \subset SL(2,\mathbb{C})$, since $N = \cos^2\theta + \sin^2\theta = 1$. It rotates the vector part: conjugation by $\exp(\theta\hat{n})$ rotates any real vector $\mathbf{v}$ about the axis $\hat{n}$ through $2\theta$, the double-cover relation $SU(2) \to SO(3)$. The family has period $2\pi$ in $SU(2)$ and $4\pi$ for the rotation, since $\exp(2\pi\hat{n}) = -e_0$.

**Hyperbolic rotations (the vector directions).** With $(i\hat{n})^2 = +e_0$ and rapidity $\psi \in \mathbb{R}$,

$$
\exp(\psi\, i\hat{n}) = \cosh\psi\, e_0 + \sinh\psi\, i\hat{n}.
$$

This element is Hermitian, lies in $\mathbb{M}_+$, and has $N = \cosh^2\psi - \sinh^2\psi = 1$. Unlike the rotation family it is not periodic and is unbounded as $\psi \to \pm\infty$; it is the rotor of a Lorentz transformation along $\hat{n}$ with rapidity $\psi$. The set of hyperbolic rotations is not a subgroup: the product of two hyperbolic rotations in non-parallel directions is a hyperbolic rotation followed by a rotation.

**Comparison.** A general element of the Lorentz Lie algebra is $\tilde{Q} = q + iq'$ with $q, q'$ real vector parts; the rotation and hyperbolic families commute only when $q$ and $q'$ are parallel, since $[q, iq'] = 2i\,(q \times q')$, and in general the closed form of §3 with $Q_0 = 0$ mixes the two behaviours.

## 11. Subgroups and the Lorentz Group

The relevant subgroups are: $\mathbb{B}^\times \cong GL(2,\mathbb{C})$, the nonzero-norm elements (complex dimension $4$, real dimension $8$); $SL(2,\mathbb{C})$, the unit-norm elements (complex dimension $3$, real dimension $6$); the rotation group $SU(2)$, the unit-norm real quaternions (real dimension $3$); and the center $\mathbb{C}^\times e_0$ of nonzero scalars (complex dimension $1$, real dimension $2$).

$SU(2)$ is the maximal compact subgroup of $SL(2,\mathbb{C})$, with Lie algebra the compact form $\mathfrak{su}(2)$ of §9. The center $\{\pm e_0\}$ is discrete, and

$$
SL(2,\mathbb{C})/\{\pm e_0\} \cong PSL(2,\mathbb{C}) \cong SO^+(1,3),
$$

the proper orthochronous Lorentz group, of real dimension $6$. Hence $SL(2,\mathbb{C})$ is a two-sheeted cover of $SO^+(1,3)$ and, being simply connected, is its universal cover: it is the spin group of Lorentzian signature,

$$
SL(2,\mathbb{C}) \cong \mathrm{Spin}(3,1), \qquad \mathfrak{sl}(2,\mathbb{C}) \cong \mathfrak{so}(3,1).
$$

The Lorentz action is rotor conjugation, $\tilde{X} \mapsto \tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger$ for $\tilde{\Lambda} \in SL(2,\mathbb{C})$, which preserves $\mathbb{M}_-$ and $N(\tilde{X})$; its compact part is the rotation family of §10 and its non-compact part the hyperbolic rotations.

## 12. Surjectivity and Its Failure for the Subgroups

The exponential of the full unit group is surjective (§5), but the two distinguished subgroups behave differently.

**Rotations: surjective.** Every unit quaternion is $\cos\theta\, e_0 + \sin\theta\,\hat{n} = \exp(\theta\hat{n})$, so $\exp : \mathfrak{su}(2) \to SU(2)$ is surjective; this is the general fact that a connected compact Lie group has a surjective exponential map.

**Lorentz group: not surjective.** The exponential $\exp : \mathfrak{sl}(2,\mathbb{C}) \to SL(2,\mathbb{C})$ is **not** surjective: $SL(2,\mathbb{C})$ is not exponential. The element corresponding under §1 to $\begin{pmatrix} -1 & 1 \\ 0 & -1 \end{pmatrix} \in SL(2,\mathbb{C})$ is

$$
\tilde{Q} = -e_0 + \frac{i}{2}e_1 - \frac{1}{2}e_2, \qquad N(\tilde{Q}) = 1 + \left(\frac{i}{2}\right)^2 + \left(-\frac{1}{2}\right)^2 = 1.
$$

Its scalar part is $Q_0 = -1$ and its vector part has $B = 0$, so the representing matrix is non-diagonalizable with the repeated eigenvalue $-1$. If $\tilde{Q} = \exp(\tilde{X})$ with $\tilde{X} \in \mathfrak{sl}(2,\mathbb{C})$, then $X_0 = 0$, and $\tilde{X} = \mu e_0 + \tilde{N}$ with $\tilde{N}$ nilpotent and $e^\mu = -1$, hence $\mu \in i\pi(2\mathbb{Z}+1)$ and $\mathrm{Tr}(\tilde{X}) = 2\mu \neq 0$, a contradiction. The same obstruction makes $\exp$ non-surjective on $SL(2,\mathbb{R})$.

**Generation versus surjectivity.** Failure of surjectivity does not mean the exponentials fail to generate: since $SL(2,\mathbb{C})$ is connected and $\exp$ is a local diffeomorphism at $0$, the image $\exp(\mathfrak{sl}(2,\mathbb{C}))$ contains a neighbourhood of the identity and generates the group, while remaining a proper subset. Nor does simple connectivity force surjectivity: $SL(2,\mathbb{C})$ is simply connected, yet $\exp$ is not onto. The classical criteria (connected compact, connected nilpotent, or $GL(n,\mathbb{C})$) are sufficient, not necessary.

---

## Summary

The algebra $\mathbb{B}$ is simultaneously eight-dimensional over $\mathbb{R}$ and four-dimensional over $\mathbb{C}$, and every dimension statement names its field. As a complex Lie algebra it is $\mathfrak{gl}(2,\mathbb{C})$, the Lie algebra of the group of units $\mathbb{B}^{\times} \cong GL(2,\mathbb{C})$, and the exponential map is the matrix exponential transported across the isomorphism $\mathbb{B} \cong M_2(\mathbb{C})$: defined by the power series, computed in closed form by the elementary functions, surjective onto $\mathbb{B}^{\times}$ but not injective. Its kernel is the set of elements diagonalizable over $\mathbb{C}$ all of whose eigenvalues lie in $2\pi i\mathbb{Z}$, and this fibre over the identity measures the ambiguity of the logarithm. Every nonzero element of nonzero norm form has both a Hamilton polar form $R\exp(\Theta\hat{n})$ and an exponential parametrisation; a nonzero zero divisor has neither, being no exponential.

The trace-free subalgebra $\mathfrak{sl}(2,\mathbb{C}) = \mathrm{span}_{\mathbb{C}}\{e_1,e_2,e_3\}$ has complex dimension $3$ and real dimension $6$, splitting over $\mathbb{R}$ into the compact form $\mathfrak{su}(2) = \mathrm{span}_{\mathbb{R}}\{e_1,e_2,e_3\}$ of the rotations and the non-compact $\mathrm{span}_{\mathbb{R}}\{ie_1,ie_2,ie_3\}$ of the hyperbolic rotations; these sit in $\mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_-$ and in $\mathbb{M}_+$ respectively, and the central direction completes $\mathfrak{gl}(2,\mathbb{C}) = \mathfrak{sl}(2,\mathbb{C}) \oplus \mathbb{C}e_0$.

The subgroups are the units, the unit-norm elements $SL(2,\mathbb{C})$, the rotation group $SU(2)$ (the maximal compact subgroup, the unit-norm real quaternions), and the center $\mathbb{C}^{\times}e_0$. Since $SL(2,\mathbb{C})/\{\pm e_0\} \cong PSL(2,\mathbb{C}) \cong SO^{+}(1,3)$, the unit-norm group is the spin group $\mathrm{Spin}(3,1)$ and the universal cover of the proper orthochronous Lorentz group, acting by rotor conjugation $\tilde{X} \mapsto \tilde{\Lambda}\tilde{X}\tilde{\Lambda}^{\dagger}$, which preserves $\mathbb{M}_-$ and the norm form.

Surjectivity of the exponential is not uniform over these groups. It is surjective onto $SU(2)$, a connected compact group, but it is **not** surjective onto $SL(2,\mathbb{C})$: the Lorentz group is not exponential, the obstruction being a non-diagonalizable element with the repeated eigenvalue $-1$, and the same obstruction applies to $SL(2,\mathbb{R})$. Failure of surjectivity does not prevent generation — the image contains a neighbourhood of the identity and generates the connected group — and simple connectivity does not force surjectivity, since $SL(2,\mathbb{C})$ is simply connected while $\exp$ is not onto.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ | Biquaternion algebra; $\mathfrak{gl}(2,\mathbb{C})$ as a complex Lie algebra |
| $\tilde{Q} = Q_0 e_0 + \mathbf{Q}$ | Biquaternion; $\mathbf{Q} = \sum_k Q_k e_k$ |
| $B = \sqrt{Q_1^2+Q_2^2+Q_3^2}$, $\hat{n} = \mathbf{Q}/B$ | Complex norm and axis of the vector part, $\hat{n}^2 = -e_0$ |
| $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}}$ | Norm form; $\tilde{Q}$ is a unit iff $N(\tilde{Q}) \neq 0$ |
| $\mathbb{B}^{\times} \cong GL(2,\mathbb{C})$ | Group of units; complex dimension $4$, real dimension $8$ |
| $SL(2,\mathbb{C})$ | Unit-norm elements; complex dimension $3$, real dimension $6$ |
| $SU(2)$ | Unit-norm real quaternions; maximal compact subgroup, real dimension $3$ |
| $\mathbb{C}^{\times}e_0$ | Center of the group of units; nonzero complex scalars |
| $\mathfrak{sl}(2,\mathbb{C}) = \{Q_0 = 0\}$ | Trace-free subalgebra, $\mathrm{span}_{\mathbb{C}}\{e_1,e_2,e_3\}$ |
| $\mathfrak{su}(2)$ | Compact form, the rotation directions $e_k$ |
| $\mathrm{span}_{\mathbb{R}}\{ie_1,ie_2,ie_3\}$ | Non-compact part of $\mathfrak{sl}(2,\mathbb{C})$, the hyperbolic-rotation directions |
| $\exp$ | Exponential map of $\mathbb{B}^{\times}$ and of its subgroups |
| $\tilde{\Lambda}\tilde{X}\tilde{\Lambda}^{\dagger}$ | Lorentz action by rotor conjugation |

## Further Reading

- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations: An Elementary Introduction* (Springer, 2nd ed. 2015), for the exponential map, its surjectivity on $GL(n,\mathbb{C})$, and the matrix logarithm.
- John Stillwell, *Naive Lie Theory* (Springer, 2008), for an elementary treatment of $SU(2)$, $SL(2,\mathbb{C})$, and the double cover of the rotation group.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), for the exponential, polar forms, and norms of biquaternions.
- S. J. Sangwine, T. A. Ell, and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* **21** (2011) 607–636, for the biquaternion exponential and polar forms.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras and the spin groups.
