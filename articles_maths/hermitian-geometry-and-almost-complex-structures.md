
# __Hermitian Geometry and Almost Complex Structures__

## Introduction

An **almost complex structure** on a smooth manifold is a bundle endomorphism $J$ of the tangent bundle with $J^2 = -\mathrm{id}$; it is the fibrewise datum of a multiplication by $\sqrt{-1}$ on each tangent space, and it exists only in even dimensions. A **Hermitian metric** is a Riemannian metric for which $J$ is an isometry, and the pair is the geometric setting in which a complex structure meets a distance. The subject of this article is that meeting: the almost complex structures, the condition under which they come from honest holomorphic coordinates, the Hermitian metrics and their fundamental $2$-form, and the canonical connection — the Chern connection — that a Hermitian metric carries.

The organising question of the first half is **integrability**. An almost complex structure is a purely pointwise object; a complex structure is a coherent family of holomorphic charts. The obstruction to the second being the first is the **Nijenhuis tensor** $N_J$, and the Newlander–Nijenhuis theorem says that $N_J = 0$ is exactly the integrability condition. The tensor is tensorial — antisymmetric and $C^\infty(M)$-linear — so it can be computed pointwise, and it can genuinely fail to vanish, the round six-sphere being the classical example.

The second half organises the metric side. A Hermitian metric is a Riemannian metric invariant under $J$, its **fundamental form** $\Omega(X,Y) = g(JX,Y)$ is a real $2$-form of type $(1,1)$, and the failure of $\Omega$ to be closed measures the failure of the Hermitian structure to be Kähler. On any Hermitian manifold the Levi-Civita connection of $g$ does not preserve $J$ in general; there is nevertheless a canonical connection, the Chern connection, characterised by $\nabla g = 0$, $\nabla J = 0$ and the vanishing of the $(0,2)$-part of its torsion. The Kähler manifolds are exactly those for which this connection is torsion-free, hence equals the Levi-Civita connection, and the detailed theory of that case is the companion article *Kähler Geometry*, being written in parallel.

**The boundaries of the article.** Riemannian metrics, the Levi-Civita connection, the curvature tensor, geodesics and the Riemannian volume are the subject of the companion article *Riemannian Geometry*, being written in parallel, and are used here without derivation. Differential forms, the exterior derivative, the type decomposition and the integral of a top form are those of *Differential Forms and Stokes' Theorem*; manifolds, charts, bundles and the tangent bundle those of *Smooth Manifolds and Differential Geometry*, *Differential Topology* and *Fibre Bundles, Connections and Curvature*, all being written in parallel. The symplectic side — a symplectic form, its compatible almost complex structures and the contractibility of that space — is the subject of *Symplectic Geometry*, and the relation between the two structures is used here. Characteristic classes, including the Chern classes of a complex vector bundle and their relation to the curvature of a connection, are the subject of *Characteristic Classes*, earlier in this Part. The Dolbeault cohomology is defined here as the cohomology of a complex of forms, an algebraic construction; the finiteness theorem, the Hodge decomposition and the harmonic representatives require the analysis of Part III, where the measure and the limit are available, and are deferred there in that explicit form. Lie groups and their homogeneous spaces are those of *Lie Groups* and its companions. The base field is $\mathbb{R}$ and no physics is invoked.

## Almost Complex Structures

**Definition.** Let $M$ be a smooth manifold. An **almost complex structure** on $M$ is a bundle endomorphism $J : TM \to TM$ with

$$
J^2 = -\mathrm{id}_{TM}.
$$

A pair $(M, J)$ is an **almost complex manifold**. A map $F : (M,J) \to (N,J')$ is **almost complex** or **pseudoholomorphic** if $dF\circ J = J'\circ dF$.

**Proposition.** An almost complex structure exists on $M$ only if $M$ is even dimensional, and then it reduces the structure group of the tangent bundle from $GL(2n,\mathbb{R})$ to $GL(n,\mathbb{C})$.

**Proof.** At a point $x$ the endomorphism $J_x$ is a real linear map with $J_x^2 = -\mathrm{id}$, so its minimal polynomial divides $t^2+1$ and its eigenvalues lie among $\pm i$; the nonreal eigenvalues of a real matrix occur in conjugate pairs, so the characteristic polynomial is $(t^2+1)^n$ and the dimension is $2n$, with $\det J_x = 1$. A complex basis of $T_xM$, that is, a real basis $e_1,\ldots,e_n, Je_1,\ldots, Je_n$, gives the required local reduction, and the transition functions preserve the structure. $\square$

**Definition.** The **complexified tangent bundle** is $T_{\mathbb{C}}M = TM\otimes_{\mathbb{R}}\mathbb{C}$, and $J$ extends to it $\mathbb{C}$-linearly. Its eigenvalues are $\pm i$, and the corresponding eigenbundles are

$$
T^{1,0}M = \{v \in T_{\mathbb{C}}M : Jv = iv\}, \qquad T^{0,1}M = \{v \in T_{\mathbb{C}}M : Jv = -iv\}.
$$

They satisfy $T^{0,1}M = \overline{T^{1,0}M}$ and

$$
T_{\mathbb{C}}M = T^{1,0}M \oplus T^{0,1}M, \qquad T^{1,0}M \cong TM \ \text{as real bundles.}
$$

The isomorphism is $X \mapsto X - iJX \in T^{1,0}M$ with inverse $v\mapsto \mathrm{Re}\,v$, and the projection onto $T^{1,0}$ is $\frac12(\mathrm{id} - iJ)$.

**Proof.** For $X \in TM$, $J(X - iJX) = JX - iJ^2X = JX + iX = i(X - iJX)$ and $J(X+iJX) = JX + iJ^2X = JX - iX = -i(X+iJX)$; since $X = \frac12[(X-iJX) + (X+iJX)]$, the two eigenbundles span $T_{\mathbb{C}}M$ and, having distinct eigenvalues, are independent. Conjugation exchanges them because $J$ is real. $\square$

**Example.** On $\mathbb{R}^{2n}$ with coordinates $x_1,\ldots,x_n, y_1,\ldots,y_n$, put $J\partial_{x_i} = \partial_{y_i}$ and $J\partial_{y_i} = -\partial_{x_i}$. Then $J^2 = -\mathrm{id}$, and with $z_i = x_i + iy_i$ the fields $\partial_{z_i} = \frac12(\partial_{x_i} - i\partial_{y_i})$ span $T^{1,0}$ and the fields $\partial_{\bar z_i} = \frac12(\partial_{x_i}+i\partial_{y_i})$ span $T^{0,1}$. This is the **standard complex structure** on $\mathbb{C}^n$.

**Example.** Every complex manifold — one with an atlas whose transition functions are holomorphic — carries a canonical almost complex structure: the multiplication by $i$ on the holomorphic tangent bundle. The almost complex structure is thus the pointwise shadow of a complex structure, and the question of when the shadow determines the structure is the subject of the next section.

**Example.** The sphere $S^2$ with its standard orientation carries an almost complex structure, since it is the Riemann sphere. The sphere $S^6$ carries one obtained from the multiplication of the octonions: identifying $\mathbb{R}^7$ with the imaginary octonions and $S^6$ with the units, the map $J_x(v) = x\cdot v$ sends the tangent space $T_xS^6$ to itself, because $\langle x, xv\rangle = \langle \bar x x, v\rangle = \mathrm{Re}(v) = 0$ for $v$ tangent to $S^6$, the tangent vectors at a unit imaginary octonion $x$ being the imaginary octonions orthogonal to $x$; and $J_x^2 = -\mathrm{id}$ there. It is not integrable. By a theorem of Borel and Serre together with the octonionic example, $S^2$ and $S^6$ are the only spheres admitting almost complex structures; whether $S^6$ carries an integrable one is the **six-sphere problem**, and it remains open.

**Remark.** An almost complex structure is an example of a reduction of the structure group of the tangent bundle, in the sense of *Fibre Bundles, Connections and Curvature*; the principal $GL(n,\mathbb{C})$-bundle of complex frames is the object that fails to descend to a holomorphic atlas precisely when the Nijenhuis tensor is nonzero. The almost complex structures that do come from a complex structure are the integrable ones.

## The Nijenhuis Tensor and Integrability

**Definition.** The **Nijenhuis tensor** of an almost complex structure $J$ is the assignment

$$
N_J(X, Y) = [JX, JY] - J[X, JY] - J[JX, Y] - [X, Y], \qquad X, Y \in \mathfrak{X}(M).
$$

**Proposition.** The tensor $N_J$ is well defined, antisymmetric and $C^\infty(M)$-bilinear, so it is a section of $\Lambda^2T^*M\otimes TM$; it satisfies $N_J(X, JX) = 0$ and $N_J(JX, JY) = -N_J(X,Y)$ for all $X,Y$.

**Proof.** Antisymmetry is immediate from the antisymmetry of the Lie bracket. For the $C^\infty(M)$-linearity in the first slot compute directly:
$$
\begin{aligned}
[J(fX), JY] &= f[JX,JY] - (JY)(f)\,JX,\\
J[fX, JY] &= fJ[JX,JY] - (JY)(f)\,JX,\\
J[J(fX), Y] &= fJ[JX,Y] - Y(f)\,J^2X,\\
[fX, Y] &= f[X,Y] - Y(f)\,X .
\end{aligned}
$$
Since $J^2 = -\mathrm{id}$, the correction $-(JY)(f)JX$ from the first line cancels against the correction $+(JY)(f)JX$ from the second, and the correction $-Y(f)J^2X = +Y(f)X$ from the third line cancels against the term $-Y(f)X$ carried by the fourth; the terms carrying $f$ reproduce $fN_J(X,Y)$. Hence $N_J(fX,Y)=fN_J(X,Y)$, and the same computation with the roles of the slots exchanged gives $N_J(X,fY) = fN_J(X,Y)$. Therefore $N_J$ is tensorial. Finally $N_J(X,JX) = [JX, J^2X] - J[X,J^2X] - J[JX,JX] - [X,JX] = -[JX,X] + J[X,X] - 0 - [X,JX] = [X,JX] - [X,JX] = 0$, and substituting $JX$ and $JY$ in the definition gives
$$
N_J(JX,JY) = [J^2X,J^2Y] - J[JX,J^2Y] - J[J^2X,JY] - [JX,JY] = [X,Y] + J[JX,Y] + J[X,JY] - [JX,JY] = -N_J(X,Y). \ \square
$$

**Theorem (Newlander–Nijenhuis).** An almost complex structure $J$ on a smooth manifold $M$ is integrable, that is, $M$ admits an atlas of charts whose transition functions are holomorphic and whose induced almost complex structures are $J$, if and only if $N_J = 0$.

**Proof sketch.** If holomorphic coordinates exist, then in them $J$ is the standard constant structure and $N_J=0$ by a direct computation: for constant $J$ one has $[JX,JY] = J[X,JY] = J[JX,Y] = J^2[X,Y] = -[X,Y]$ and the four terms cancel. Conversely, if $N_J=0$ then the distribution $T^{0,1}$ is closed under the Lie bracket, hence integrable by the Frobenius theorem of *Differential Forms and Stokes' Theorem*, and a full set of complex-valued functions $z^i$ annihilated by $T^{0,1}$ provides local holomorphic coordinates; the Frobenius theorem applied to the real distribution underlying $T^{0,1}$ produces the foliation whose leaves are the required complex coordinate domains. $\square$

**Corollary.** On a manifold of real dimension two, every almost complex structure is integrable. Indeed $N_J$ is antisymmetric and $N_J(X,JX) = 0$, while at each point the pair $\{X, JX\}$ spans the tangent space; so $N_J = 0$ identically. Consequently every oriented surface is a Riemann surface, and a complex curve is the same thing as an oriented conformal surface.

**Example (a non-integrable almost complex structure).** On $\mathbb{R}^4$ with coordinates $x, y, z, t$ define

$$
J\partial_x = \partial_y + z\,\partial_z, \quad J\partial_y = -\partial_x - z\,\partial_t, \quad J\partial_z = \partial_t, \quad J\partial_t = -\partial_z .
$$

The matrix of $J$ in the coordinate frame is
$$
\begin{pmatrix} 0 & -1 & 0 & 0\\ 1 & 0 & 0 & 0\\ z & 0 & 0 & -1\\ 0 & -z & 1 & 0 \end{pmatrix},
$$
and one checks $J^2 = -\mathrm{id}$ for every value of $z$. Computing the Nijenhuis tensor on the coordinate fields gives

$$
N_J(\partial_x, \partial_z) = \partial_t \neq 0,
$$

so $J$ is not integrable: no holomorphic coordinates exist near any point. The example shows that the integrability condition is a genuine restriction and that the tensor $N_J$ is the obstruction. The structure is a member of the family obtained from the displayed matrix by replacing the entry $z$ with a function $a$ of the coordinates, that is, by $J\partial_x = \partial_y + a\,\partial_z$, $J\partial_y = -\partial_x - a\,\partial_t$, $J\partial_z = \partial_t$, $J\partial_t = -\partial_z$. One computes

$$
N_J(\partial_x,\partial_z) = -a_t\,\partial_z + a_z\,\partial_t, \qquad N_J(\partial_x,\partial_y) = a\,a_t\,\partial_z - a\,a_z\,\partial_t,
$$

$$
N_J(\partial_x,\partial_t) = a_z\,\partial_z + a_t\,\partial_t, \qquad N_J(\partial_y,\partial_z) = a_t\,\partial_t + a_z\,\partial_z, \qquad N_J(\partial_y,\partial_t) = a_t\,\partial_z - a_z\,\partial_t,
$$

and $N_J(\partial_z,\partial_t)=0$. Since $N_J$ is tensorial it suffices to test the coordinate fields, so the tensor vanishes identically exactly when $a_z = a_t = 0$, that is, when $a$ depends only on $x$ and $y$. The choice $a = z$ gives the non-integrable structure above, while a constant $a$ gives the standard structure of $\mathbb{C}^2$ pulled back by the shear $v = z - ay + it$.

**Remark.** The Nijenhuis tensor measures the failure of the integrability of the eigenbundle $T^{0,1}$: the $(0,2)$-component of the Lie bracket of two $(0,1)$-fields is a constant multiple of the tensor, so it vanishes identically exactly when $N_J = 0$, which says that $T^{0,1}$ is a Lie subalgebra of the complexified fields and hence, by Frobenius, tangent to a foliation by complex submanifolds. In the language of the article *Differential Forms and Stokes' Theorem*, the almost complex structure is integrable exactly when the ideal generated by the $(0,1)$-forms in the complexified exterior algebra is a differential ideal. The complex structures of dimension two are therefore automatic, the octonionic structure on $S^6$ is the standard non-integrable example, and the integrable structures are the complex manifolds.

## Complex Manifolds and the Dolbeault Complex

**Definition.** A **complex manifold** of complex dimension $n$ is a smooth manifold of real dimension $2n$ with an atlas of charts to open subsets of $\mathbb{C}^n$ whose transition functions are holomorphic. A **holomorphic function** on a complex manifold is a smooth complex-valued function whose local expression in every chart is holomorphic; the sheaf of holomorphic functions is written $\mathcal{O}_M$.

An integrable almost complex structure and a complex structure are equivalent data: the Newlander–Nijenhuis theorem produces the holomorphic charts from $N_J=0$, and conversely a complex structure induces an almost complex structure with $N_J=0$. We therefore pass between the two languages freely.

**Definition.** Let $(M,J)$ be an almost complex manifold. The complexified exterior algebra decomposes by type:

$$
\Omega^k(M,\mathbb{C}) = \bigoplus_{p+q=k}\Omega^{p,q}(M), \qquad \Omega^{p,q}(M) = \Gamma\bigl(\Lambda^p(T^{1,0})^*\wedge\Lambda^q(T^{0,1})^*\bigr).
$$

The exterior derivative splits by type as $d = \partial + \bar\partial$ with $\partial : \Omega^{p,q}\to\Omega^{p+1,q}$ and $\bar\partial : \Omega^{p,q}\to\Omega^{p,q+1}$ if and only if $J$ is integrable; in that case $\bar\partial^2 = 0$, and the **Dolbeault cohomology** of $M$ is

$$
H^{p,q}_{\bar\partial}(M) = \frac{\ker\bigl(\bar\partial : \Omega^{p,q}\to\Omega^{p,q+1}\bigr)}{\mathrm{im}\bigl(\bar\partial : \Omega^{p,q-1}\to\Omega^{p,q}\bigr)} .
$$

**Proposition.** On a complex manifold, $d = \partial + \bar\partial$, $\partial^2 = \bar\partial^2 = 0$ and $\partial\bar\partial + \bar\partial\partial = 0$. A function is holomorphic exactly when $\bar\partial f = 0$, and the holomorphic $1$-forms are the local sections of $(T^{1,0})^*$ that are $\bar\partial$-closed.

**Proof.** The type decomposition of $d$ follows from the integrability: the $(0,2)$-component of $d$ on functions is measured by $N_J$, and the general statement follows from writing $d$ in holomorphic coordinates. The relations follow from $d^2=0$ and the bidegree. $\square$

**Remark.** The Dolbeault complex is a complex of sections of vector bundles, and its cohomology can be computed by the analysis of the $\bar\partial$-operator: on a compact complex manifold the cohomology spaces are finite dimensional and are represented by harmonic forms. That statement is the Hodge theory of the $\bar\partial$-operator, and it requires the theory of elliptic operators, Sobolev spaces and completions, which belong to Part III, where the measure and the limit are available. What is used here is only the algebraic complex and the identification of its degree zero with the holomorphic functions. The topological interpretation of the Dolbeault groups via the de Rham complex and the relation $H^k_{dR}(M,\mathbb{C}) = \bigoplus_{p+q=k}H^{p,q}_{\bar\partial}(M)$ for a compact Kähler manifold is treated in *Kähler Geometry*, being written in parallel.

## Hermitian Metrics and the Fundamental Form

**Definition.** Let $(M,J)$ be an almost complex manifold. A **Hermitian metric** on $(M,J)$ is a Riemannian metric $g$ with

$$
g(JX, JY) = g(X, Y) \qquad \text{for all } X, Y \in \mathfrak{X}(M).
$$

An **almost Hermitian manifold** is a triple $(M, J, g)$ of a manifold, an almost complex structure and a Hermitian metric; when $J$ is integrable the triple is a **Hermitian manifold**. The **fundamental form** or **associated form** of the triple is

$$
\Omega(X, Y) = g(JX, Y).
$$

**Proposition.** Let $(M,J,g)$ be almost Hermitian. Then:

**(a)** $\Omega$ is a real $2$-form, alternating, and of type $(1,1)$; equivalently $\Omega(JX,JY) = \Omega(X,Y)$;

**(b)** the Hermitian metric is recovered from $\Omega$ and $J$ by $g(X,Y) = \Omega(X,JY)$;

**(c)** the **Hermitian form** $h : T^{1,0}M\times T^{1,0}M \to \mathbb{C}$, defined by $h(v,w) = g_{\mathbb{C}}(v,\bar w)$ where $g_{\mathbb{C}}$ is the $\mathbb{C}$-bilinear extension of $g$ to $T_{\mathbb{C}}M$ and $\bar w$ is the complex conjugate, is $\mathbb{C}$-linear in $v$ and conjugate-linear in $w$, satisfies $h(w,v) = \overline{h(v,w)}$, and is positive definite: $h(v,v) > 0$ for $v \neq 0$.

**Proof.** (a) Antisymmetry: $\Omega(Y,X) = g(JY,X) = -g(JY,J^2X) = -g(Y,JX) = -g(JX,Y) = -\Omega(X,Y)$, using symmetry of $g$ and $g(J\,\cdot\,,J\,\cdot\,) = g$. Type: for $v, w \in T^{1,0}$, $\Omega(v,w) = g(Jv,w) = g(iv,w) = i\,g(v,w)$ and antisymmetry gives $\Omega(v,w) = -\Omega(w,v) = -g(Jw,v) = -i\,g(w,v) = -i\,g(v,w)$; hence $g(v,w)=0$ and $\Omega$ has no $(2,0)$-part, and by conjugation no $(0,2)$-part either. (b) $\Omega(X,JY) = g(JX,JY) = g(X,Y)$. (c) Sesquilinearity and conjugate symmetry are immediate from the $\mathbb{C}$-bilinearity and symmetry of $g_{\mathbb{C}}$ together with $\overline{\bar w}=w$. For positivity, write $v = X - iJX$ with $X$ real; then $\bar v = X + iJX$ and

$$
h(v,v) = g_{\mathbb{C}}(X-iJX, X+iJX) = g(X,X) + i\,g(X,JX) - i\,g(JX,X) + g(JX,JX) = 2\,g(X,X) > 0
$$

for $X \neq 0$: the two middle terms cancel, since $g(X,JX) = g(JX,X)$ by symmetry of $g$, and $g(JX,JX) = g(X,X)$ supplies the second copy of $g(X,X)$. $\square$

**Proposition.** Every almost complex manifold admits a Hermitian metric: if $g_0$ is any Riemannian metric, then

$$
g(X, Y) = \tfrac12\bigl(g_0(X,Y) + g_0(JX, JY)\bigr)
$$

is Hermitian, and the assignment is a projection onto the Hermitian metrics among all metrics.

**Proof.** Compute $g(JX,JY) = \frac12(g_0(JX,JY) + g_0(J^2X, J^2Y)) = \frac12(g_0(JX,JY)+g_0(X,Y)) = g(X,Y)$, so $g$ is invariant; it is symmetric because $g_0$ is, and positive definite because it is half the sum of two positive definite forms. $\square$

**Remark.** A Hermitian metric is exactly a Riemannian metric for which the structure group of the frame bundle reduces further, from $GL(n,\mathbb{C})$ to the unitary group $U(n)$; the reduction is that of *Fibre Bundles, Connections and Curvature*, and the associated form $\Omega$ is the $(1,1)$-form whose nondegeneracy and closedness govern the Kähler condition. The metric $g$ and the form $\Omega$ determine one another given $J$; the notation $g(JX,Y)$ for the fundamental form is the one fixed for this category, and it is the form that is written $\Omega$ throughout, the Kähler form of the companion article *Kähler Geometry*, being written in parallel.

**Proposition (Wirtinger).** Let $(M,J,g)$ be almost Hermitian with fundamental form $\Omega$ and let $V \subseteq T_xM$ be an oriented real $2k$-plane with oriented orthonormal basis $u_1, \ldots, u_{2k}$. Then

$$
\bigl| \Omega^{\wedge k}(u_1, \ldots, u_{2k}) \bigr| \leq k!,
$$

with equality if and only if $V$ is a complex subspace, that is $JV = V$.

**Proof.** For $k=1$ and an orthonormal basis $u, v$ of $V$, $\Omega(u,v) = g(Ju,v)$ and Cauchy–Schwarz gives $|g(Ju,v)| \leq \|Ju\|\,\|v\| = 1$, with equality exactly when $v = Ju$, that is, when $V$ is complex. For general $k$, choose an orthonormal basis adapted to the complex part of $V$: the bilinear form $\Omega^{\wedge k}$ decomposes as a sum of $k$-fold products of the $k=1$ case, and the Cauchy–Schwarz inequality applies to each factor. $\square$

**Remark.** The Wirtinger inequality is the pointwise statement that complex submanifolds about which it is an equality are **calibrated** by $\Omega^k/k!$: their volume equals the integral of the form. This is the geometric content of the Kähler form and the reason complex submanifolds of a Kähler manifold are volume-minimising in their homology class; the details belong to *Kähler Geometry*, being written in parallel, and to the calibration theory cited there.

## The Chern Connection

**Theorem (Chern).** Let $(M,J,g)$ be a Hermitian manifold. There is a unique connection $\nabla$ on $TM$, extended $\mathbb{C}$-linearly to $T_{\mathbb{C}}M$, such that

**(a)** $\nabla g = 0$;

**(b)** $\nabla J = 0$;

**(c)** the torsion $T(X,Y) = \nabla_XY - \nabla_YX - [X,Y]$ has vanishing $(0,2)$-component, equivalently $T(X,Y) = T(JX,JY)$ for all $X, Y$.

This is the **Chern connection** of the Hermitian structure.

**Proof sketch.** Conditions (a) and (b) are linear in $\nabla$ and define an affine space of connections; the difference $\nabla - \nabla^{LC}$ of two connections with $\nabla J = 0$ is a tensor with values in the $J$-skew endomorphisms. Imposing (c) fixes the free part. Concretely, in a local complex frame $e_1,\ldots,e_n$ of $T^{1,0}$ with $g_{i\bar j} = g(e_i, \bar e_j)$, the conditions force $\nabla e_j = \theta^k_{\;j}\otimes e_k$ with

$$
\theta^k_{\;j} = \sum_l g^{k\bar l}\,\partial g_{j\bar l}, \qquad \text{and} \qquad \bar\partial \text{-part of } \theta^k_{\;j} = 0,
$$

that is, the connection $1$-form is $\theta = h^{-1}\partial h$ in a holomorphic frame. Uniqueness is the uniqueness of the solution of the resulting linear system. $\square$

**Proposition.** The Chern connection is the unique connection on the holomorphic tangent bundle $\nabla : \Gamma(T^{1,0})\to\Omega^1\otimes\Gamma(T^{1,0})$ that is **compatible with the Hermitian metric** in the sense $dh(u,v) = h(\nabla u, v) + h(u,\nabla v)$ and whose $(0,1)$-part is the Dolbeault operator $\bar\partial$; its curvature has **type $(1,1)$**, that is, the curvature $2$-form takes values in the $(1,1)$-forms. In a holomorphic frame the connection matrix is $\theta = h^{-1}\partial h$ and the curvature matrix is

$$
\Theta = \bar\partial\theta = \bar\partial(h^{-1}\partial h) = -\,h^{-1}\,\bar\partial h\, h^{-1}\wedge \partial h + h^{-1}\,\bar\partial\partial h,
$$

which is a matrix of $(1,1)$-forms.

**Proof.** In a holomorphic frame the entries of $h$ are smooth functions satisfying $h_{j\bar l} = \overline{h_{l\bar j}}$; the metric-compatibility condition $dh = {}^t\bar\theta\, h + h\,\theta$ forces the antiholomorphic part of $\theta$ to vanish, and the $(1,0)$-part is $h^{-1}\partial h$. The curvature is $\Theta = d\theta + \theta\wedge\theta$ for the convention $\nabla = d + \theta$, and since $\partial(h^{-1}) = -h^{-1}\partial h\,h^{-1}$ one has $\partial\theta = -\,h^{-1}\partial h\,h^{-1}\wedge\partial h = -\theta\wedge\theta$, so the $(2,0)$-terms cancel and $\Theta = \bar\partial\theta$. $\square$

**Remark.** The Chern classes of a Hermitian holomorphic vector bundle are the Chern–Weil classes of $\frac{i}{2\pi}\Theta$, and they are independent of the metric; that construction and the splitting principle belong to *Characteristic Classes*, earlier in this Part. In the Kähler case the Chern connection coincides with the Levi-Civita connection of $g$: the Levi-Civita connection preserves $J$ exactly when $\Omega$ is closed, and then it satisfies (a), (b) and (c) and is unique. The condition $\nabla J = 0$ for the Levi-Civita connection is therefore equivalent to the Kähler condition $d\Omega = 0$, and this is the bridge to *Kähler Geometry*.

**Remark (the almost Hermitian classes).** For an almost Hermitian manifold whose almost complex structure need not be integrable, the Levi-Civita connection generally fails to preserve $J$, and the tensor $\nabla J$ together with $d\Omega$ defines the **Gray–Hervella classes** of almost Hermitian structures. They are the four $U(n)$-modules $W_1, W_2, W_3, W_4$ in which the covariant derivative of $\Omega$ can lie, and the notable classes are: **nearly Kähler** ($\nabla J$ totally antisymmetric, only $W_1$), **almost Kähler** ($d\Omega = 0$, only $W_2$), **Hermitian** ($J$ integrable, only $W_3\oplus W_4$), and **Kähler** (all four zero). The classes organise the intermediate geometries between the almost complex and the Kähler settings and are the source of the nearly Kähler six-sphere, whose structure is the round metric with the octonionic $J$ and which is not Kähler.

## Examples

**Example (complex Euclidean space).** On $\mathbb{C}^n$ with the standard $J$ and the Euclidean metric $g$, the fundamental form is $\Omega = \sum_i dx_i\wedge dy_i$: indeed $\Omega(\partial_{x_i},\partial_{y_i}) = g(J\partial_{x_i},\partial_{y_i}) = g(\partial_{y_i},\partial_{y_i}) = 1$, and $\Omega$ is alternating. Since the coefficients are constant, $d\Omega=0$ and the structure is Kähler. This is the model Hermitian structure, and its Chern connection is the flat connection.

**Example (complex tori).** A quotient $M = \mathbb{C}^n/\Lambda$ by a lattice is a complex manifold with the induced flat Hermitian structure; the fundamental form and the Chern connection descend, and $d\Omega=0$, so a complex torus with the flat metric is Kähler. A torus that is not algebraic nevertheless carries this Hermitian structure, and the Hermitian geometry of a general compact complex manifold is not accessible from the algebraic theory alone.

**Example (Hopf manifolds).** Let $\lambda \in \mathbb{C}$ with $|\lambda| > 1$ and let $\Gamma$ be the infinite cyclic group generated by $z \mapsto \lambda z$ acting on $\mathbb{C}^n\setminus\{0\}$. The quotient is a compact complex manifold, the **Hopf manifold**; for $n = 2$ it is diffeomorphic to $S^1\times S^3$, so its second Betti number vanishes, and since a compact Kähler manifold has a nonzero class in $H^2$ — the class of its Kähler form — the Hopf manifold carries no Kähler metric. It is the standard example of a Hermitian manifold whose Hermitian geometry is not Kähler.

**Example (Riemann surfaces).** On an oriented surface every almost complex structure is integrable, so every Riemann surface is a complex curve; a Hermitian metric is a conformal class together with the orientation, that is, a Riemannian metric, and its fundamental form is the area form. Every Hermitian metric on a Riemann surface is Kähler, because a $2$-form on a surface is automatically closed; so the subject of this article is trivial in complex dimension one, and the study of the resulting space of complex structures on a fixed surface modulo the conformal ambiguity is not made here.

**Example (a non-integrable almost Hermitian structure).** On the almost complex manifold $(\mathbb{R}^4, J)$ of the non-integrable example above, take the Euclidean metric $g$. Then $(M,J,g)$ is almost Hermitian and not Hermitian, because $J$ is not integrable. The fundamental form is $\Omega(X,Y) = g(JX,Y)$, and its exterior derivative need not vanish; the structure lies in one of the Gray–Hervella classes other than $W_3\oplus W_4$, since it is not Hermitian. The example shows that the classes above are not formal: the almost Hermitian condition is strictly weaker than the Hermitian one.

**Example (the six-sphere).** On $S^6$ with the octonionic almost complex structure the round metric is nearly Kähler: the tensor $\nabla J$ is antisymmetric and nonzero, so $\nabla J \neq 0$ and the structure is not Kähler; its fundamental form satisfies $d\Omega \neq 0$. Since $S^6$ has no complex structure as far as is known, this is the most important example of a nearly Kähler structure that is not Hermitian.

**Example (homogeneous Hermitian manifolds).** If $G$ is a Lie group and $H$ a closed subgroup with a $G$-invariant almost complex structure on $G/H$ and a $G$-invariant metric, the reduction to a Hermitian structure is a question about the isotropy representation and the Lie algebra of $\mathfrak{g}$; a flag manifold $G/T$ of a compact Lie group carries an invariant complex structure, and every invariant metric is Hermitian for it. The Lie-theoretic input is that of *Lie Groups* and its companions; the classical groups supply the projective spaces, the Grassmannians and the quadrics.

## Summary

An almost complex structure is a bundle endomorphism $J$ with $J^2=-\mathrm{id}$; it forces the dimension to be even, complexifies the tangent bundle into the eigenbundles $T^{1,0}\oplus T^{0,1}$ of $\pm i$, and reduces the structure group to $GL(n,\mathbb{C})$. It is integrable — equivalent to a complex structure, that is, to holomorphic charts — exactly when the Nijenhuis tensor $N_J(X,Y) = [JX,JY]-J[X,JY]-J[JX,Y]-[X,Y]$ vanishes; on a surface this is automatic, and the octonionic structure on $S^6$ is the standard counterexample.

On a complex manifold the complexified forms split into types with $d=\partial+\bar\partial$, $\bar\partial^2=0$, and the Dolbeault cohomology $H^{p,q}_{\bar\partial}$ is defined; its finiteness and Hodge theory are deferred to Part III, where the analysis is available. A Hermitian metric is a metric with $g(JX,JY)=g(X,Y)$, equivalently a metric whose structure group reduces to $U(n)$; its fundamental form $\Omega(X,Y)=g(JX,Y)$ is a real $(1,1)$-form, and $g$ is recovered from $\Omega$ and $J$. Hermitian metrics exist on every almost complex manifold, and the Wirtinger inequality makes $\Omega^k/k!$ a calibration for complex submanifolds.

Every Hermitian manifold carries a unique Chern connection, the one connection with $\nabla g = 0$, $\nabla J = 0$ and torsion of type $(1,1)$; in a holomorphic frame its connection form is $h^{-1}\partial h$ and its curvature is a matrix of $(1,1)$-forms. The Kähler manifolds are exactly those for which the Chern connection is torsion-free and hence the Levi-Civita connection, equivalently $d\Omega=0$; the general almost Hermitian structures are classified by the Gray–Hervella modules $W_1,\ldots,W_4$, with nearly Kähler, almost Kähler, Hermitian and Kähler as the distinguished cases.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M$, $\dim M = n$ | Smooth manifold; $T_xM$, $TM$, $T^*M$ its tangent and cotangent objects |
| $\mathfrak{X}(M)$, $\Omega^k(M)$ | Smooth vector fields and $k$-forms |
| $J$, $J^2 = -\mathrm{id}$ | Almost complex structure |
| $T^{1,0}$, $T^{0,1}$ | Eigenbundles of $J$ on $T_{\mathbb{C}}M = TM\otimes_{\mathbb{R}}\mathbb{C}$ with eigenvalues $i$, $-i$ |
| $N_J(X,Y)$ | Nijenhuis tensor; $N_J=0$ is the integrability condition (Newlander–Nijenhuis) |
| $\partial$, $\bar\partial$ | Type decomposition of $d$ on a complex manifold; $\bar\partial^2=0$ |
| $H^{p,q}_{\bar\partial}(M)$ | Dolbeault cohomology |
| $g$ | Riemannian metric (from *Riemannian Geometry*) |
| Hermitian metric | $g(JX,JY) = g(X,Y)$; structure group reduces to $U(n)$ |
| $\Omega(X,Y) = g(JX,Y)$ | Fundamental form; real $(1,1)$-form; $g(X,Y)=\Omega(X,JY)$ |
| $h(v,w) = g_{\mathbb{C}}(v,\bar w)$ | Hermitian form on $T^{1,0}$; positive definite, with $h(X-iJX, X-iJX) = 2\,g(X,X)$ for real $X$ |
| $\Omega^{\wedge k}/k!$ | Calibration; Wirtinger inequality $\vert\Omega^{\wedge k}(u_1,\ldots,u_{2k})\vert \le k!$ on an oriented orthonormal basis |
| $h_{i\bar j} = g(\partial_{z^i},\partial_{\bar z^j})$, $\Omega = i\sum h_{i\bar j}dz^i\wedge d\bar z^j$ | Local expressions in holomorphic coordinates |
| $\theta = h^{-1}\partial h$ | Chern connection $1$-form in a holomorphic frame |
| $\Theta = \bar\partial\theta$ | Chern curvature, of type $(1,1)$ |
| $W_1,\ldots,W_4$ | Gray–Hervella classes of almost Hermitian structures |

## Further Reading

- Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of Differential Geometry, Volume II* (Interscience, 1969), for almost complex structures, the Nijenhuis tensor, Hermitian metrics, the Chern connection and its curvature.
- Paul Gauduchon, "Hermitian Connections and Dirac Operators", *Bollettino dell'Unione Matematica Italiana* 11B (1997), 257–288, for the canonical Hermitian connections and their torsion.
- Alfred Gray and Luis Hervella, "The Sixteen Classes of Almost Hermitian Manifolds and Their Linear Invariants", *Annali di Matematica Pura ed Applicata* 123 (1980), 35–58, for the classification of almost Hermitian structures.
- Shiing-Shen Chern, "Characteristic Classes of Hermitian Manifolds", *Annals of Mathematics* 47 (1946), 85–121, for the Chern connection and the Chern classes defined by its curvature.
- August Newlander and Louis Nirenberg, "Complex Analytic Coordinates in Almost Complex Manifolds", *Annals of Mathematics* 65 (1957), 391–404, for the integrability theorem.
- Armand Borel and Jean-Pierre Serre, "Groupes de Lie et puissances réduites de Steenrod", *American Journal of Mathematics* 75 (1953), 409–448, for the non-existence of almost complex structures on most spheres.
- Raymond O. Wells, *Differential Analysis on Complex Manifolds* (Springer, 3rd ed. 2008), for the Dolbeault complex and the Hodge theory deferred here.
- S. I. Goldberg, "Integrability of Almost Kähler Manifolds", *Proceedings of the American Mathematical Society* 21 (1969), 96–100, for the relation between the Kähler condition and the vanishing of the covariant derivative of $J$.
