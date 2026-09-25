# __Lie Groups__

## Introduction

A **Lie group** is a group that is also a smooth manifold, with smooth group operations. Lie groups formalize continuous symmetry: the rotations of the plane and of space, the Lorentz group, the unitary group, and the invertible linear maps of a vector space are all Lie groups.

The treatment is introductory and purely mathematical. We assume familiarity with groups from *Groups* and Lie algebras from *Lie Algebras: A General Introduction*, together with the elementary notions of smooth manifolds (charts, smooth maps, tangent spaces, vector fields). Only a little differential geometry is needed, and it is recalled where used.

To a Lie group $G$ one associates its tangent space at the identity, $\mathfrak{g} = T_eG$, equipped with a bracket built from the commutator of left-invariant vector fields. This linear object is the **Lie algebra** of $G$; it records the local structure of $G$ and discards its global topology. A connected, simply connected Lie group is determined up to isomorphism by its Lie algebra. We treat real and complex Lie groups of finite dimension.

---

# Part I: Lie Groups and the Classical Matrix Groups

## 1. Smooth Manifolds (Recalled)

A **smooth manifold** of dimension $n$ is a second-countable Hausdorff space $M$ with a maximal atlas of charts $\phi : U \to \mathbb{R}^n$ whose transition maps are smooth; smooth maps and their derivatives $df_p : T_pM \to T_{f(p)}N$ are defined in charts. The pushforward of a vector field $X$ by a diffeomorphism $F$ is written $F_*X$.

## 2. Definition of a Lie Group

A **Lie group** is a group $G$ that is also a smooth manifold, such that the maps

$$
m : G \times G \to G, \quad m(g,h) = gh, \qquad \iota : G \to G, \quad \iota(g) = g^{-1}
$$

are smooth. Its **dimension** is the dimension of the underlying manifold; the identity is $e$. It is enough to require that $m$ is smooth, for then $\iota$ is smooth as well (inverse function theorem applied to $(g,h) \mapsto (g,gh)$ at $(e,e)$); the sources in Further Reading require both operations, and the definitions agree.

For each $g$, left and right translations $L_g(h) = gh$ and $R_g(h) = hg$ are diffeomorphisms, with inverses $L_{g^{-1}}$ and $R_{g^{-1}}$. Conjugation

$$
\Psi_g = L_g \circ R_{g^{-1}} : h \mapsto ghg^{-1}
$$

is an automorphism of $G$ and a diffeomorphism; since it fixes $e$, its derivative at $e$ is an invertible linear map of $T_eG$, the source of the adjoint representation (§15).

## 3. The Classical Matrix Groups

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$, and write $A^* = \overline{A}^{\,T}$ in the complex case. The classical groups are

$$
GL_n(\mathbb{K}) = \{A \in M_n(\mathbb{K}) : \det A \neq 0\},
$$

$$
SL_n(\mathbb{K}) = \{A \in GL_n(\mathbb{K}) : \det A = 1\},
$$

$$
O(n) = \{A \in GL_n(\mathbb{R}) : A^TA = I\}, \qquad SO(n) = \{A \in O(n) : \det A = 1\},
$$

$$
U(n) = \{A \in GL_n(\mathbb{C}) : A^*A = I\}, \qquad SU(n) = \{A \in U(n) : \det A = 1\}.
$$

Two groups share the name **symplectic**: the compact symplectic (quaternionic unitary) group $Sp(n) = \{A \in GL_n(\mathbb{H}) : A^*A = I\}$, and the real symplectic group $Sp(2n,\mathbb{R}) = \{A \in GL_{2n}(\mathbb{R}) : A^TJA = J\}$ for a fixed invertible antisymmetric $J$. Note $Sp(1) \cong SU(2)$ and $Sp(2,\mathbb{R}) \cong SL_2(\mathbb{R})$.

The real dimensions are:

| Group | Field | Real dimension |
|---|---|---|
| $GL_n(\mathbb{R})$ | $\mathbb{R}$ | $n^2$ |
| $GL_n(\mathbb{C})$ | $\mathbb{C}$ | $2n^2$ |
| $SL_n(\mathbb{R})$ | $\mathbb{R}$ | $n^2 - 1$ |
| $SL_n(\mathbb{C})$ | $\mathbb{C}$ | $2n^2 - 2$ |
| $O(n)$ | $\mathbb{R}$ | $n(n-1)/2$ |
| $SO(n)$ | $\mathbb{R}$ | $n(n-1)/2$ |
| $U(n)$ | $\mathbb{C}$ | $n^2$ |
| $SU(n)$ | $\mathbb{C}$ | $n^2 - 1$ |
| $Sp(n)$ | $\mathbb{H}$ | $n(2n+1)$ |
| $Sp(2n,\mathbb{R})$ | $\mathbb{R}$ | $n(2n+1)$ |

Each is a closed subgroup of a general linear group, itself a Lie group with polynomial multiplication and rational inversion. The defining conditions are level sets of smooth maps with surjective derivative; for instance $A \mapsto A^TA$ has derivative $H \mapsto A^TH + H^TA$, so the regular value theorem makes $O(n)$ an embedded submanifold of dimension $n^2 - n(n+1)/2 = n(n-1)/2$, and the same argument gives the table (Cartan's closed subgroup theorem, §12, is an alternative). The group operations restrict from the ambient group, so each group is a Lie group. Here $O(n)$ is compact with identity component $SO(n)$, of index $2$, while $U(n)$ and $SU(n)$ are compact connected with $U(n)/SU(n) \cong U(1)$.

## 4. Further Examples

The additive group $\mathbb{R}^n$ is an abelian Lie group of dimension $n$, and $\mathbb{C}^n$ is a real Lie group of dimension $2n$. A **torus**

$$
T^n = \mathbb{R}^n/\mathbb{Z}^n = U(1)^n
$$

is a compact connected abelian Lie group of dimension $n$; the circle $S^1 = U(1)$ is the case $n=1$.

The unit sphere $S^3 = \{q \in \mathbb{H} : |q| = 1\}$ is closed under quaternion multiplication and inversion, and

$$
S^3 \cong SU(2) \cong Sp(1).
$$

It is compact, connected, and simply connected, and $S^3/\{\pm1\} \cong SO(3)$ with a two-sheeted covering $S^3 \to SO(3)$. This double cover of the rotation group by the unit quaternions is the group-theoretic reason quaternions describe rotations. Among spheres, only $S^0$, $S^1$, $S^3$ admit a Lie group structure, so $S^7$ does not.

The **Heisenberg group**

$$
H_3(\mathbb{R}) = \left\{ \begin{pmatrix} 1 & a & c \\ 0 & 1 & b \\ 0 & 0 & 1 \end{pmatrix} : a,b,c \in \mathbb{R} \right\}
$$

is a simply connected nilpotent Lie group of dimension $3$, with the Heisenberg Lie algebra. Semidirect products $G \rtimes H$ with a smooth action, such as the Euclidean group $\mathbb{R}^n \rtimes SO(n)$, are Lie groups as well.

---

# Part II: The Lie Algebra of a Lie Group

## 5. Left-Invariant Vector Fields

A **vector field** $X$ on $G$ assigns to each $g$ a tangent vector $X_g \in T_gG$, smoothly in $g$, and is equivalently a derivation of $C^\infty(G)$. It is **left-invariant** if $(L_g)_*X = X$ for all $g$, that is, if

$$
X_{gh} = (dL_g)_h X_h \quad \text{for all } g,h \in G.
$$

Taking $h = e$ gives $X_g = (dL_g)_eX_e$, so a left-invariant field is determined by its value at $e$; conversely $X_g = (dL_g)_eX$ defines a left-invariant field for any $X \in T_eG$. Evaluation at $e$ is a linear isomorphism

$$
\{\text{left-invariant vector fields}\} \xrightarrow{\ \sim\ } T_eG.
$$

## 6. The Lie Bracket

Vector fields carry the **commutator bracket**

$$
[X,Y]f = X(Yf) - Y(Xf), \qquad f \in C^\infty(G),
$$

which is bilinear, antisymmetric, and satisfies the Jacobi identity. It is natural under diffeomorphisms: $F_*[X,Y] = [F_*X, F_*Y]$. Since left translations are diffeomorphisms, $(L_g)_*[X,Y] = [X,Y]$ whenever $X, Y$ are left-invariant, so the left-invariant fields form a Lie subalgebra. Transporting the bracket across the isomorphism of §5 gives a bracket on $T_eG$.

**Definition.** The **Lie algebra of $G$** is $\mathfrak{g} = T_eG$ with this bracket, written $\mathfrak{g} = \operatorname{Lie}(G)$.

In group terms the bracket is the infinitesimal commutator: for $X, Y \in \mathfrak{g}$,

$$
\exp(tX)\exp(sY)\exp(-tX)\exp(-sY) = \exp\!\left(ts[X,Y] + \text{higher order}\right),
$$

so

$$
[X,Y] = \frac{\partial^2}{\partial s\,\partial t}\Big|_{s=t=0} \exp(tX)\exp(sY)\exp(-tX)\exp(-sY).
$$

The left-invariant convention is the standard one and is used throughout this series.

## 7. The Lie Algebra of a Matrix Group

If $G \subseteq GL_n(\mathbb{R})$ is a closed subgroup, its Lie algebra is

$$
\mathfrak{g} = T_IG = \{X \in M_n(\mathbb{R}) : \exp(tX) \in G \text{ for all } t \in \mathbb{R}\},
$$

with bracket the matrix commutator

$$
[X,Y] = XY - YX.
$$

Indeed the left-invariant fields determined by $X, Y$ are $A \mapsto AX$ and $A \mapsto AY$, whose commutator at $I$ is $XY - YX$. The tangent space is the kernel of the derivative of the defining equations: $d(\det)_I = \operatorname{tr}$ gives $\mathfrak{sl}_n = \{\operatorname{tr}H = 0\}$; $A^TA = I$ gives $\mathfrak{so}(n) = \{H^T = -H\}$; and $A^*A = I$ gives $\mathfrak{u}(n) = \{H^* = -H\}$. Similarly $\mathfrak{su}(n) = \{H^* = -H,\ \operatorname{tr}H = 0\}$, and $\mathfrak{sp}(n)$, $\mathfrak{sp}(2n,\mathbb{R})$ satisfy $H^* = -H$ and $H^TJ + JH = 0$ respectively. Each has the real dimension of the corresponding group in §3, and these algebras coincide with those classified in *Lie Algebras: Categorization*; in particular $\mathfrak{so}(3)$ is $\mathbb{R}^3$ with the cross product, and $\mathfrak{gl}_2(\mathbb{C})$ is the biquaternions with the commutator bracket.

For an abelian group all brackets vanish, and different groups can share a Lie algebra: $S^1$ and $\mathbb{R}$ both have Lie algebra $\mathbb{R}$ but are not isomorphic. The Lie algebra records local data only.

---

# Part III: The Exponential Map

## 8. One-Parameter Subgroups and the Exponential Map

A **one-parameter subgroup** of $G$ is a smooth homomorphism $\gamma : \mathbb{R} \to G$, so $\gamma(0) = e$ and $\gamma(s+t) = \gamma(s)\gamma(t)$. Left-invariant vector fields are **complete** (their flows extend by translation), so for each $X \in \mathfrak{g}$ there is a unique one-parameter subgroup $\gamma_X$ with $\gamma_X(0) = e$ and $\gamma_X'(0) = X$. The **exponential map** is

$$
\exp : \mathfrak{g} \to G, \qquad \exp(X) = \gamma_X(1).
$$

## 9. Properties of the Exponential Map

**(a)** $\exp(tX) = \gamma_X(t)$ for all $t$, hence $\exp(0) = e$.

**(b)** $\exp(sX)\exp(tX) = \exp((s+t)X)$ and $\exp(-X) = \exp(X)^{-1}$.

**(c)** The map $\exp$ is smooth with $d\exp_0 = \operatorname{id}_{\mathfrak{g}}$, so by the inverse function theorem some neighborhoods $U$ of $0$ and $V$ of $e$ satisfy $\exp(U) = V$ diffeomorphically; thus every element near $e$ has a unique small logarithm.

**(d)** For a Lie group homomorphism $\varphi : G \to H$,
$$
\varphi(\exp_G X) = \exp_H(d\varphi_e X).
$$

**(e)** For a matrix group, $\exp(X) = \sum_{k \geq 0} X^k/k!$, the matrix exponential.

**(f)** For $g \in G$, $\ g\exp(X)g^{-1} = \exp(\operatorname{Ad}_gX)$, with $\operatorname{Ad}_g$ as in §15.

**(g)** **Baker–Campbell–Hausdorff:** for sufficiently small $X, Y$ there is $Z \in \mathfrak{g}$ with $\exp(X)\exp(Y) = \exp(Z)$ and
$$
Z = X + Y + \frac{1}{2}[X,Y] + \frac{1}{12}[X,[X,Y]] - \frac{1}{12}[Y,[X,Y]] + \cdots,
$$
a convergent series of iterated brackets. Thus the group law near $e$ is determined by the bracket, and $\exp(X)\exp(Y) = \exp(X+Y)$ whenever $[X,Y] = 0$.

**(h)** If $G$ is connected, $\exp(\mathfrak{g})$ generates $G$.

## 10. Limits of the Exponential Map

The map $\exp$ is a local diffeomorphism at $0$, but in general it is neither injective nor surjective.

- **Not injective.** For $G = S^1 = U(1)$ and $\mathfrak{g} = i\mathbb{R}$, one has $\exp(2\pi i) = 1 = \exp(0)$.
- **Not surjective.** For $G = SL_2(\mathbb{R})$, the matrix
$$
A = \begin{pmatrix} -1 & 1 \\ 0 & -1 \end{pmatrix}
$$
lies in $SL_2(\mathbb{R})$ but equals no $\exp(X)$ with $X$ real. A real matrix is the exponential of a real matrix exactly when it is invertible and each Jordan block belonging to a negative real eigenvalue occurs an even number of times; the eigenvalue $-1$ of $A$ has a single Jordan block of size $2$, so $A$ has no real logarithm.
- **Surjective cases.** The map $\exp$ is surjective when $G$ is connected and compact (for example $U(n)$, $SU(n)$, $SO(n)$, $Sp(n)$, $T^n$), when $G = GL_n(\mathbb{C})$ (every invertible complex matrix has a complex logarithm), and when $G$ is connected and nilpotent; in the last case, if $G$ is simply connected then $\exp$ is a diffeomorphism, the standard example being the Heisenberg group $H_3(\mathbb{R})$. If $G$ is connected and abelian, then $\exp : \mathfrak{g} \to G$ is a surjective homomorphism with discrete kernel, so $G \cong \mathfrak{g}/\Gamma$ for a discrete subgroup $\Gamma$, as for $\mathbb{R}/\mathbb{Z} \cong S^1$ and $\mathbb{R}^n/\mathbb{Z}^n \cong T^n$.
- **Exponential coordinates.** Since $\exp$ is a local diffeomorphism at $0$, the pair $(U,\exp^{-1})$ is a chart near $e$, called a system of **exponential coordinates**.

---

# Part IV: Homomorphisms and the Lie Correspondence

## 11. Lie Group Homomorphisms and Their Differentials

A **Lie group homomorphism** is a map $\varphi : G \to H$ that is both a group homomorphism and smooth; it is an **isomorphism** if it is bijective with smooth inverse. Every continuous group homomorphism between Lie groups is automatically smooth.

Its derivative at the identity,

$$
d\varphi_e : \mathfrak{g} \to \mathfrak{h},
$$

is a **Lie algebra homomorphism**:

$$
d\varphi_e([X,Y]) = [d\varphi_eX, d\varphi_eY].
$$

The assignment $G \mapsto \mathfrak{g}$ is functorial: $d(\psi \circ \varphi)_e = d\psi_e \circ d\varphi_e$ and $d(\operatorname{id}_G)_e = \operatorname{id}_{\mathfrak{g}}$. For example, $\det$ differentiates to $\operatorname{tr}$, and the covering $SU(2) \to SO(3)$ has differential an isomorphism $\mathfrak{su}(2) \to \mathfrak{so}(3)$.

**Integration theorem.** If $G$ is simply connected and $\phi : \mathfrak{g} \to \mathfrak{h}$ is a Lie algebra homomorphism, then there is a unique Lie group homomorphism $\varphi : G \to H$ with $d\varphi_e = \phi$. (This is sometimes called Lie's second theorem; the numbering of Lie's theorems varies among sources.)

For a homomorphism $\varphi : G \to H$: $\operatorname{Lie}(\ker\varphi) = \ker d\varphi_e$; the image is an immersed Lie subgroup with $\operatorname{Lie}(\varphi(G)) = \operatorname{im}d\varphi_e$; if $G, H$ are connected of the same dimension and $d\varphi_e$ is an isomorphism, then $\varphi$ is a covering map, and an isomorphism if $G$ is simply connected; if $\varphi$ is surjective with $H$ connected, then $G/\ker\varphi \cong H$.

## 12. Lie Subgroups and Lie Subalgebras

A **Lie subalgebra** of $\mathfrak{g}$ is a subspace $\mathfrak{h}$ with $[\mathfrak{h},\mathfrak{h}] \subseteq \mathfrak{h}$. An **embedded Lie subgroup** of $G$ is a subgroup that is an embedded submanifold; the group operations then restrict to smooth maps, and its Lie algebra is $\mathfrak{h} = T_eH \subseteq T_eG$. An **immersed Lie subgroup** (analytic subgroup) is a subgroup with a smooth structure making the inclusion an injective immersion; it need not be embedded.

**Cartan's closed subgroup theorem.** Every closed subgroup of a Lie group is an embedded Lie subgroup. In particular the classical matrix groups are Lie groups, being closed in $GL_n(\mathbb{K})$.

**Lie correspondence.** Let $G$ have Lie algebra $\mathfrak{g}$. Every Lie subalgebra $\mathfrak{h} \subseteq \mathfrak{g}$ is the Lie algebra of a unique connected immersed Lie subgroup $H \subseteq G$, and conversely the Lie algebra of such an $H$ is a subalgebra; these assignments are inverse, giving a bijection

$$
\{\text{Lie subalgebras of } \mathfrak{g}\} \longleftrightarrow \{\text{connected immersed Lie subgroups of } G\}.
$$

Under it $\dim H = \dim\mathfrak{h}$, and inclusions correspond to inclusions. For subgroups, being embedded is equivalent to being closed, so an immersed subgroup is embedded exactly when it is closed.

**Example.** In the torus $T^2 = \mathbb{R}^2/\mathbb{Z}^2$, the subgroup $H = \{(e^{2\pi it}, e^{2\pi i\alpha t}) : t \in \mathbb{R}\}$ with $\alpha$ irrational is a connected immersed subgroup of dimension $1$, with Lie algebra the line $\mathbb{R}\cdot(1,\alpha)$. It is dense, hence neither closed nor embedded, and its closure is all of $T^2$; thus a one-dimensional subalgebra can generate a dense subgroup.

## 13. The Lie Correspondence for Simply Connected Groups

**Lie's third theorem.** Every finite-dimensional real Lie algebra $\mathfrak{g}$ is the Lie algebra of some simply connected Lie group $G$.

**Equivalence theorem.** The assignment $G \mapsto \operatorname{Lie}(G)$ is an equivalence of categories between simply connected Lie groups and finite-dimensional real Lie algebras: essentially surjective by Lie's third theorem, full by the integration theorem, and faithful because a homomorphism is determined by its differential on a connected domain. Hence a connected simply connected Lie group is determined up to isomorphism by its Lie algebra.

**Universal covering group.** Every connected Lie group $G$ has a simply connected **universal covering group** $\tilde{G}$ with a covering homomorphism $\pi : \tilde{G} \to G$ and $\operatorname{Lie}(\tilde{G}) \cong \mathfrak{g}$. The kernel $\pi_1(G)$ is a discrete central subgroup, and $G \cong \tilde{G}/\pi_1(G)$. Examples: $\mathbb{R} \to S^1$ with $\pi_1(S^1) = \mathbb{Z}$; $SU(2) \to SO(3)$ with $\pi_1(SO(3)) = \mathbb{Z}/2$; and $\operatorname{Spin}(n) \to SO(n)$ for $n \geq 3$, which is simply connected.

## 14. Connected, Simply Connected, and Compact Examples

| Group | Connected | Simply connected | Compact |
|---|---|---|---|
| $\mathbb{R}^n$ | yes | yes | no |
| $T^n$, $n \geq 1$ | yes | no | yes |
| $S^1 = U(1)$ | yes | no | yes |
| $S^3 = SU(2) = Sp(1)$ | yes | yes | yes |
| $GL_n(\mathbb{R})$, $n \geq 1$ | no | no | no |
| $GL_n(\mathbb{C})$, $n \geq 1$ | yes | no | no |
| $SL_n(\mathbb{R})$, $n \geq 2$ | yes | no | no |
| $SL_n(\mathbb{C})$, $n \geq 2$ | yes | yes | no |
| $O(n)$ | no | no | yes |
| $SO(n)$, $n \geq 2$ | yes | no | yes |
| $U(n)$ | yes | no | yes |
| $SU(n)$ | yes | yes | yes |
| $Sp(n)$ | yes | yes | yes |

A compact connected Lie group has finite fundamental group exactly when its universal cover is compact; the circle shows that compactness alone does not force this, since $\pi_1(S^1) = \mathbb{Z}$. Also $SO(3) \cong \mathbb{RP}^3$, compact and connected but not simply connected.

---

# Part V: The Adjoint Representation and Structure

## 15. The Adjoint Representation

For $g \in G$, conjugation $\Psi_g(h) = ghg^{-1}$ fixes $e$, so its derivative at $e$ is an invertible linear map

$$
\operatorname{Ad}_g = d(\Psi_g)_e \in GL(\mathfrak{g}).
$$

The map $\operatorname{Ad} : G \to GL(\mathfrak{g})$, $g \mapsto \operatorname{Ad}_g$, is a smooth Lie group homomorphism, the **adjoint representation** of $G$; each $\operatorname{Ad}_g$ preserves the bracket, $\operatorname{Ad}_g[X,Y] = [\operatorname{Ad}_gX, \operatorname{Ad}_gY]$, and for a matrix group $\operatorname{Ad}_gX = gXg^{-1}$. Its derivative at the identity is the **adjoint representation of the Lie algebra**

$$
\operatorname{ad} = d\operatorname{Ad}_e : \mathfrak{g} \to \mathfrak{gl}(\mathfrak{g}), \qquad \operatorname{ad}_XY = [X,Y].
$$

The Jacobi identity is exactly the statement that $\operatorname{ad}$ is a Lie algebra homomorphism:

$$
\operatorname{ad}_{[X,Y]} = [\operatorname{ad}_X, \operatorname{ad}_Y].
$$

For $g \in G$ and $X \in \mathfrak{g}$ one has

$$
g\exp(X)g^{-1} = \exp(\operatorname{Ad}_gX), \qquad \operatorname{Ad}_{\exp X} = e^{\operatorname{ad}_X} = \sum_{k \geq 0} \frac{\operatorname{ad}_X^k}{k!}.
$$

If $G$ is connected, then $\ker\operatorname{Ad} = Z(G)$, so the **adjoint group** satisfies $\operatorname{Ad}(G) \cong G/Z(G)$, with Lie algebra $\operatorname{ad}(\mathfrak{g}) \cong \mathfrak{g}/Z(\mathfrak{g})$. Connectedness is needed here: for $O(2)$, whose Lie algebra is abelian of dimension $1$, the rotations in $SO(2)$ act trivially on $\mathfrak{so}(2)$ while the reflections act by $-1$, so $\ker\operatorname{Ad} = SO(2) \neq Z(O(2)) = \{\pm I\}$.

## 16. The Derived Subgroup; Solvable and Nilpotent Groups

The **commutator** of $g, h \in G$ is $[g,h] = ghg^{-1}h^{-1}$, and the **derived subgroup** $[G,G]$ is generated by all commutators. It is normal, and $G/[G,G]$ is the largest abelian quotient of $G$. Define the **derived series** by

$$
G^{(0)} = G, \qquad G^{(k+1)} = [G^{(k)},G^{(k)}],
$$

and the **lower central series** by

$$
G_0 = G, \qquad G_{k+1} = [G, G_k].
$$

The group $G$ is **solvable** if $G^{(k)} = \{e\}$ for some $k$, and **nilpotent** if $G_k = \{e\}$ for some $k$. Every nilpotent group is solvable, but not conversely. These definitions parallel those for Lie algebras, and for connected $G$ the two theories agree: $\operatorname{Lie}([G,G]) = [\mathfrak{g},\mathfrak{g}]$, and $G$ is solvable (respectively nilpotent) if and only if $\mathfrak{g}$ is.

Examples: abelian groups are nilpotent of step $1$; the Heisenberg group $H_3(\mathbb{R})$ is nilpotent of step $2$, with derived subgroup equal to its center; the invertible upper triangular matrices form a solvable group, whose unipotent subgroup (all diagonal entries $1$) is nilpotent; and for $n \geq 2$, $[\mathfrak{gl}_n,\mathfrak{gl}_n] = \mathfrak{sl}_n$ and $[\mathfrak{sl}_n,\mathfrak{sl}_n] = \mathfrak{sl}_n \neq 0$, so $\mathfrak{gl}_n$, hence $GL_n$, is neither solvable nor nilpotent. The underlying Lie algebra facts are Engel's theorem, that a finite-dimensional $\mathfrak{g}$ is nilpotent if and only if every $\operatorname{ad}_X$ is nilpotent, and Lie's theorem, that a solvable subalgebra of $\mathfrak{gl}(V)$ over an algebraically closed field of characteristic $0$ is simultaneously triangularizable.

## 17. Quotients by Normal Closed Subgroups

Let $N \subseteq G$ be a **closed normal subgroup**. Then $G/N$ carries a unique smooth manifold structure making the quotient map $\pi : G \to G/N$ a smooth surjective submersion; with it, $G/N$ is a Lie group and

$$
\operatorname{Lie}(G/N) \cong \mathfrak{g}/\mathfrak{n}, \qquad \mathfrak{n} = \operatorname{Lie}(N).
$$

The map $\pi$ is a principal $N$-bundle, and $G/N$ is connected, respectively compact, when $G$ is. More generally, for any closed subgroup $H$ the homogeneous space $G/H$ has a unique smooth structure making $\pi : G \to G/H$ a submersion, with $\dim G/H = \dim G - \dim H$; when $H$ is normal this is a Lie group. Closedness is essential: the quotient by a dense subgroup such as the irrational line of §12 is not a manifold.

**First isomorphism theorem.** For a Lie group homomorphism $\varphi : G \to H$, the kernel is a closed normal subgroup, the image is an immersed Lie subgroup, and $\varphi$ induces an isomorphism of Lie groups $G/\ker\varphi \cong \varphi(G)$.

Examples: $\mathbb{R}/\mathbb{Z} \cong S^1$, $\mathbb{R}^n/\mathbb{Z}^n \cong T^n$, $SU(2)/\{\pm1\} \cong SO(3) \cong \mathbb{RP}^3$, $U(n)/SU(n) \cong U(1)$, $GL_n(\mathbb{R})/SL_n(\mathbb{R}) \cong \mathbb{R}^\times$, and $G/[G,G]$ is the maximal abelian quotient, equal to $\mathbb{R}^2$ for the Heisenberg group.

---

# Part VI: Summary

## 19. Lie Groups in the Wider Corpus

- The group of units of the biquaternion algebra is $\mathbb{B}^\times \cong GL_2(\mathbb{C})$, a real Lie group of dimension $8$ whose Lie algebra is $\mathfrak{gl}_2(\mathbb{C})$ with the commutator bracket, in agreement with *Lie Algebras: Categorization*; the biquaternion exponential is treated in a separate article of the biquaternion series.
- The unit quaternions form $S^3 \cong SU(2) \cong Sp(1)$, the double cover of $SO(3)$, and $SL_2(\mathbb{C})$ is the double cover of the identity component $SO^+(1,3)$ of the Lorentz group.
- The spin groups $\operatorname{Spin}(n)$ for $n \geq 3$, the universal covers of $SO(n)$, link this article to the Clifford algebra and spinor articles of the series.

---

## Summary

- A Lie group is a group and a smooth manifold with smooth group operations; the classical matrix groups $GL_n$, $SL_n$, $O(n)$, $SO(n)$, $U(n)$, $SU(n)$, $Sp(n)$, and $Sp(2n,\mathbb{R})$ are the basic examples, with real dimensions as in §3.
- Its Lie algebra $\mathfrak{g} = T_eG$ is the space of left-invariant vector fields with the commutator bracket; for matrix groups $[X,Y] = XY - YX$.
- The exponential map is a local diffeomorphism at $0$, natural in homomorphisms, and surjective for connected compact groups, connected nilpotent groups, and $GL_n(\mathbb{C})$, but not in general.
- Lie group homomorphisms differentiate to Lie algebra homomorphisms, and the differential functor is an equivalence between simply connected Lie groups and finite-dimensional real Lie algebras; Lie subalgebras correspond to connected immersed Lie subgroups, closed subgroups being embedded.
- The adjoint representation $\operatorname{Ad}$ differentiates to $\operatorname{ad}$, with $\ker\operatorname{Ad} = Z(G)$ for connected $G$; for such $G$, solvability and nilpotency of $G$ and $\mathfrak{g}$ coincide, and quotients by closed normal subgroups have Lie algebra $\mathfrak{g}/\mathfrak{n}$.

## Further Reading

- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations: An Elementary Introduction* (Springer, 2nd ed. 2015).
- John Stillwell, *Naive Lie Theory* (Springer, 2008).
- John M. Lee, *Introduction to Smooth Manifolds* (Springer, 2nd ed. 2013).
- Frank W. Warner, *Foundations of Differentiable Manifolds and Lie Groups* (Springer, 1983).
- Wulf Rossmann, *Lie Groups: An Introduction Through Linear Groups* (Oxford University Press, 2002).
- V. S. Varadarajan, *Lie Groups, Lie Algebras, and Their Representations* (Springer, 1984).
- Anthony W. Knapp, *Lie Groups Beyond an Introduction* (Birkhäuser, 2nd ed. 2002).
- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (American Mathematical Society, 2001).
- J. J. Duistermaat and J. A. C. Kolk, *Lie Groups* (Springer, 2000).
- Jean-Pierre Serre, *Lie Algebras and Lie Groups* (Springer, 1992).
- David S. Dummit and Richard M. Foote, *Abstract Algebra* (Wiley, 3rd ed. 2004).
