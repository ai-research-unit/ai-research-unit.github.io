
# __Hyperbolic Rotations__

## Introduction

This article describes the group of linear transformations of the split complex plane that preserve the split norm, and its realisation by the algebra $\mathbb{D} = \mathbb{R}[j]$, $j^2 = +1$. It is the split complex counterpart of *Rotations and Reflections in the Complex Plane*, written in parallel: there the unit circle acts by multiplication and its group is identified with the compact rotation group $SO(2)$, whereas here the unit hyperbola acts by multiplication and its identity component is identified with $SO(1,1)$, a group isomorphic to the additive line. The transformations are the **hyperbolic rotations**, and they are treated here only as a group of linear transformations of a plane, with no physical interpretation invoked.

The split complex algebra and its conjugation $\bar A = a - ja'$ are taken from *Split-Complex Algebra*; the split norm $N(A) = A\bar A = a^2 - a'^2$, its polarisation and the group of units are the form and the distance of *Split-Complex Norm and Invertibility*; and the idempotents $\Pi_\pm = \tfrac12(1\pm j)$ are taken from *Split-Complex Idempotents and Projections*. The vocabulary of quadratic forms, polar forms and orthogonal groups is that of *Isometries and Orthogonal Transformations*, and the Lie algebra of a matrix group is that of *The Orthogonal Lie Algebra*. The base field throughout is $\mathbb{R}$, so that $2$ is invertible and every isometry of a non-degenerate form is a linear automorphism; the coefficients $a, a'$ of $A = a + ja'$ are always real, and $\mathbb{D}$ is written in the basis $\{1, j\}$.

Two features distinguish the theory from its complex counterpart and organise everything below. The norm $N$ is indefinite, of signature $(1,1)$, so the set $\{N = 0\}$ is a pair of lines, the **null cone**, rather than the single point of the complex case; and the unit group $\{N = 1\}$ is a hyperbola with two branches rather than a circle, so the rotation group is non-compact and its exponential is injective. The null cone is also the zero-divisor set of $\mathbb{D}$, so the group theory developed here and the failure of the Cauchy theory recorded below have the same locus.

## The Form and Its Isometries

### The Bilinear Form

The **split bilinear form** on $\mathbb{D}$ is the polarisation of the norm $N$ of *Split-Complex Norm and Invertibility*; in explicit terms it is

$$
g(A, B) = \operatorname{Re}(\bar A B) = \frac{1}{2}\big(N(A + B) - N(A) - N(B)\big), \qquad A, B \in \mathbb{D}.
$$

In the real basis $\{1, j\}$, with $A = a + ja'$ and $B = b + jb'$,

$$
g(A, B) = ab - a'b', \qquad N(A) = g(A, A) = a^2 - a'^2.
$$

**Proposition.** The form $g$ is symmetric and bilinear, its matrix in the basis $\{1, j\}$ is

$$
G = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix},
$$

it is non-degenerate of signature $(1,1)$, and its null set is the **null cone**

$$
\{A : N(A) = 0\} = \{A : A_+ = 0 \text{ or } A_- = 0\}.
$$

**Proof.** Bilinearity and symmetry follow from the definition through $N$ and from the explicit formula $ab - a'b'$. The matrix is read off from $g(1,1) = 1$, $g(1,j) = 0$, $g(j,j) = -1$, and $\det G = -1 \neq 0$, so the form is non-degenerate with one positive and one negative square, that is, signature $(1,1)$. Since $N(A) = A_+A_-$, the null set is the union of the two lines $A_+ = 0$ and $A_- = 0$.

The two null lines are the real spans of $\Pi_1$ and of $\Pi_2$ respectively. They are the lines on which the form vanishes, and equivalently the lines of zero divisors of the ring: a non-zero element is a zero divisor exactly when it lies on the cone.

### The Orthogonal Group

**Definition.** The **orthogonal group** of the form is

$$
O(1,1) = \{T \in GL_2(\mathbb{R}) : N(TA) = N(A) \text{ for all } A \in \mathbb{D}\}.
$$

The **special orthogonal group** is $SO(1,1) = \{T \in O(1,1) : \det T = 1\}$, and $SO^+(1,1)$ is its identity component.

**Proposition.** For a linear map $T : \mathbb{D} \to \mathbb{D}$ the condition $N(TA) = N(A)$ for all $A$ is equivalent to $g(TA, TB) = g(A, B)$ for all $A, B$. Consequently every element of $O(1,1)$ is invertible, and $O(1,1)$ is a group.

**Proof.** If $N \circ T = N$ then, by bilinearity of $g$ and linearity of $T$,

$$
2g(TA, TB) = N(T(A + B)) - N(TA) - N(TB) = N(A + B) - N(A) - N(B) = 2g(A, B),
$$

and $2$ is invertible. The converse is the case $A = B$. If $N(TA) = N(A)$ and $TA = 0$, then $g(A, B) = g(TA, TB) = 0$ for every $B$, so $A = 0$ by non-degeneracy of $g$; hence $T$ is injective, and being linear on a finite-dimensional space it is invertible.

The determinant of an isometry is $\pm 1$, since $(\det T)^2 \det G = \det G$ and $\det G \neq 0$; thus $SO(1,1)$ is the kernel of the determinant on $O(1,1)$ and has index two in $O(1,1)$.

### Isometries Are Multiplications and Reflections

**Theorem.** A bijective linear map $T : \mathbb{D} \to \mathbb{D}$ is an isometry of $N$ if and only if there exists $u \in \mathbb{D}$ with $N(u) = 1$ such that either

$$
T(A) = uA \quad \text{for all } A, \qquad \text{or} \qquad T(A) = u\bar A \quad \text{for all } A.
$$

In the first case $\det T = 1$ and in the second $\det T = -1$.

**Proof.** Both maps preserve $N$: $N(uA) = N(u)N(A) = N(A)$ and $N(u\bar A) = N(u)N(\bar A) = N(A)$, since $N(\bar A) = N(A)$ and the norm is multiplicative. This proves the converse, and the determinant statement follows from $\det M_u = N(u) = 1$ for the matrix $M_u$ of multiplication, computed below, together with $\det \mathrm{diag}(1,-1) = -1$ for conjugation.

Conversely, let $T$ preserve $N$ and put $u = T(1)$. Then $N(u) = N(1) = 1$. Since $g(T(1), T(j)) = g(1, j) = 0$, the vector $T(j)$ lies in the $g$-orthogonal complement $u^\perp$. That complement is one-dimensional, spanned by $ju$: indeed $g(u, ju) = \operatorname{Re}(\bar u\, ju) = \operatorname{Re}(j\,\bar u u) = N(u)\operatorname{Re}(j) = 0$, since $\bar u u = N(u)$ is real, and $ju \neq 0$. So $T(j) = \lambda\, ju$ for some real $\lambda$. Taking norms,

$$
-1 = N(T(j)) = N(\lambda\, ju) = \lambda^2 N(ju) = \lambda^2 N(j) N(u) = -\lambda^2,
$$

so $\lambda = \pm 1$. If $\lambda = 1$ then $T$ fixes $1 \mapsto u$ and $j \mapsto ju$, hence by linearity $T(A) = uA$ for $A = a + ja'$. If $\lambda = -1$ then $T(j) = -ju$, and $T(A) = au - a'ju = u(a - ja') = u\bar A$.

The two families are the rotations and the reflections. They are disjoint, since a map of the first form is $\mathbb{D}$-linear while a map of the second is not: $S_u(j\cdot 1) = S_u(j) = -ju \neq j S_u(1) = ju$. Every isometry is therefore either a rotation or a reflection, and the determinant distinguishes the two.

## The Unit Hyperbola and Its Branches

### The Units and the Norm-One Group

By *Split-Complex Norm and Invertibility*, an element $A \in \mathbb{D}$ is a unit exactly when $N(A) \neq 0$, with $A^{-1} = \bar A/N(A)$, and the norm is a surjective group homomorphism $N : \mathbb{D}^\times \to \mathbb{R}^\times$ with kernel the norm-one group $\mathcal{H} = \{u : N(u) = 1\}$. So $\mathbb{D}^\times$ is the complement of the null cone, and $N$ presents it as an extension of $\mathbb{R}^\times$ by $\mathcal{H}$; the unit group, its four components and its exponential parametrisation are treated in *Split-Complex Norm and Invertibility* and *Split-Complex Exponential and Lie Group Structure*.

### The Unit Hyperbola

**Definition.** The **unit hyperbola** is

$$
\mathcal{H} = \{u \in \mathbb{D} : N(u) = 1\} = \{u = a + ja' : a^2 - a'^2 = 1\}.
$$

**Theorem.** The map

$$
\phi \longmapsto e^{\phi j} = \cosh\phi + j \sinh\phi, \qquad \mathbb{R} \longrightarrow \mathcal{H},
$$

is a group isomorphism onto the component $\mathcal{H}^+ = \{u \in \mathcal{H} : \operatorname{Re} u > 0\}$ of $\mathcal{H}$. The other component is $\mathcal{H}^- = -\mathcal{H}^+ = \{u \in \mathcal{H} : \operatorname{Re} u < 0\}$, and $\mathcal{H} = \mathcal{H}^+ \sqcup \mathcal{H}^-$ with $\operatorname{Re} u$ of constant sign on each component.

**Proof.** The split complex exponential $\exp(B) = \sum B^n/n!$ converges for every $B$, and $e^{\phi j} = \cosh\phi + j\sinh\phi$ because $j^{2m} = 1$ and $j^{2m+1} = j$; this follows also from the addition formula. Then $N(e^{\phi j}) = \cosh^2\phi - \sinh^2\phi = 1$, so the image lies in $\mathcal{H}$, and $e^{\phi j}e^{\psi j} = e^{(\phi+\psi)j}$ since $j$ commutes with scalars and $j^2 = 1$. So the map is a homomorphism from $(\mathbb{R},+)$. It is injective, because $\cosh\phi \geq 1$ determines $|\phi|$ and $\sinh\phi$ determines the sign, and it is surjective onto $\mathcal{H}^+$, since for $u = a + ja' \in \mathcal{H}^+$ the number $\phi = \operatorname{arsinh} a'$ is real and then $a = \cosh\phi \geq 1$ is forced by $a^2 - a'^2 = 1$ and $a > 0$. The component $\mathcal{H}^-$ is the negative of $\mathcal{H}^+$, and $\operatorname{Re} u$ cannot vanish on $\mathcal{H}$ because that would give $-a'^2 = 1$.

The parameter $\phi$ is the **hyperbolic angle** of the unit $u$; it is also called the rapidity. Since the branch sign $\epsilon$ is carried separately, $\phi$ is a coordinate on all of $\mathcal{H}$, one copy of $\mathbb{R}$ for each branch; and it is defined modulo nothing at all, because the exponential is injective, in contrast with $e^{i\theta}$, whose kernel is $2\pi\mathbb{Z}$. Half of the difference between the two theories is already visible here.

### Components and Polar Decomposition

**Theorem.** The unit group has exactly four connected components, and

$$
\mathbb{D}^\times \cong \mathbb{R}_{>0} \times \mathbb{R} \times (\mathbb{Z}/2\mathbb{Z})^2
$$

as a group, with the isomorphism sending $A$ to $(\rho, \phi, \sigma_+, \sigma_-)$ where $\rho = \sqrt{|N(A)|}$, $\sigma_\pm = \operatorname{sgn} A_\pm \in \{\pm 1\}$ and

$$
A = \rho\,\big(\sigma_+ \Pi_1 + \sigma_- \Pi_2\big)e^{\phi j}.
$$

**Proof.** The map $A \mapsto (A_+, A_-)$ is a ring isomorphism $\mathbb{D} \to \mathbb{R} \times \mathbb{R}$, hence restricts to an isomorphism of unit groups, and $(A^{-1})_\pm = A_\pm^{-1}$. Each factor $\mathbb{R}^\times$ is $\mathbb{R}_{>0} \times \{\pm1\}$ through $t \mapsto (|t|, t/|t|)$. Hence $\mathbb{D}^\times \cong \mathbb{R}_{>0}^2 \times (\mathbb{Z}/2)^2$, which has four components and is isomorphic to $\mathbb{R}_{>0} \times \mathbb{R} \times (\mathbb{Z}/2)^2$ because $\mathbb{R}_{>0}^2 \cong \mathbb{R}_{>0} \times \mathbb{R}_{>0}$ and $\mathbb{R}_{>0} \cong \mathbb{R}$ by the logarithm. In the coordinates $(A_+, A_-)$ the identity component is $A_+ > 0$, $A_- > 0$, and the norm there is positive; transporting back through $e^{\phi j}$ gives the stated form. The factors of the isomorphism are the two moduli $\lvert A_+ \rvert, \lvert A_- \rvert$, written as the geometric mean $\rho$ and the ratio $e^{2\phi}$, and the two signs $\sigma_\pm$.

For non-zero $A$, the factorisation $A = \rho u$ with $\rho > 0$ and $N(u) = \pm 1$ is the **polar decomposition** of a split complex number, the analogue of $A = |A|\,u$ in the complex case, with the circle replaced by the union of the two hyperbolas $N = 1$ and $N = -1$. The unit group is not compact, because the branch $\mathcal{H}^+$ is a hyperbola, and it is abelian, as the multiplicative group of a commutative ring must be.

### The Branches as Orbits

**Proposition.** The identity component $SO^+(1,1)$ acts simply transitively on each branch $\mathcal{H}^\pm$ of the unit hyperbola, and on each of the two branches of the hyperbola $\{N = -1\}$.

**Proof.** For $u = e^{\alpha j}$ and the parametrisation $e^{\phi j}$ of a branch, $R_u(e^{\phi j}) = e^{(\alpha+\phi)j}$, which is a free and transitive action of $(\mathbb{R},+)$ on the branch by translation of the parameter; the same computation applies to the branch $-\mathcal{H}^+$ and, after multiplying by $j$, to the branches of $\{N = -1\}$.

## Hyperbolic Rotations

### Multiplication by a Norm-One Unit

**Definition.** For $u \in \mathcal{H}$ the **hyperbolic rotation** determined by $u$ is

$$
R_u : \mathbb{D} \to \mathbb{D}, \qquad R_u(A) = uA.
$$

**Theorem.** For every $u \in \mathcal{H}$, the map $R_u$ is an isometry of $N$, with $R_u R_v = R_{uv}$ and $R_u^{-1} = R_{u^{-1}} = R_{\bar u}$. Consequently

$$
\mathcal{H} \longrightarrow SO(1,1), \qquad u \mapsto R_u,
$$

is a group isomorphism and $R_u$ has determinant $1$.

**Proof.** The isometry property is $N(uA) = N(u)N(A) = N(A)$. The composition law is associativity of multiplication, and $u^{-1} = \bar u$ when $N(u) = 1$, by the inversion formula. Injectivity of $u \mapsto R_u$ is clear at $A = 1$, and surjectivity onto $SO(1,1)$ is the determinant-one half of the classification theorem.

**Proposition (matrix form).** In the basis $\{1, j\}$, write $u = a + ja'$. Then

$$
R_u \ \longleftrightarrow \ M_u = \begin{pmatrix} a & a' \\ a' & a \end{pmatrix}, \qquad \det M_u = a^2 - a'^2 = N(u).
$$

**Proof.** $R_u(1) = u = a\cdot 1 + a'\cdot j$ and $R_u(j) = uj = (a+ja')j = a' + aj$, which are the two columns. The determinant is $a^2 - a'^2$.

So the matrices of the form $\begin{pmatrix} a & a'\\ a' & a\end{pmatrix}$ constitute a two-dimensional family, and the rotation group is cut out inside it by the single equation $N(u) = 1$: the group $SO(1,1) = \{M_u : N(u) = 1\}$ is the hyperbola $a^2 - a'^2 = 1$, a curve with two branches, and $SO^+(1,1)$ is the branch $a > 0$, which the angle parametrises.

### The Hyperbolic Angle

**Definition.** Every $u \in \mathcal{H}$ has a unique expression $u = \epsilon\, e^{\phi j}$ with **branch sign** $\epsilon = \pm 1$ and **hyperbolic angle** $\phi \in \mathbb{R}$; the branch sign is $+1$ on $\mathcal{H}^+$ and $-1$ on $\mathcal{H}^-$.

**Proposition.** Let $u = \epsilon e^{\alpha j}$ and $v = \eta e^{\beta j}$ with $\epsilon, \eta \in \{\pm 1\}$. Then

$$
uv = \epsilon\eta\, e^{(\alpha+\beta)j}.
$$

Hence the hyperbolic angle is additive, $\operatorname{angle}(uv) = \alpha + \beta$, and the branch sign multiplies; both are homomorphisms from $\mathcal{H}$ to $\mathbb{R}$ and to $\{\pm1\}$ respectively.

**Proof.** Since $e^{\alpha j}e^{\beta j} = e^{(\alpha+\beta)j}$ and $\epsilon, \eta, e^{\alpha j}, e^{\beta j}$ all commute, the product formula follows, and both stated homomorphism properties are read off from it.

The angle is the group coordinate of the identity component: it identifies $SO^+(1,1)$ with the additive group of real numbers, and it is the logarithm of the eigenvalues $e^{\pm\phi}$ of the corresponding rotation matrix, as the idempotent decomposition below makes explicit.

### Diagonal Form in Idempotent Coordinates

The idempotent decomposition gives the simplest description of a hyperbolic rotation.

**Theorem.** Let $u = e^{\phi j} \in \mathcal{H}^+$. In the idempotent coordinates $A = A_+\Pi_1 + A_-\Pi_2$ the rotation $R_u$ acts diagonally:

$$
R_u : \ (A_+, A_-) \longmapsto (e^{\phi}A_+, \ e^{-\phi}A_-), \qquad u = e^{\phi}\Pi_1 + e^{-\phi}\Pi_2.
$$

Equivalently, $R_u$ fixes each null line and scales the two primitive idempotents by reciprocal positive factors, and it preserves the product $N(A) = A_+A_-$.

**Proof.** Since $\Pi_1 j = \Pi_1$ and $\Pi_2 j = -\Pi_2$, one has $e^{\phi j} = e^{\phi}\Pi_1 + e^{-\phi}\Pi_2$. Multiplying a split complex number in the idempotent basis is componentwise, so the action is as stated. The product $A_+A_-$ is multiplied by $e^{\phi}e^{-\phi} = 1$; the two null lines $A_- = 0$ and $A_+ = 0$ are preserved.

**Remark.** The name *hyperbolic rotation* records the action on the hyperbola, not a rotation of the Euclidean plane. In the Euclidean coordinates $a, a'$ the map is a squeeze: the lines $a' = \pm a$ are fixed and the hyperbolas $N = \text{const}$ are traced out, with the point $(1,0)$ moving along the branch to $(\cosh\phi, \sinh\phi)$. Euclidean angles are not preserved; the invariant is the indefinite form $N$.

### Composition and the Additive Group

**Theorem.** The map $\phi \mapsto M_\phi$ is an isomorphism of groups

$$
(\mathbb{R}, +) \longrightarrow SO^+(1,1), \qquad M_\phi = \begin{pmatrix} \cosh\phi & \sinh\phi \\ \sinh\phi & \cosh\phi \end{pmatrix},
$$

so $SO^+(1,1)$ is abelian and isomorphic to the additive group of the line.

**Proof.** By the theorem above, $R_{e^{\alpha j}}R_{e^{\beta j}} = R_{e^{(\alpha+\beta)j}}$, so the correspondence preserves the group law, and it is bijective because $\phi \mapsto e^{\phi j}$ parametrises $\mathcal{H}^+$ bijectively.

So the "rotation group of the split plane" is the real line, and the composition of two hyperbolic rotations is the addition of their angles; the two-element group of the sign of $a$ supplies the second component of $SO(1,1)$.

### The Matrix Form and the Hyperbolic Functions

Writing out the action of $M_\phi$ on $A = a + ja'$,

$$
M_\phi(a, a') = (a\cosh\phi + a'\sinh\phi,\ a\sinh\phi + a'\cosh\phi),
$$

which is the pair of transformation laws

$$
a' = a\cosh\phi + a'\sinh\phi, \qquad a'' = a\sinh\phi + a'\cosh\phi.
$$

The multiplicativity of the correspondence between rotations and angles is exactly the pair of addition theorems of the hyperbolic functions,

$$
\cosh(\alpha + \beta) = \cosh\alpha\cosh\beta + \sinh\alpha\sinh\beta, \qquad \sinh(\alpha+\beta) = \sinh\alpha\cosh\beta + \cosh\alpha\sinh\beta,
$$

because the product of the matrices $M_\alpha$ and $M_\beta$ is $M_{\alpha+\beta}$. The trace of $M_\phi$ is $2\cosh\phi \geq 2$, with equality only at $\phi = 0$; thus every element of the identity component has trace at least $2$, in sharp contrast with the Euclidean rotation matrix, whose trace is $2\cos\theta$ and fills the interval $[-2,2]$.

### The Exponential and the Lie Algebra

**Definition.** The **orthogonal Lie algebra** of the form is

$$
\mathrm{SO}(1,1) = \{X \in \mathrm{GL}_2(\mathbb{R}) : X^T G + G X = 0\}.
$$

**Proposition.** $\mathrm{SO}(1,1)$ is one-dimensional, spanned by

$$
J = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix},
$$

and is abelian: $[J, J] = 0$. The exponential map

$$
\exp : \mathrm{SO}(1,1) \longrightarrow SO^+(1,1), \qquad \exp(tJ) = \begin{pmatrix} \cosh t & \sinh t \\ \sinh t & \cosh t \end{pmatrix},
$$

is a bijection, and in particular $SO^+(1,1)$ is simply connected and contractible.

**Proof.** For $X = \begin{pmatrix} p & q\\ r & s\end{pmatrix}$ the condition reads $2p = 0$, $q = r$, $2s = 0$, so $X = qJ$; the bracket vanishes in one dimension. Since $J^2 = I$, the exponential series gives $\exp(tJ) = I\cosh t + J\sinh t$, the stated matrix. The map $t \mapsto \exp(tJ)$ is the isomorphism of the previous section, hence bijective.

**Remark.** In the complex plane the analogous map $\mathrm{SO}(2) \to SO(2)$ is surjective but not injective, with kernel $2\pi\mathbb{Z}$, because the exponential of an imaginary number is periodic. Here $J^2 = I$, the exponential is a diffeomorphism onto the identity component, and the group is non-compact. The passage from the Lie algebra to the group loses nothing on the identity component, but the exponential does not see the other components of $O(1,1)$: no $t$ gives $-I$ or a reflection.

### The Group Law in Hyperbolic Coordinates

The additive coordinate $\phi$ can be replaced by a bounded one, which exhibits the group law in the form familiar from the addition formula for the hyperbolic tangent.

**Proposition.** The map $\phi \mapsto s = \tanh\phi$ is a bijection $\mathbb{R} \to (-1,1)$, and it transports the additive law to the operation

$$
s \star t = \frac{s + t}{1 + st}, \qquad s, t \in (-1, 1).
$$

With this operation, $(-1,1)$ is a group isomorphic to $SO^+(1,1)$.

**Proof.** $\tanh$ is a strictly increasing bijection of $\mathbb{R}$ onto $(-1,1)$. The identity $\tanh(\alpha+\beta) = (\tanh\alpha + \tanh\beta)/(1 + \tanh\alpha\tanh\beta)$ is the quotient of the two addition theorems above, and it becomes the stated law under the identification $s = \tanh\alpha$, $t = \tanh\beta$.

The quantity $s = \tanh\phi$ is bounded, while $\phi$ is not, and the group law on the interval is the one that makes the two ends $\pm 1$ infinitely far from the identity. The parametrisation is the split complex analogue of the tangent half-angle substitution, with the circle replaced by the hyperbola.

## Reflections

### Anti-Linear Isometries

**Definition.** For $u \in \mathcal{H}$ the **reflection** determined by $u$ is

$$
S_u : \mathbb{D} \to \mathbb{D}, \qquad S_u(A) = u\bar A.
$$

**Theorem.** For every $u \in \mathcal{H}$ the map $S_u$ is an isometry of $N$ with $\det S_u = -1$ and $S_u^2 = \mathrm{id}$; it is $\mathbb{R}$-linear but not $\mathbb{D}$-linear. In the basis $\{1,j\}$ it has the matrix

$$
M_u\, \kappa, \qquad \kappa = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}.
$$

**Proof.** $N(u\bar A) = N(u)N(\bar A) = N(A)$, since $N(\bar A) = N(A)$. Conjugation has matrix $\kappa$ and determinant $-1$, the matrix $M_u$ has determinant $1$, so $\det S_u = -1$. That $S_u$ is an involution is $u\overline{u\bar A} = u\bar u A = A$ because $u\bar u = N(u) = 1$. Finally $S_u(j) = u\bar j = -uj = -j u \neq jS_u(1) = ju$, so $S_u$ is not $\mathbb{D}$-linear.

So the reflections are the anti-linear isometries, exactly as in the complex plane, where they are the maps $A \mapsto u\bar A$. The element $u = 1$ gives the plain conjugation $\bar\cdot$, whose matrix is $\kappa$.

### Fixed Lines

**Theorem.** Let $u = e^{\phi j} \in \mathcal{H}^+$. Then $S_u$ fixes pointwise the line

$$
L_+ = \mathbb{R}\big(\cosh(\phi/2), \ \sinh(\phi/2)\big),
$$

whose generator $(\cosh(\phi/2),\sinh(\phi/2))$ has norm $\cosh^2(\phi/2) - \sinh^2(\phi/2) = 1$, and negates the $g$-orthogonal line

$$
L_- = \mathbb{R}\big(\sinh(\phi/2), \ \cosh(\phi/2)\big),
$$

whose generator has norm $-1$. These are the two eigenspaces of $S_u$, with eigenvalues $+1$ and $-1$; the norm of a generator, not the norm of an arbitrary element, is what is meant here, the norm varying along each line.

**Proof.** In the idempotent coordinates $u = e^{\phi}\Pi_1 + e^{-\phi}\Pi_2$ and $\bar A = A_-\Pi_1 + A_+\Pi_2$, so

$$
S_u(A) = e^{\phi}A_-\, \Pi_1 + e^{-\phi}A_+\, \Pi_2.
$$

The fixed condition $S_u(A) = A$ is therefore $A_+ = e^{\phi}A_-$, a line in the $(A_+,A_-)$-plane; transporting a direction $A_+ = e^{\phi}t$, $A_- = t$ to the coordinates $a = (A_++A_-)/2$, $a' = (A_+-A_-)/2$ gives $(a,a') = t\,e^{\phi/2}(\cosh(\phi/2),\sinh(\phi/2))$, which is $L_+$, with norm $t^2e^{\phi}$ vanishing nowhere on $L_+ \setminus \{0\}$. Because $S_u$ preserves $g$, it preserves the $g$-orthogonal complement $L_+^\perp$, which is one-dimensional and spanned by $(\sinh(\phi/2),\cosh(\phi/2))$, a vector of norm $-1$; indeed the two generators are $g$-orthogonal because $\cosh(\phi/2)\sinh(\phi/2) - \sinh(\phi/2)\cosh(\phi/2) = 0$. The eigenvalues of $S_u$ are the roots of $\lambda^2 - (\operatorname{tr} S_u)\lambda + \det S_u = \lambda^2 - 1$, namely $\pm 1$, so $S_u$ acts on $L_+^\perp$, which the fixed line does not meet, by the eigenvalue $-1$.

**Example.** For $u = 1$ (angle $\phi = 0$) the reflection is plain conjugation: it fixes the real axis and negates the $j$-axis. For $u = -1$ the reflection is $A \mapsto -\bar A$, and direct computation shows that it fixes the imaginary axis $\mathbb{R}j$ and negates the real axis. For $u = e^{\phi j}$ with $\phi \neq 0$, the fixed line is the tilted line $L_+$ above, which is neither of the coordinate axes. In general, for $u = \epsilon e^{\phi j}$ with $\epsilon = \pm 1$, the fixed line has a generator of norm $\epsilon$ and the negated line a generator of norm $-\epsilon$; the sign of $u$ exchanges the roles of the two eigenspaces.

### Reflections Permute the Null Lines

**Proposition.** Every reflection $S_u$ interchanges the two null lines and every rotation $R_u$ preserves each of them.

**Proof.** $\overline{\Pi_1} = \Pi_2$ and $\overline{\Pi_2} = \Pi_1$, so $\bar\cdot$ swaps the two null lines $\mathbb{R}\Pi_1$ and $\mathbb{R}\Pi_2$. For $u = \epsilon e^{\phi j} \in \mathcal{H}$ one has $u \Pi_1 = \epsilon e^{\phi}\Pi_1$ and $u \Pi_2 = \epsilon e^{-\phi}\Pi_2$, non-zero multiples of $\Pi_1$ and of $\Pi_2$, so multiplication by $u$ preserves each line separately. Hence $S_u$ swaps the lines and $R_u$ fixes them.

So the null lines are the fixed directions of the rotation group and the exchanged directions of the reflection coset. Since the null lines are the zero-divisor cone of *Split-Complex Algebra* and the characteristic set of the Cauchy–Riemann operator, this is the group-theoretic statement that the rotations preserve the cone and the reflections permute its two halves.

### Composition of Two Reflections

**Theorem.** Let $u, v \in \mathcal{H}$. Then

$$
S_u \circ S_v = R_{u\bar v}, \qquad R_u \circ S_v = S_{uv}, \qquad S_u \circ R_v = S_{u\bar v}.
$$

In particular the composition of two reflections is a rotation, and the composition of a reflection with a rotation is a reflection.

**Proof.** Directly, $S_u(S_v(A)) = u\overline{v\bar A} = u\bar v A = R_{u\bar v}(A)$, since $\overline{\bar A} = A$; the other two identities are the same computation. Moreover $N(u\bar v) = N(u)N(v) = 1$, so $u\bar v \in \mathcal{H}$ and $R_{u\bar v}$ is a rotation.

**Corollary (angles).** If $u = e^{\alpha j}$ and $v = e^{\beta j}$, then $S_u S_v = R_{e^{(\alpha-\beta)j}}$; the composition of two reflections is the rotation whose angle is the difference of their angles.

**Proof.** $\bar v = e^{-\beta j}$, so $u\bar v = e^{(\alpha-\beta)j}$.

**Corollary (Cartan–Dieudonné, dimension two).** Every element of $O(1,1)$ is a product of at most two reflections: the identity is $S_1 \circ S_1$, a reflection is itself, and a rotation is $R_u = S_u \circ S_1$.

**Proof.** $S_u(S_1(A)) = u\overline{\bar A} = uA = R_u(A)$ for every $A$, and the classification theorem lists the elements of $O(1,1)$ as the rotations and the reflections.

**Proposition (conjugacy of the reflections).** For $u, B \in \mathcal{H}$,

$$
R_B \, S_u \, R_B^{-1} = S_{B^2u}, \qquad S_B \, S_u \, S_B^{-1} = S_{B^2\bar u},
$$

so conjugation by an element of $O(1,1)$ maps the branch $\mathcal{H}^+$ of the parameter to itself and likewise $\mathcal{H}^-$; each $S_u$ with $u \in \mathcal{H}^+$ is conjugate to $S_1$, and each $S_u$ with $u \in \mathcal{H}^-$ to $S_{-1}$. The reflections therefore fall into exactly two conjugacy classes, one for each branch of $\mathcal{H}$.

**Proof.** Since $N(B) = 1$ gives $B^{-1} = \bar B$ and hence $R_B^{-1} = R_{\bar B}$, the rules $S_aR_b = S_{a\bar b}$ and $R_aS_b = S_{ab}$ give

$$
R_BS_uR_B^{-1} = R_BS_uR_{\bar B} = R_BS_{uB} = S_{B^2u},
$$

and the second identity is $S_BS_uS_B^{-1} = S_BS_uS_B = R_{B\bar u}S_B = S_{B^2\bar u}$, because $S_B$ is an involution. Write $B = \epsilon e^{\phi j}$; then $B^2 = e^{2\phi j} \in \mathcal{H}^+$ has both idempotent coordinates positive, and $\bar u$ has the two idempotent coordinates of $u$ in the opposite order, so $B^2u$ and $B^2\bar u$ lie in the branch of $u$. Given $u, v \in \mathcal{H}^+$, the element $B = \sqrt{v/u}$ lies in $\mathcal{H}^+$ and satisfies $B^2u = v$, so the first identity conjugates $S_u$ to $S_v$; in particular each such $S_u$ is conjugate to $S_1$. The same argument inside $\mathcal{H}^-$ conjugates every $S_u$ there to $S_{-1}$. Since conjugation always preserves the branch of the parameter, the two sets are distinct, and they are the two conjugacy classes.

In $O(2)$, where every unit is a square, the reflections form a single conjugacy class; here the two branches of $\mathcal{H}$ separate them, exactly as the two branches separate $SO(1,1)$ from $-SO(1,1)$.

## The Orthogonal Group $O(1,1)$

### The Four Components

Write $M_\phi$ for the matrix of $R_{e^{\phi j}}$ and $\kappa = \mathrm{diag}(1,-1)$ for that of conjugation, so that the matrix of $S_{e^{\phi j}}$ is $M_\phi\kappa$.

**Theorem.** Every element of $O(1,1)$ has exactly one of the four forms

$$
\pm M_\phi, \qquad \pm M_\phi \kappa, \qquad \phi \in \mathbb{R},
$$

and the following table describes them, where $\operatorname{Re} u$ denotes the first column entry $a$ of the corresponding $u = a + ja'$.

| Matrix | Determinant | Sign of $a = \operatorname{Re} u$ | Map | Component of $O(1,1)$ |
|---|---|---|---|---|
| $M_\phi$ | $+1$ | $+$ | $A \mapsto uA$ | identity |
| $-M_\phi$ | $+1$ | $-$ | $A \mapsto -uA$ | proper, $a < 0$ |
| $M_\phi\kappa$ | $-1$ | $+$ | $A \mapsto u\bar A$ | reflection, $a > 0$ |
| $-M_\phi\kappa$ | $-1$ | $-$ | $A \mapsto -u\bar A$ | reflection, $a < 0$ |

**Proof.** By the classification theorem every isometry is $R_u$ or $S_u$ with $N(u) = 1$. If $u \in \mathcal{H}^+$, then $u = e^{\phi j}$ and the matrix is $M_\phi$ or $M_\phi\kappa$; if $u \in \mathcal{H}^-$, then $u = -e^{\phi j}$ and the matrix is $-M_\phi$ or $-M_\phi\kappa$. The determinant is read off from $\det M_\phi = 1$ and $\det\kappa = -1$, and the first entry of the first column is $\operatorname{Re} u$, whose sign is that of the branch of $\mathcal{H}$ containing $u$.

The table shows that $O(1,1)$ has four connected components, indexed by the sign of the determinant and by the branch of $u$, and that each is a copy of $\mathbb{R}$.

### The Semidirect Product Structure

**Theorem.** There are isomorphisms of groups

$$
SO(1,1) \cong \mathbb{R} \times \mathbb{Z}/2\mathbb{Z}, \qquad O(1,1) \cong SO(1,1) \rtimes \mathbb{Z}/2\mathbb{Z},
$$

the second $\mathbb{Z}/2\mathbb{Z}$ being generated by the conjugation $\kappa$.

**Proof.** The map $(\phi, \sigma) \mapsto (-1)^\sigma e^{\phi j}$ is a group isomorphism $(\mathbb{R},+) \times \mathbb{Z}/2 \to \mathcal{H}$, because $-1$ is central of order two and $(-1)e^{\phi j} = -e^{\phi j}$; applying $u \mapsto R_u$ gives the first isomorphism. For the second, $O(1,1) = SO(1,1) \cup SO(1,1)\kappa$, and $\kappa^2 = \mathrm{id}$, so the union is a semidirect product once the action of $\kappa$ on $SO(1,1)$ is known: conjugation by $\kappa$ inverts the angle, $\kappa M_\phi \kappa^{-1} = M_{-\phi}$, as is checked by matrix multiplication.

So the rotation subgroup is normal and its complement is a single coset, the extension being split by $\kappa$. The identity component is $SO^+(1,1) \cong \mathbb{R}$.

### The Centre and the Lie Algebra

**Theorem.** The centre of $O(1,1)$ is $\{\pm I\}$. The group $SO(1,1)$ is abelian, so its centre is $SO(1,1)$ itself; the centre of the identity component $SO^+(1,1)$ is $SO^+(1,1)$. The Lie algebra of both is $\mathrm{SO}(1,1) = \mathbb{R}J$; the exponential has image the identity component $SO^+(1,1)$, and is not surjective onto $O(1,1)$.

**Proof.** A matrix $X = \begin{pmatrix} p & q \\ r & s\end{pmatrix}$ commuting with every $M_\phi$ commutes with $M_\phi - M_0 = (\cosh\phi - 1)I + \sinh\phi\, J$, hence with $J$, and the equation $XJ = JX$ gives $q = r$ and $p = s$, so $X = \begin{pmatrix} p & q \\ q & p\end{pmatrix}$. For such an $X$, the condition $X\kappa = \kappa X$ forces $q = 0$, and then $X \in O(1,1)$ forces $p = \pm 1$; hence the centre of $O(1,1)$ is $\{\pm I\}$. Since $M_\alpha M_\beta = M_{\alpha+\beta} = M_\beta M_\alpha$, the group $SO(1,1) = \{M_\phi\} \cup \{-M_\phi\}$ is abelian and equals its own centre; so does its identity component. The Lie algebra was computed above, and $\exp(\mathrm{SO}(1,1)) = \{M_\phi\} = SO^+(1,1)$; the element $-I$, which is $M_\phi$ for no real $\phi$, and the reflections are not in the image.

**Remark.** Both $SO(2)$ and $SO^+(1,1)$ are abelian, and both are the image of the exponential of a one-dimensional abelian Lie algebra; what separates them is that $SO(2)$ is compact and the exponential winds around it, whereas $SO^+(1,1)$ is non-compact and contractible. The identity component here is a line, so it is simply connected and its only connected covering is itself; the passage from $\mathrm{SO}(1,1)$ to $SO^+(1,1)$ is a diffeomorphism, while the exponential misses the other component of $SO(1,1)$ and the reflection coset entirely.

## The Null Cone and the Sectors

### The Null Cone

**Proposition.** The null cone $\{N = 0\}$ is the union of the two lines $\mathbb{R}\Pi_1$ and $\mathbb{R}\Pi_2$; its non-zero elements are exactly the zero divisors of $\mathbb{D}$, and $\Pi_1$ and $\Pi_2$ are the primitive idempotents.

**Proof.** $N(A) = A_+A_-$, which vanishes exactly when $A_+ = 0$ or $A_- = 0$; these are the lines spanned by $\Pi_2$ and $\Pi_1$ respectively. An element $B$ is a zero divisor exactly when it is not a unit, that is, when $N(B) = 0$, by the unit criterion.

The cone is therefore at once the zero-divisor set, the complement of the unit group, the obstruction to the Cauchy integral formula. It is the locus common to the algebra, the analysis and the group theory of the plane.

### The Sectors and the Action

**Definition.** The four **sectors** of the split plane are the connected components of the complement of the null cone, namely

$$
\{A : A_+ > 0, A_- > 0\}, \quad \{A : A_+ > 0, A_- < 0\}, \quad \{A : A_+ < 0, A_- > 0\}, \quad \{A : A_+ < 0, A_- < 0\}.
$$

They are indexed by the pair of signs $(\operatorname{sgn} A_+, \operatorname{sgn} A_-)$, and $N$ has the sign of the product.

**Theorem.** Every hyperbolic rotation $R_u$ preserves each of the four sectors. A reflection $S_u$ with $u \in \mathcal{H}^+$ preserves the two sectors in which $A_+$ and $A_-$ have the same sign and interchanges the two in which they have opposite signs. Every isometry of $N$ preserves the value of $N$, hence its sign, and the sign of $N$ is positive exactly on the two sectors with $A_+A_- > 0$.

**Proof.** $R_u$ multiplies $A_+$ by $e^{\phi} > 0$ and $A_-$ by $e^{-\phi} > 0$, so both signs are unchanged and $N = A_+A_-$ is unchanged in value. The conjugation $\bar\cdot$ interchanges $A_+$ and $A_-$, so it interchanges the two signs; multiplying by $u \in \mathcal{H}^+$ changes neither sign, and $u_+u_- = N(u) = 1$, so $S_u$ maps the sign pair $(s_+, s_-)$ to $(s_-, s_+)$ and leaves the product $A_+A_-$ unchanged. Hence the equal-sign sectors are preserved and the opposite-sign sectors are swapped. All isometries preserve $N$ by definition of $O(1,1)$.

So the identity component of the isometry group acts on the four sectors trivially at the level of the discrete invariant, while the reflection coset acts by the swap on the two mixed-sign sectors, and the group of components of $O(1,1)$ is $(\mathbb{Z}/2\mathbb{Z})^2$, one factor for the branch of $u$ and one for the determinant.

### The Hyperbola and Its Asymptotes

The norm-one hyperbola $a^2 - a'^2 = 1$ has the two null lines as asymptotes; it meets each sector with $N > 0$ in one branch, and the hyperbola $N = -1$ meets each sector with $N < 0$ in one branch. The identity component of the rotation group acts simply transitively on each branch, and the whole rotation group $SO(1,1)$ acts transitively on each *pair* of branches of a given hyperbola. The orbit of a point under the rotation group is the hyperbola through it, and the two null lines, with the origin removed, are the two non-trivial orbits of the cone: each line is preserved setwise by every rotation and fixed pointwise by none except the identity.

## Comparison with the Complex Case

The two theories are the positive-definite and indefinite cases of the same construction: the unit group of the norm acting on the plane by multiplication.

| Property | Complex | Split complex |
|---|---|---|
| Norm | $a^2 + a'^2$, signature $(2,0)$ | $a^2 - a'^2$, signature $(1,1)$ |
| Null cone | $\{0\}$, no null directions | two null lines, the zero divisors |
| Norm-one group | circle $U(1)$, compact, connected | hyperbola $\mathcal{H}$, non-compact, two branches |
| Rotation group | $SO(2) \cong U(1) \cong \mathbb{R}/2\pi\mathbb{Z}$ | $SO^+(1,1) \cong \mathbb{R}$, $SO(1,1) \cong \mathbb{R} \times \mathbb{Z}/2$ |
| Angle | $\theta$, defined mod $2\pi$ | $\phi \in \mathbb{R}$, no period |
| Exponential | $e^{i\theta} = \cos\theta + i\sin\theta$, periodic | $e^{j\phi} = \cosh\phi + j\sinh\phi$, injective |
| Exponential map | $\mathbb{R} \to SO(2)$ surjective, kernel $2\pi\mathbb{Z}$ | $\mathbb{R} \to SO^+(1,1)$ bijective |
| Reflection | $S_u(A) = u\bar A$, fixes a line | $S_u(A) = u\bar A$, fixes a line |
| Conjugacy classes of the reflections | one | two, one for each branch of $\mathcal{H}$ |
| Two reflections | compose to a rotation | compose to a rotation |
| Orthogonal group | $O(2) \cong U(1) \rtimes \mathbb{Z}/2$, two components | $O(1,1) \cong SO(1,1) \rtimes \mathbb{Z}/2$, four components |
| Trace of a rotation matrix | $2\cos\theta \in [-2,2]$ | $2\cosh\phi \geq 2$ |

The complex rotation group is compact and the angle is periodic, so a rotation is described by a point of a circle; the split rotation group is a line and the angle is a real parameter. In both cases multiplication by a unit, rather than conjugation by it, is the natural action of a commutative algebra on itself, and in both cases the reflections are the anti-linear isometries $A \mapsto u\bar A$; what differs is the shape of the unit set, and hence the topology and the type of the group. One further contrast belongs here: an isometry of the Euclidean plane is a translation composed with a linear isometry, whereas the indefinite form admits no translation at all, since $N(A+b) = N(A)$ for all $A$ gives $2g(A,b) + N(b) = 0$ for all $A$, hence $g(A,b) = 0$ for all $A$ and $b = 0$ by non-degeneracy of $g$. The isometry group of $N$ is therefore the linear group $O(1,1)$ itself.

## Summary

The split plane carries the indefinite **norm** $N(a+ja') = a^2 - a'^2$ of signature $(1,1)$ and its **polar form** $g(A,B) = ab - a'b'$. The **isometries** of $N$ are exactly the maps $A \mapsto uA$ and $A \mapsto u\bar A$ with $N(u) = 1$; the first family is the rotation subgroup with determinant $1$ and the second the reflection coset with determinant $-1$. The **unit group** $\mathbb{D}^\times$ is the complement of the null cone, with four components and polar decomposition $A = \rho u$, $\rho > 0$, $N(u) = \pm 1$.

The **unit hyperbola** $\mathcal{H} = \{N = 1\}$ has two branches, parametrised by the **hyperbolic angle** through $u = e^{\phi j} = \cosh\phi + j\sinh\phi$, and $\mathcal{H}^+ \cong \mathbb{R}$ via the additive angle. The **hyperbolic rotation** $R_u(A) = uA$ is an isometry, realises $\mathcal{H}$ as $SO(1,1)$ through $u \mapsto R_u$, and in the idempotent coordinates is the diagonal map $(A_+, A_-) \mapsto (e^{\phi}A_+, e^{-\phi}A_-)$, a squeeze that preserves the product $A_+A_-$ and hence the form. The composition law is the addition of angles, $SO^+(1,1) \cong (\mathbb{R},+)$, and the group law transported to the interval $(-1,1)$ by $s = \tanh\phi$ is $s \star t = (s+t)/(1+st)$. The Lie algebra is $\mathrm{SO}(1,1) = \mathbb{R}J$ with $J^2 = I$, and the exponential is a bijection onto the identity component.

The **reflection** $S_u(A) = u\bar A$ has determinant $-1$, is an involution, fixes a line pointwise and negates the $g$-orthogonal line, interchanges the two null lines, and satisfies $S_uS_v = R_{u\bar v}$: the composition of two reflections is the rotation whose angle is the difference of their angles. Every element of $O(1,1)$ is a product of at most two reflections, since $R_u = S_uS_1$, and the reflections form exactly two conjugacy classes, one for each branch of $\mathcal{H}$, because conjugation sends $S_u$ to $S_{B^2u}$ or to $S_{B^2\bar u}$ and $B^2$ always lies in $\mathcal{H}^+$. The orthogonal group has **four components**, $O(1,1) \cong SO(1,1) \rtimes \mathbb{Z}/2$ with $SO(1,1) \cong \mathbb{R} \times \mathbb{Z}/2$, its centre is $\{\pm I\}$, and the null cone, which is the zero-divisor set, divides the plane into four sectors that the rotations preserve and the reflections swap.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D} = \mathbb{R}[j]$, $j^2 = +1$ | Split complex numbers |
| $A = a + ja'$ | General split complex number, $a = \operatorname{Re} A$, $a' = \operatorname{Im} A$ |
| $\bar A = a - ja'$ | Split complex conjugate |
| $N(A) = A\bar A = a^2 - a'^2$ | Norm, signature $(1,1)$ |
| $g(A,B) = \operatorname{Re}(\bar A B) = ab - a'b'$ | Polar bilinear form of $N$ |
| $G = \operatorname{diag}(1,-1)$ | Matrix of $g$ in the basis $\{1,j\}$ |
| $\{N = 0\}$ | Null cone, the zero-divisor set |
| $\Pi_1 = \tfrac12(1+j), \ \Pi_2 = \tfrac12(1-j)$ | Idempotents, $\Pi_\pm^2 = \Pi_\pm$, $\Pi_1\Pi_2 = 0$ |
| $A = A_+\Pi_1 + A_-\Pi_2$, $A_+ = a+a'$, $A_- = a-a'$ | Idempotent decomposition and coordinates |
| $\mathbb{D}^\times$, $\mathbb{R}^\times$ | Unit groups of $\mathbb{D}$ and of $\mathbb{R}$; $\mathbb{R}_{>0}$ the positive reals |
| $\mathbb{Z}/2\mathbb{Z}$, $\rtimes$ | The two-element group, and the semidirect product |
| $O(1,1)$ | Orthogonal group of $N$ |
| $SO(1,1)$, $SO^+(1,1)$ | Determinant-one subgroup and its identity component |
| $\mathcal{H} = \{N = 1\}$, $\mathcal{H}^\pm$ | Unit hyperbola and its two branches |
| $\phi$ | Hyperbolic angle (the rapidity), defined on all of $\mathcal{H}$ |
| $\epsilon = \pm 1$ | Branch sign of a unit, $u = \epsilon\, e^{\phi j}$; a second unit's sign is written $\eta$ |
| $\sigma_\pm = \operatorname{sgn} A_\pm$ | Signs of the idempotent coordinates of a unit |
| $e^{\phi j} = \cosh\phi + j\sinh\phi$ | Split exponential of an angle |
| $R_u(A) = uA$ | Hyperbolic rotation determined by $u$ |
| $M_\phi = \begin{pmatrix}\cosh\phi & \sinh\phi\\ \sinh\phi & \cosh\phi\end{pmatrix}$ | Matrix of $R_{e^{\phi j}}$ |
| $S_u(A) = u\bar A$ | Reflection determined by $u$; $S_1 = \bar{\cdot}$ is conjugation |
| $L_\pm$, $L_+^\perp$ | Fixed and negated lines of a reflection |
| $\kappa = \operatorname{diag}(1,-1)$ | Matrix of conjugation |
| $\mathrm{SO}(1,1) = \mathbb{R}J$, $J = \begin{pmatrix}0&1\\1&0\end{pmatrix}$ | Orthogonal Lie algebra, abelian |
| $\exp : \mathrm{SO}(1,1) \to SO^+(1,1)$ | Matrix exponential, a bijection |
| $s = \tanh\phi \in (-1,1)$ | Bounded angle coordinate, law $s \star t = \frac{s+t}{1+st}$ |
| $\rho = \sqrt{\lvert N(A)\rvert}$ | Positive factor of the polar decomposition |

## Further Reading

- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the systematic use of $A \mapsto uA$ and $A \mapsto u\bar A$ as rotations and reflections of the split plane.
- Felix Klein, *Vorlesungen über nicht-euklidische Geometrie* (Springer, 1928), for the projective treatment of non-Euclidean geometry and its isometries.
- Carl Ludwig Siegel, *Topics in Complex Function Theory, Vol. I* (Wiley, 1969), for the exponential, the argument and the contrast between the periodic and the injective cases.
- Michael Artin, *Algebra* (Prentice Hall, 2nd ed. 2011), for the structure of orthogonal groups, semidirect products and the classification of isometries of a plane.
- John Stillwell, *Naive Lie Theory* (Springer, 2008), for the exponential map, the Lie algebra $\mathrm{SO}(1,1)$ and the topology of the rotation groups.
- Vladimir V. Kisil, *Geometry of Möbius Transformations: Elliptic, Parabolic and Hyperbolic Actions of $SL(2,\mathbb{R})$* (Imperial College Press, 2012), for the hyperbolic action and its comparison with the elliptic one.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the split complex numbers as a Clifford algebra and the null cone as its zero-divisor set.
