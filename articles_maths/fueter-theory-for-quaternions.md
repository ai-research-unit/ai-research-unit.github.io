
# __Fueter Theory for Quaternions__

## Introduction

Fueter theory is the four-variable function theory attached to the quaternion algebra: a first-order operator, the class of functions it annihilates, and a construction that produces those functions from holomorphic functions of one complex variable. This article develops that theory for $\mathbb{H}$, whose definite norm makes it the classical and unobstructed case. It is the quaternion member of the family's Fueter-theory pair; its counterpart is the biquaternion case, where the indefinite form introduces the null cone and the imaginary units are no longer a sphere. Here the imaginary units form the sphere $S^2$, the only singularity of the theory is the origin, and the Fueter construction holds in the form Fueter gave it.

The article uses *Quaternion Regular Functions* for the Cauchy–Riemann operator and its conjugate, the regularity system, harmonicity and the Cauchy integral formula; *Quaternion Roots of Minus One* for the sphere of imaginary units; *Quaternion Special Functions* for the exponential; *Quaternion Integration* for the fundamental solution and the mean value property; and *Clifford Algebras in Finite Dimensions* for the Clifford identifications. It does not re-derive the Cauchy formula, which belongs to *Quaternion Regular Functions*. The Clifford analysis referred to below is the function theory of the Cauchy–Riemann operator on the even Clifford algebra; the biquaternion comparison is *Fueter Theory for Biquaternions*.

The corpus's default base is a commutative ring with identity; the analysis requires the real numbers, so domains are taken in $\mathbb{R}^4$ and functions are quaternion-valued.

Throughout, $\mathbb{H}$ is the quaternion algebra over $\mathbb{R}$ with basis $e_0 = 1, e_1, e_2, e_3$, $e_k^2 = -e_0$; the variable is $\tilde q = q_0+\mathbf{q}$, $\mathbf{q} = q_1e_1+q_2e_2+q_3e_3$, with $\rho = |\mathbf{q}|$ and, for $\rho>0$, the direction $\hat{\mathbf{q}} = \mathbf{q}/\rho$. The partials are $\partial_\mu = \partial/\partial q_\mu$, and $\Delta_4 = \sum_\mu\partial_\mu^2$ is the four-dimensional Laplacian. Vector operations on $\mathbf{F} = F_1e_1+F_2e_2+F_3e_3$ are as in *Quaternion Regular Functions*.

## The Fueter Operator

### Definition and Conjugate

**Definition.** The **Fueter operator**, also called the **Cauchy–Riemann–Fueter operator**, is the quaternion-valued first-order operator

$$
D = \partial_0+\mathbf{D} = \sum_{\mu=0}^{3}e_\mu\partial_\mu, \qquad D F = \sum_{\mu=0}^{3}e_\mu\partial_\mu F,
$$

acting on the left, with $\mathbf{D} = e_1\partial_1+e_2\partial_2+e_3\partial_3$. Its **conjugate** is $\bar D = \partial_0-\mathbf{D} = \sum_\mu e_\mu^{\natural}\partial_\mu$, obtained by negating the vector part, $e_0^{\natural} = e_0$, $e_k^{\natural} = -e_k$.

**Remark.** The Fueter operator is the Cauchy–Riemann operator of *Quaternion Regular Functions*, under the name used in the Fueter tradition; it is the same operator and this article does not restate its definition independently.

### Factorization of the Laplacian

**Theorem.** On $\mathbb{H}$ the operator and its conjugate factor the Laplacian,

$$
D\bar D = \bar DD = \Delta_4 ,
$$

so $D$ is a square root of $\Delta_4$.

*Proof.* Expand $D\bar D = \sum_{\mu,\nu}e_\mu e_\nu^{\natural}\partial_\mu\partial_\nu$. The diagonal term is $\sum_\mu e_\mu e_\mu^{\natural}\partial_\mu^2 = \sum_\mu\partial_\mu^2$, since $e_0e_0^{\natural} = 1$ and $e_k e_k^{\natural} = -e_k^2 = 1$; for $\mu\neq\nu$ the coefficient is $e_\mu e_\nu^{\natural}+e_\nu e_\mu^{\natural} = 0$ by the Clifford relation of *Quaternion Regular Functions*. Hence all mixed terms cancel, leaving $\Delta_4$; the same argument gives $\bar DD = \Delta_4$.

### Relation to the Cauchy–Riemann Operator

Since $\mathbf{D}^2 = -\Delta_3$ on the vector part, the product $(\partial_0+\mathbf{D})(\partial_0-\mathbf{D})$ equals $\partial_0^2+\Delta_3 = \Delta_4$, so the Fueter operator is the four-dimensional Cauchy–Riemann operator up to normalization. On a slice $\mathbb{C}_I$ (below) the part differentiating along the slice is the classical operator $\partial_{q_0}+I\partial_\rho$, so $DF = 0$ is the quaternionic Cauchy–Riemann equation. In the Clifford language of *Clifford Algebras in Finite Dimensions*, the quaternion algebra is the even subalgebra of $\mathrm{Cl}_{0,3}$,

$$
\mathbb{H}\cong\mathrm{Cl}^0_{0,3}\cong\mathrm{Cl}_{0,2},
$$

and the Fueter operator is the restriction of the first-order Clifford operator of that even algebra; for this reason Fueter-regular functions are called **monogenic**.

## Fueter-Regular Functions

### Left and Right Regularity

**Definition.** Let $F : \Omega\to\mathbb{H}$ be differentiable on an open $\Omega\subseteq\mathbb{H}$. Then $F$ is **left-regular**, or **Fueter-regular**, if $DF = 0$, and **right-regular** if $F D = \sum_\mu\partial_\mu F\,e_\mu = 0$.

**Proposition.** Left-regular functions form a right $\mathbb{H}$-module, $D(Fa) = (DF)a = 0$ for constant $a$; right-regular functions form a left module, $(aF)D = a(FD) = 0$. Neither class is two-sided in general, and conjugation exchanges the two: $DF = 0\iff\bar F\bar D = 0$.

*Proof.* Both regularities are linear and are preserved by multiplication by a constant on the appropriate side; the exchange by conjugation is *Quaternion Regular Functions*.

### The Componentwise System

**Theorem.** Writing $F = F_0+\mathbf{F}$, the operator decomposes as

$$
DF = \bigl(\partial_0F_0-\mathrm{div}\,\mathbf{F}\bigr) + \bigl(\partial_0\mathbf{F}+\mathrm{grad}\,F_0+\mathrm{rot}\,\mathbf{F}\bigr),
$$

so left-regularity is the **quaternionic Cauchy–Riemann system**

$$
\partial_0F_0 = \mathrm{div}\,\mathbf{F}, \qquad \partial_0\mathbf{F} = -\mathrm{grad}\,F_0-\mathrm{rot}\,\mathbf{F},
$$

one quaternion equation, equivalently four real equations for the four coefficients. The right action gives the same system with $+\mathrm{rot}\,\mathbf{F}$ in the second equation, so the two systems differ only in the sign of the curl and coincide when $\mathrm{rot}\,\mathbf{F} = 0$.

*Proof.* Multiplication out of $e_\mu\partial_\mu(F_0+\mathbf{F})$ with $\mathbf{a}\mathbf{b} = -\langle\mathbf{a},\mathbf{b}\rangle+\mathbf{a}\times\mathbf{b}$; the right action reverses the order of $e_\mu$ and the differentiated component.

**Corollary.** The system is elliptic, with principal symbol $s(\xi) = \sum_\mu\xi_\mu e_\mu$ invertible for every real $\xi\neq0$, since $s(\xi)s^{\natural}(\xi) = |\xi|^2e_0$; hence Fueter-regular functions are real-analytic.

### The Debye-Type Reformulation of the System

The system can also be written, away from the origin, as identities that trade each first-order equation for a radial derivative of one component and angular derivatives of the others. The rewriting is classical in one complex variable, and it is the source of the name.

**The complex case.** Let $f_0(A) = u(a,a')+iv(a,a')$ be holomorphic on a disc, put $\mathbf{a} = (a,a')$ with $\rho = |\mathbf{a}|>0$, and write $[\mathbf{a}\times\nabla g]_3 = a\,\partial_{a'} g-a'\,\partial_a g$ for the out-of-plane component of the two-dimensional cross product. The Cauchy–Riemann relations are equivalent to the two identities

$$
u = (\hat{\mathbf{a}}\cdot\nabla)(\rho u) - [\mathbf{a}\times\nabla v]_3 ,
\qquad
v = (\hat{\mathbf{a}}\cdot\nabla)(\rho v) + [\mathbf{a}\times\nabla u]_3 .
$$

Since $(\hat{\mathbf{a}}\cdot\nabla)(\rho g) = g+a\partial_ag+a'\partial_{a'}g$, the first identity states $0 = a\partial_au+a'\partial_{a'}u-[\mathbf{a}\times\nabla v]_3$ and the second states $0 = a\partial_av+a'\partial_{a'}v+[\mathbf{a}\times\nabla u]_3$; the Cauchy–Riemann relations imply both, and conversely the two rows $(a,a',a',-a)$ and $(-a',a,a,a')$ in the partials $(\partial_au,\partial_{a'}u,\partial_av,\partial_{a'}v)$ are orthogonal and their span contains $(1,0,0,-1)$ and $(0,1,1,0)$, so away from $\rho = 0$ the pair is equivalent to $\partial_au = \partial_{a'}v$, $\partial_{a'}u = -\partial_av$. The rewriting is called **Debye** because the two real scalars $\psi_E,\psi_M$ that generate the source-free Maxwell solutions and satisfy the wave equation are the **Debye potentials**: the identity is the sense in which an analytic function serves as its own Debye potential, the cross term playing the role of the companion component.

**The quaternion case.** The same contraction applies to the quaternion system. For $F = F_0+\mathbf{F}$ regular with $\mathbf{F} = F_1e_1+F_2e_2+F_3e_3$, and $\mathbf{q} = q_1e_1+q_2e_2+q_3e_3$, $\rho = |\mathbf{q}|>0$, the component $F_0$ satisfies

$$
F_0 = (\hat{\mathbf{q}}\cdot\nabla)(\rho F_0) + \partial_0(\mathbf{q}\cdot\mathbf{F}) + (\mathbf{q}\times\nabla F_1)_1+(\mathbf{q}\times\nabla F_2)_2+(\mathbf{q}\times\nabla F_3)_3 ,
$$

and the three companions are obtained by applying the same statement to $-Fe_1$, $-Fe_2$, $-Fe_3$, each again regular, since $D(Fc) = (DF)c$ for a constant $c$ and the scalar component of $-Fe_j$ is $F_j$. The companion for $F_1$ reads

$$
F_1 = (\hat{\mathbf{q}}\cdot\nabla)(\rho F_1) + \partial_0(-q_1F_0-q_2F_3+q_3F_2) - (\mathbf{q}\times\nabla F_0)_1-(\mathbf{q}\times\nabla F_3)_2+(\mathbf{q}\times\nabla F_2)_3 ,
$$

and the remaining two follow the same pattern; in each case one component is expressed through its own radial derivative, the $q_0$-derivative of the inner product of the radius with the other three, and the components of $\mathbf{q}\times\nabla$ of those three.

**Structural content.** The identity for $F_0$ collapses. Because $(\hat{\mathbf{q}}\cdot\nabla)(\rho F_0) = F_0+\mathbf{q}\cdot\nabla F_0$ and $\sum_k(\mathbf{q}\times\nabla F_k)_k = \mathbf{q}\cdot\mathrm{rot}\,\mathbf{F}$, the term $F_0$ cancels on the two sides and the relation states

$$
0 = \mathbf{q}\cdot\bigl(\partial_0\mathbf{F}+\mathrm{grad}\,F_0+\mathrm{rot}\,\mathbf{F}\bigr) ,
$$

which is the vector part of $DF$ contracted with the radius. Each of the four relations is therefore the radius contraction of one component equation of the system, and every regular $F$ satisfies it; the vector part vanishes in each radial direction precisely because it vanishes outright. The four relations together are a **reformulation** of the system in the source's sense — each component is recovered from radial and angular derivatives of the four — and the source notes that they are not explicitly found in the literature; they are an identity satisfied by regular functions rather than a construction of them, the construction remaining Fueter's.

## Harmonicity and the Mean Value Property

**Theorem.** Every left- or right-regular function is harmonic,

$$
DF = 0\ \text{or}\ FD = 0 \implies \Delta_4 F = 0
$$

componentwise, and the converse fails.

*Proof.* $DF = 0$ gives $\Delta_4F = \bar D(DF) = 0$, and $FD = 0$ gives $\Delta_4F = (FD)\bar D = 0$. The coordinate $q_0$ is harmonic with $Dq_0 = e_0\neq0$.

**Theorem (mean value property).** A regular function $F$ near a closed ball $\bar B(q_0,r)$ satisfies

$$
F(q_0) = \frac{1}{|B(q_0,r)|}\int_{B(q_0,r)}F\,dV = \frac{1}{|\partial B(q_0,r)|}\int_{\partial B(q_0,r)}F\,dS,
$$

with the ordinary Lebesgue measures on $\mathbb{R}^4$.

*Proof.* By the preceding theorem each component of $F$ is harmonic, and the mean value property for harmonic functions gives the two equalities; equivalently, the property follows from the Cauchy integral formula of *Quaternion Regular Functions* by shrinking the boundary of the ball.

**Corollary.** Regular functions satisfy the maximum principle, Liouville's theorem, the identity theorem and the Cauchy estimates on $\mathbb{H}$; all of these are consequences of harmonicity together with ellipticity, and none of them requires an exceptional set because the quaternion norm is definite.

## The Fueter Construction

### The Axial Extension of a Holomorphic Function

**Definition.** Let $f_0$ be holomorphic on the disc $D(0,R)\subseteq\mathbb{C}$, written $f_0(A) = u(a,a')+iv(a,a')$ with $A = a+ia'$ and $u,v$ real-valued. The **axial extension** of $f_0$ is

$$
\tilde f_0(\tilde q) = u(q_0,\rho)+\hat{\mathbf{q}}\,v(q_0,\rho),
$$

defined for $\rho>0$ by replacing $a$ by $q_0$, $a'$ by $\rho$ and the complex unit $i$ by $\hat{\mathbf{q}}$, which is legitimate because $\hat{\mathbf{q}}^2 = -1$. When $f_0$ has real Taylor coefficients, $v(q_0,0) = 0$, the extension extends continuously to $\rho = 0$ with value $f_0(q_0)$, and $\tilde f_0(\tilde q) = \sum_{n\geq0}a_n\tilde q^n$ on $B(0,R)$.

### Fueter's Theorem

**Theorem (Fueter's construction).** Let $f_0$ be holomorphic on $D(0,R)$ with axial extension $\tilde f_0$. Then

$$
F(\tilde q) = \Delta_4\tilde f_0(\tilde q) = \frac{2\,\partial_\rho u(q_0,\rho)}{\rho}+\hat{\mathbf{q}}\left(\frac{2\,\partial_\rho v(q_0,\rho)}{\rho}-\frac{2\,v(q_0,\rho)}{\rho^2}\right)
$$

is defined and real-analytic on $B(0,R)$, by continuity at $\rho = 0$, and is both left- and right-Fueter-regular there.

*Proof.* For $g = A(q_0,\rho)+\hat{\mathbf{q}}B(q_0,\rho)$ with central coefficients $A,B$, one has $\partial_{q_k}A = (\partial_\rho A)\hat q_k$, $\sum_ke_k\hat q_k = \hat{\mathbf{q}}$ and $\sum_{j,k}(\partial_{q_k}\hat q_j)e_ke_j = (-3-\hat{\mathbf{q}}^2)/\rho = -2/\rho$, because $\hat{\mathbf{q}}^2 = -1$. Hence $Dg = gD = (\partial_0A-\partial_\rho B-2B/\rho)+\hat{\mathbf{q}}(\partial_0B+\partial_\rho A)$, so $g$ is left-regular if and only if it is right-regular, and this holds exactly when $\partial_0A = \partial_\rho B+2B/\rho$ and $\partial_0B = -\partial_\rho A$. Applying the radial form of the three-dimensional Laplacian and the identity $\Delta_{\mathbb{R}^3}(B\hat{\mathbf{q}}) = \hat{\mathbf{q}}(\Delta_{\mathbb{R}^3}B-2B/\rho^2)$ to the harmonic pair $(u,v)$ gives $\Delta_4\tilde f_0(\tilde q) = P+\hat{\mathbf{q}}Q$ with $P = 2u_\rho/\rho$, $Q = 2(\rho v_\rho-v)/\rho^2$, and the Cauchy–Riemann equations give $Q_\rho+2Q/\rho = \partial_0P$, $-\partial_0Q = P_\rho$; thus $P,Q$ satisfy the regularity system and extend continuously to $\rho = 0$.

### The Kernel and Injectivity

**Proposition.** The Fueter map $\tau(f_0) = \Delta_4\tilde f_0$ vanishes if and only if $f_0$ is affine, $f_0(A) = CA+D$.

*Proof.* $\tau(f_0) = 0$ forces $u_\rho = 0$ and $\rho v_\rho = v$, so $u = u(q_0)$ and $v = c(q_0)\rho$; then $c' = 0$ and $u = cq_0+d$ with $c,d\in\mathbb{R}$, and complex linearity gives all affine functions. Conversely, $\Delta_4$ annihilates the constants and the linear monomials.

**Corollary.** The Fueter map is injective exactly on the holomorphic functions whose Taylor coefficients vanish to order two, $a_0 = a_1 = 0$, its kernel being the affine functions.

## The Axial and Slice Approach

### Imaginary Units and Slices

**Definition.** An **imaginary unit** is an element $I$ with $I^2 = -1$. The **slice** through $I$ is $\mathbb{C}_I = \mathbb{R}+I\mathbb{R}\cong\mathbb{C}$.

**Theorem.** In $\mathbb{H}$ the imaginary units form the two-sphere

$$
S^2 = \{I\in\operatorname{Im}\mathbb{H} : N(I) = 1\},
$$

and every non-real quaternion has a unique representation $\tilde q = q_0+I\rho$ with $I\in S^2$ and $\rho>0$. Two slices meet only in $\mathbb{R}$ unless $I = \pm J$, in which case they coincide.

*Proof.* The roots of $-1$ are the pure unit quaternions, which form the unit sphere of the three-dimensional space $\operatorname{Im}\mathbb{H}$, by *Quaternion Roots of Minus One*; the direction $\hat{\mathbf{q}}$ is pure and unit and $\hat{\mathbf{q}}^2 = -1$, giving the representation, and the uniqueness is the uniqueness of the polar form of the vector part. Two slices $\mathbb{C}_I,\mathbb{C}_J$ intersect in the real span of $I,J$, which is larger than $\mathbb{R}$ exactly when $I = \pm J$.

### Axially Symmetric Functions and the Harmonic Coefficients

**Definition.** A function $F$ on $\mathbb{H}$ is **axially symmetric** if it depends on the direction $\hat{\mathbf{q}}$ only through $\hat{\mathbf{q}}$ itself, that is, if it has the **axial representation**

$$
F(\tilde q) = A(q_0,\rho)+\hat{\mathbf{q}}B(q_0,\rho),
$$

with $A,B$ the **axial coefficients**, functions of the two variables $q_0,\rho$.

**Proposition.** For an axially symmetric $F$ the left- and right-regularity conditions coincide, and they reduce to

$$
\partial_0A = \partial_\rho B+\frac{2B}{\rho}, \qquad \partial_0B = -\partial_\rho A .
$$

Eliminating $B$ gives $\Delta_4A = 0$, so the scalar axial coefficient is harmonic, while the vector coefficient satisfies $\Delta_4B = 2B/\rho^2$.

*Proof.* The first display is the computation in the proof of Fueter's theorem, valid for any central-coefficient axial function and the same on the left and on the right; applying the radial Laplacian and eliminating gives $\Delta_4A = 0$ from the two equations, and substituting back gives $\Delta_4B = 2B/\rho^2$.

**Theorem.** The Fueter construction realizes every axially symmetric regular function with central axial coefficients: such an $F$ arises as $\Delta_4\tilde f_0$ for a holomorphic $f_0$, uniquely modulo the affine kernel.

*Proof.* The axial coefficients $P = 2u_\rho/\rho$, $Q = 2(\rho v_\rho-v)/\rho^2$ are produced from the harmonic conjugate pair $(u,v)$ by Fueter's theorem, and conversely the regularity system solved for $A,B$ recovers a holomorphic $f_0$ up to the affine functions, by the injectivity of the Fueter map.

### The Fueter–Sce Theorem and Its Hypotheses

**Theorem (Fueter–Sce).** Let $n\geq1$ be odd, let $\mathrm{Cl}_{0,n}$ have generators $e_1,\dots,e_n$, and let $f_0$ be holomorphic on a disc, with axial extension $\tilde f_0$ to $\mathbb{R}^{n+1}$. Then $\tilde F = \Delta^{(n-1)/2}\tilde f_0$ is monogenic, annihilated on the left and on the right by the operator $\partial_{q_0}+\sum_{j=1}^{n}e_j\partial_{q_j}$, on the ball where the extension is defined. For $n = 3$ the exponent is one, recovering Fueter's construction.

*Proof.* The power $(n-1)/2$ is a non-negative integer because $n$ is odd, so the operator is ordinary iteration of the Laplacian; the argument of Fueter's theorem generalizes to each odd $n$, the radial computation with $-3$ replaced by $-n$.

**Remark.** Three hypotheses are needed. The function $f_0$ must be holomorphic on $D(0,R)$, so that $\Delta^{(n-1)/2}(\tilde q^n)$ is a homogeneous polynomial of degree $n-1-(n-1)/2$ with at most polynomial growth in $n$ and the induced series converges on $B(0,R)$; the parity exponent $(n-1)/2$ must be a non-negative integer, so $n$ is odd; and the affine kernel $az+b$ remains, so a one-to-one correspondence requires the Taylor coefficients to vanish to order two. None of the three can be dropped.

## Power Series Representations

A series with quaternionic coefficients on the right, $F(\tilde q) = \sum_{n\geq0}\tilde q^na_n$, converges absolutely on $|\tilde q| < R$ with $R^{-1} = \limsup_n|a_n|^{1/n}$, because $|\tilde q^n| = |\tilde q|^n$. Its sum is **slice-regular**, or Cullen-regular: holomorphic on each slice. Slice-regular functions form a class distinct from the Fueter-regular ones; for instance $\tilde q\mapsto\tilde q$ is slice-regular but

$$
Dx = \sum_{\mu=0}^{3}e_\mu e_\mu = e_0^2+e_1^2+e_2^2+e_3^2 = e_0-e_0-e_0-e_0 = -2e_0\neq0 .
$$

The Fueter construction is exactly the operation converting slice-regular, or holomorphic, data into Fueter-regular functions.

For real Taylor coefficients, $\tilde f_0(\tilde q) = \sum_{n\geq0}a_n\tilde q^n$ and termwise application of $\Delta_4$ gives the induced series $\tau(f_0) = \sum_{n\geq0}a_n\Delta_4(\tilde q^n)$, beginning at $n = 2$ and converging normally on $B(0,R)$, since $\Delta_4(\tilde q^n)$ has degree $n-2$ and at most polynomial growth; termwise differentiation is therefore justified. In general, with $\mathcal{P}_k$ the homogeneous quaternion-valued polynomials of degree $k$ and $\mathcal{M}_k = \{P\in\mathcal{P}_k : DP = 0\}$ the **monogenic homogeneous polynomials**, the Fischer decomposition

$$
\mathcal{P}_k = \bigoplus_{j=0}^{k}\tilde q^j\mathcal{M}_{k-j}
$$

gives every Fueter-regular function on $B(0,R)$ a normally convergent expansion $F = \sum_{k\geq0}F_k$ with $F_k\in\mathcal{M}_k$, the four-variable analogue of the Taylor series of one complex variable.

## Relation to the Biquaternion Theory and Clifford Analysis

The biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ carries Fueter theory on its quaternion subspace $\mathbb{H}_{\mathbb{B}}$, and when the values are taken in $\mathbb{H}$ rather than in $\mathbb{B}$ that theory is exactly the theory of this article: same operator, same regularity, same Fueter construction. The quaternion case is therefore the real-coefficient case of the biquaternion theory, and it is the case in which no obstruction appears.

| Feature | Quaternion case $\mathbb{H}$ | Biquaternion case $\mathbb{B}$ |
|---|---|---|
| Norm | definite | indefinite |
| Imaginary units | the sphere $S^2$ of pure unit quaternions | the larger family of *Biquaternion Square Roots of Minus One, Zero and Plus One*, not a sphere |
| Slice structure | a single sphere of slices | one slice selected at a time from a non-spherical root set |
| Singularity of the Cauchy theory | the origin only | the null quadric, real dimension $6$ |
| Ellipticity of the Fueter operator | everywhere for real covectors | fails over $\mathbb{C}$ |
| Fueter construction | Fueter's theorem, exponent one | same on $\mathbb{H}_{\mathbb{B}}$; open on the full algebra |

The relation to Clifford analysis is the identification $\mathbb{H}\cong\mathrm{Cl}^0_{0,3}$ of *Clifford Algebras in Finite Dimensions*: Fueter-regular functions are the monogenic functions of the even Clifford algebra in three dimensions, and the biquaternion theory is the monogenic theory of the complexified even Clifford algebra $\mathrm{Cl}^0_{1,3}$. The Fueter–Sce theorem is the general statement of that correspondence for odd $n$, of which the quaternion case $n = 3$ is the first non-trivial instance. Because the quaternion norm is definite, the Clifford analysis here is elliptic throughout, and the only singularity of the Cauchy theory is the origin.

## Summary

The Fueter operator $D = \sum_\mu e_\mu\partial_\mu$ and its conjugate $\bar D = \partial_0-\mathbf{D}$ factor the four-dimensional Laplacian, $D\bar D = \bar DD = \Delta_4$, and on a slice $\mathbb{C}_I$ reduce to the classical operator $\partial_{q_0}+I\partial_\rho$. Fueter-regular functions, the solutions of $DF = 0$, satisfy the quaternionic Cauchy–Riemann system $\partial_0F_0 = \mathrm{div}\,\mathbf{F}$, $\partial_0\mathbf{F} = -\mathrm{grad}\,F_0-\mathrm{rot}\,\mathbf{F}$; left- and right-regularity differ only in the sign of the curl and coincide for axially symmetric functions. The system is elliptic, and every regular function is harmonic, hence real-analytic and subject to the mean value property, the maximum principle, Liouville's theorem and the Cauchy estimates, with no exceptional set. The system also admits a **Debye-type reformulation**, in which each component is expressed through its own radial derivative, the $q_0$-derivative of the radius contracted with the others, and the components of $\mathbf{q}\times\nabla$ of the others; the four relations are the radius contractions of the four component equations, so they hold identically for a regular function, and in one complex variable the same pair of identities is equivalent to the Cauchy–Riemann relations.

The Fueter construction sends a holomorphic $f_0$ to $F = \Delta_4\tilde f_0 = 2u_\rho/\rho+\hat{\mathbf{q}}(2v_\rho/\rho-2v/\rho^2)$, which is both left- and right-regular; it is injective exactly on holomorphic functions whose Taylor coefficients vanish to order two, with the affine functions as kernel. The imaginary units of $\mathbb{H}$ form the two-sphere $S^2$, so that every non-real quaternion has a unique slice representation $\tilde q = q_0+I\rho$, and the axial representation $F = A(q_0,\rho)+\hat{\mathbf{q}}B(q_0,\rho)$ reduces regularity to $\partial_0A = \partial_\rho B+2B/\rho$, $\partial_0B = -\partial_\rho A$, with $\Delta_4A = 0$ and $\Delta_4B = 2B/\rho^2$. The Fueter–Sce theorem extends the construction to odd $n$ with the power $(n-1)/2$ under the hypotheses of holomorphic convergence, order-two vanishing and odd dimension.

Regular functions have the induced series and the monogenic Taylor expansion of the Fischer decomposition, while slice-regular series form the distinct class the construction converts into regular functions. The quaternion case is the real-coefficient case of the biquaternion Fueter theory; the biquaternion case differs through the indefiniteness of the norm, the non-spherical root set, the null quadric obstruction, and the failure of ellipticity over $\mathbb{C}$. In Clifford terms, $\mathbb{H}\cong\mathrm{Cl}^0_{0,3}$, and this article treats the elliptic classical instance of the Fueter–Sce correspondence.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | The quaternion algebra, a division algebra |
| $\tilde q = q_0+\mathbf{q}$, $\rho = \lvert\mathbf{q}\rvert$, $\hat{\mathbf{q}} = \mathbf{q}/\rho$ | Variable, modulus of the vector part, direction |
| $D = \partial_0+\mathbf{D}$, $\mathbf{D} = \sum_k e_k\partial_k$ | Fueter (Cauchy–Riemann–Fueter) operator, acting on the left |
| $\bar D = \partial_0-\mathbf{D}$ | Conjugate Fueter operator |
| $\Delta_4 = \sum_\mu\partial_\mu^2$ | Four-dimensional Laplacian; $D\bar D = \bar DD = \Delta_4$ |
| $DF = 0$ | Left-regularity; monogenic in Clifford language |
| $FD = 0$ | Right-regularity |
| $\mathrm{div}, \mathrm{grad}, \mathrm{rot}$ | Vector operators in the componentwise system |
| $\partial_0F_0 = \mathrm{div}\,\mathbf{F}$, $\partial_0\mathbf{F} = -\mathrm{grad}\,F_0-\mathrm{rot}\,\mathbf{F}$ | Quaternionic Cauchy–Riemann system |
| $(\mathbf{q}\times\nabla g)_k$ | Components of the radius–gradient cross product in the Debye-type identities |
| $\psi_E$, $\psi_M$ | Debye potentials, the two real scalar generators of source-free Maxwell solutions |
| $I$, $S^2$ | Imaginary unit, $I^2 = -1$; the imaginary units of $\mathbb{H}$ form the two-sphere |
| $\mathbb{C}_I = \mathbb{R}+I\mathbb{R}$ | Slice through $I$, a copy of the complex plane |
| $A, B$ | Axial coefficients, $F = A(q_0,\rho)+\hat{\mathbf{q}}B(q_0,\rho)$ |
| $\tilde f_0$, $\tau(f_0) = \Delta_4\tilde f_0$ | Axial extension of a holomorphic $f_0$ and its Fueter-induced regular function |
| $\mathcal{P}_k$, $\mathcal{M}_k$ | Homogeneous polynomials of degree $k$; monogenic ones; Fischer decomposition |
| $\mathrm{Cl}^0_{0,3}\cong\mathrm{Cl}_{0,2}\cong\mathbb{H}$ | Clifford identifications of the quaternion algebra |
| $\mathbb{B}$, $\mathbb{H}_{\mathbb{B}}$ | Biquaternion algebra and its quaternion subspace, the complexified case |

## Further Reading

- Rudolf Fueter, "Die Funktionentheorie der Differentialgleichungen $\Delta u = 0$ und $\Delta\Delta u = 0$ mit vier reellen Variablen", *Commentarii Mathematici Helvetici* **7** (1934) 307–330, for the construction of regular functions from holomorphic ones.
- F. Brackx, Richard Delanghe and F. Sommen, *Clifford Analysis* (Pitman, 1982), for monogenic functions, the Cauchy–Riemann operator and the Fischer decomposition.
- Richard Delanghe, F. Sommen and V. Souček, *Clifford Algebra and Spinor-Valued Functions* (Kluwer, 1992), for the function theory of the operator and its Taylor expansions.
- Graziano Gentili, Caterina Stoppato and Daniele C. Struppa, *Regular Functions of a Quaternionic Variable* (Springer, 2013), for slice-regular functions and their power series.
- F. Colombo, I. Sabadini and D. C. Struppa, *Noncommutative Functional Calculus* (Birkhäuser, 2011), for the slice approach and the Fueter mapping theorem.
- Klaus Gürlebeck and Wolfgang Sprößig, *Quaternionic and Clifford Calculus for Physicists and Engineers* (Wiley, 1997), for the quaternion Cauchy theory and the mean value property.
- M. Acevedo M., J. López-Bonilla and M. Sánchez-Meraz, "Quaternions, Maxwell equations and Lorentz transformations", *Apeiron* **12** (2005) 371–384, for the Debye-type rewriting of the Cauchy–Riemann relations and its quaternionic extension to the Fueter system.
