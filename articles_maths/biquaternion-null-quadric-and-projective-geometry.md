# __Biquaternion Null Quadric and Projective Geometry__

## Introduction

The norm form $N(\tilde{Q})=\tilde{Q}\bar{\tilde{Q}}=\sum_{\mu=0}^{3} Q_\mu^2$ decides invertibility (*Biquaternion Norm and Invertibility*) and vanishes exactly on the zero divisors together with the origin (*Biquaternion Zero Divisors*). Both treatments are algebraic; this article treats the form geometrically.

The plan: polarise $N$ and read $\mathbb{B}$ as a complex quadratic space; describe its null cone, a cone over the Segre variety $\mathbb{P}^1\times\mathbb{P}^1$; identify the two rulings of that variety with the two chiral spinor families; place the picture in the classical projective geometry of lines in $\mathbb{P}^3$, namely the Klein quadric and the Plﾃｼcker embedding; and state carefully how the quadric is related to the Lorentz group. Everything here is standard; no new results are claimed and no physics is invoked.

**Conventions.** The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0=1,e_1,e_2,e_3$ and central scalar imaginary $i$; a general element is $\tilde{Q}=\sum_{\mu=0}^{3} Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$. We use the isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$ of the article *Biquaternion Algebraic Representations*,
$$
\tilde{Q}\;\longmapsto\;\begin{pmatrix} Q_0 - iQ_3 & -iQ_1 - Q_2 \\ -iQ_1 + Q_2 & Q_0 + iQ_3 \end{pmatrix},
$$
under which $N$ becomes the determinant. The criterion of *Biquaternion Norm and Invertibility* is used without proof: $N(\tilde{Q})\neq0$ if and only if $\tilde{Q}$ is invertible, and $N(\tilde{Q})=0$ with $\tilde{Q}\neq0$ if and only if $\tilde{Q}$ is a zero divisor.

---

# Part I: The Norm Form as a Quadratic Space

## 1. The norm form and its polarization

$N(\tilde{Q})=\sum_{\mu=0}^{3} Q_\mu^2$ is homogeneous of degree two, hence is a quadratic form on $\mathbb{B}\cong\mathbb{C}^4$. Its polar form is
$$
B(\tilde{P},\tilde{Q})=\tfrac{1}{2}\bigl(N(\tilde{P}+\tilde{Q})-N(\tilde{P})-N(\tilde{Q})\bigr)=\sum_{\mu=0}^{3} P_\mu Q_\mu,
$$
the complex bilinear dot product. It is symmetric and non-degenerate, and the quaternion units are orthonormal:
$$
B(e_\mu,e_\nu)=\delta_{\mu\nu}.
$$
So $(\mathbb{B},N)$ is the standard non-degenerate quadratic space of dimension $4$ over $\mathbb{C}$. The form $B$ is complex-bilinear; it is not the Hermitian inner product $\sum_\mu P_\mu^*Q_\mu$ of the basic algebra article. Under $\mathbb{B}\cong M_2(\mathbb{C})$ the norm is the determinant, and for $2\times2$ matrices
$$
\det(X+Y)-\det X-\det Y=\operatorname{tr}(X)\operatorname{tr}(Y)-\operatorname{tr}(XY),
$$
so $B(X,Y)=\tfrac{1}{2}\bigl(\operatorname{tr}(X)\operatorname{tr}(Y)-\operatorname{tr}(XY)\bigr)$.

## 2. Real forms and split signature

Over $\mathbb{C}$ a non-degenerate quadratic form has no signature; signature appears only after a real form is chosen. With $Q_\mu=q_\mu+iq'_\mu$, $q_\mu,q'_\mu\in\mathbb{R}$,
$$
\operatorname{Re}N=\sum_{\mu=0}^{3}\bigl(q_\mu^2-q'_\mu{}^2\bigr),\qquad \operatorname{Im}N=2\sum_{\mu=0}^{3} q_\mu q'_\mu .
$$
Hence the realification $\operatorname{Re}N$ on $\mathbb{R}^8$ is non-degenerate of signature $(4,4)$, a **split** (neutral) signature; in the real basis $e_\mu,ie_\mu$ its matrix is $\operatorname{diag}(1,1,1,1,-1,-1,-1,-1)$. The six distinguished real subspaces $\mathbb{C}_{\mathbb{B}}, \mathrm{Vect}(\mathbb{B}), \mathbb{H}_{\mathbb{B}}, i\mathbb{H}_{\mathbb{B}}, \mathbb{M}_+, \mathbb{M}_-$ (the eigenspaces of the three involutions $\bar{\cdot},{}^{*},\dagger$ of the basic algebra article) give six real forms:

| Real subspace | $N$ restricted | Signature |
|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $q_0^2-(q'_0)^2$ | $(1,1)$ |
| $\mathrm{Vect}(\mathbb{B})$ | $q_1^2+q_2^2+q_3^2-(q'_1)^2-(q'_2)^2-(q'_3)^2$ | $(3,3)$ |
| $\mathbb{H}_{\mathbb{B}}$ | $\sum q_\mu^2$ | $(4,0)$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $-\sum (q'_\mu)^2$ | $(0,4)$ |
| $\mathbb{M}_+$ | $q_0^2-(q'_1)^2-(q'_2)^2-(q'_3)^2$ | $(1,3)$ |
| $\mathbb{M}_-$ | $-(q'_0)^2+q_1^2+q_2^2+q_3^2$ | $(3,1)$ |

Each is a real slice whose complexification is $(\mathbb{B},N)$. The full realification is split; the Lorentzian slice is $\mathbb{M}_+$, and up to sign $\mathbb{M}_-$.

## 3. The associated Clifford algebra

With the series convention $v^2=N(v)\cdot1$,
$$
\mathrm{Cl}(\mathbb{B},N)\cong\mathrm{Cl}_4(\mathbb{C})\cong M_4(\mathbb{C}),\qquad \mathrm{Cl}_{4,4}\cong M_{16}(\mathbb{R}),
$$
the second being the split real form of signature $(4,4)$, the case $p-q\equiv0\pmod 8$. The even part is
$$
\mathrm{Cl}^+(\mathbb{B},N)\cong\mathrm{Cl}_3(\mathbb{C})\cong M_2(\mathbb{C})\oplus M_2(\mathbb{C})\cong\mathbb{C}\otimes_{\mathbb{R}}\mathbb{B},
$$
whose two simple summands are the two chiralities, matched to the rulings in ﾂｧ7.

A caution. The biquaternion algebra itself is the even Clifford algebra $\mathbb{B}\cong\mathrm{Cl}^+_{1,3}$ of the Minkowski quadratic space of signature $(1,3)$ (*Spinors*). That is a different Clifford algebra, attached to a different quadratic space; it is not $\mathrm{Cl}(\mathbb{B},N)$.

---

# Part II: The Null Cone and Its Rulings

## 4. The null cone

The null cone is
$$
\mathcal{N}=\{\tilde{Q}\in\mathbb{B}:N(\tilde{Q})=0\}.
$$
It is one complex quadratic equation in four complex variables: a complex hypersurface of complex dimension $3$ and real dimension $6$, and a cone, since $N$ is homogeneous. The polynomial $N$ is irreducible, and its gradient $2(Q_0,Q_1,Q_2,Q_3)$ vanishes only at the origin, so $\mathcal{N}$ is irreducible with $0$ as its only singular point; the punctured cone $\mathcal{N}\setminus\{0\}$ is a smooth complex $3$-manifold. By the criterion above it is exactly the zero-divisor set:
$$
\{\text{zero divisors}\}=\mathcal{N}\setminus\{0\}=\{\tilde{Q}\neq0:N(\tilde{Q})=0\}.
$$

## 5. Rank-one description and the Segre embedding

Since $N$ is the determinant, the nonzero null elements are exactly the rank-one matrices. Such a matrix is an outer product
$$
A=uv^{T},\qquad u=\binom{\alpha}{\beta}\neq0,\quad v=\binom{\gamma}{\delta}\neq0,
$$
determined by $(u,v)$ up to $(u,v)\mapsto(\lambda u,\lambda^{-1}v)$. Projectivising gives the **Segre embedding**
$$
s:\mathbb{P}^1\times\mathbb{P}^1\longrightarrow\mathbb{P}^3,\qquad ([u],[v])\mapsto[uv^{T}]=[\alpha\gamma:\alpha\delta:\beta\gamma:\beta\delta].
$$
The matrix identity $A_{11}A_{22}=A_{12}A_{21}$, read through $A_{11}=Q_0-iQ_3$, $A_{22}=Q_0+iQ_3$, $A_{12}=-iQ_1-Q_2$, $A_{21}=-iQ_1+Q_2$, is
$$
(Q_0-iQ_3)(Q_0+iQ_3)=(-iQ_1-Q_2)(-iQ_1+Q_2)\iff Q_0^2+Q_3^2=-Q_1^2-Q_2^2,
$$
exactly $N(\tilde{Q})=0$. Hence
$$
\mathbb{P}(\mathcal{N})=\{[\tilde{Q}]\in\mathbb{P}^3:N(\tilde{Q})=0\}
$$
is the image of the Segre embedding. The affine null cone is the cone over the Segre variety $\mathbb{P}^1\times\mathbb{P}^1$, and the zero-divisor set is that cone with its apex removed. In particular a null biquaternion is parametrised by a pair of two-component spinors, as made explicit in ﾂｧ7.

## 6. The two rulings of null planes

For fixed $[u]$ the set $\ell_{[u]}=\{[uv^{T}]:v\in\mathbb{C}^2\}$ is a line in $\mathbb{P}^3$, and for fixed $[v]$ the set $m_{[v]}=\{[uv^{T}]:u\in\mathbb{C}^2\}$ is another. These are the **two rulings**, with the classical incidence properties: each is a $\mathbb{P}^1$ of lines; every quadric point lies on exactly one line of each family; lines of the same family are disjoint, while lines of different families meet in exactly one point.

In algebra language, $\ell_{[u]}=\mathbb{P}(W_u)$ with $W_u=\{uv^{T}:v\in\mathbb{C}^2\}$, and $W_u$ is totally isotropic:
$$
B(uv_1^{T},uv_2^{T})=0\qquad\text{for all }v_1,v_2\in\mathbb{C}^2,
$$
by the trace formula of ﾂｧ1 and $\operatorname{tr}(uv^{T})=v^{T}u$. Since $\dim W_u=2$ is the maximal isotropic dimension for a non-degenerate form in dimension $4$, these are the **null planes**; the two rulings are the two families $\{W_u\}$ and $\{W^v\}$.

## 7. Chirality: the primed and unprimed spinor lines

As a module over the complexified Lorentz algebra, the complexification of the Minkowski slice is the tensor product of the two Weyl spinor spaces of *Spinors*,
$$
\mathbb{B}\cong\Delta^+\otimes\Delta^-,\qquad \dim_{\mathbb{C}}\Delta^\pm=2,
$$
the complexified four-vector representation. A biquaternion is therefore a **mixed spinor** with one unprimed and one primed index, $A_\alpha{}^{\dot\beta}$, and the rank-one condition is exactly factorisability:
$$
A_\alpha{}^{\dot\beta}=\phi_\alpha\,\pi^{\dot\beta},\qquad \phi\in\Delta^+,\ \pi\in\Delta^- .
$$
Matching $A=uv^{T}$, the column $u$ is the unprimed spinor $\phi$ and the row $v^{T}$ the primed spinor $\pi$. Hence fixing $\phi$ and varying $\pi$ traces $\ell_{[\phi]}\cong\mathbb{P}(\Delta^-)=\mathbb{P}^1$, while fixing $\pi$ and varying $\phi$ traces $m_{[\pi]}\cong\mathbb{P}(\Delta^+)=\mathbb{P}^1$. The two rulings are the **primed and unprimed spinor lines**, and they correspond to the two chiralities, since the complexified algebra splits as
$$
\mathbb{C}\otimes_{\mathbb{R}}\mathbb{B}\cong M_2(\mathbb{C})\oplus M_2(\mathbb{C})
$$
into its two simple summands, the two chirality eigenspaces. Which half-spin module is named $\Delta^+$ is a convention.

---

# Part III: Projective Geometry of the Null Quadric

## 8. The projective null quadric $Q^2$

The projectivised null cone
$$
Q^2=\{[\tilde{Q}]\in\mathbb{P}^3:N(\tilde{Q})=0\}
$$
is a smooth irreducible quadric surface, isomorphic to $\mathbb{P}^1\times\mathbb{P}^1$; it is the classical **Segre quadric**. Non-degeneracy of $B$ gives smoothness, and over $\mathbb{C}$ all smooth quadric surfaces in $\mathbb{P}^3$ are projectively equivalent.

Its real points depend on the real form of ﾂｧ2: empty for the definite form on $\mathbb{H}_{\mathbb{B}}$; the sphere $S^2$ for the Lorentzian form on $\mathbb{M}_+$ (or $\mathbb{M}_-$); the torus $S^1\times S^1$ for the split form of signature $(2,2)$. Only in the split case does the real quadric contain real lines.

## 9. Lines in $\mathbb{P}^3$, the Klein quadric, and the Plﾃｼcker embedding

A line in $\mathbb{P}^3$ is $\mathbb{P}(U)$ for a two-dimensional subspace $U\subset\mathbb{C}^4$. With a basis $x,y$ of $U$, the **Plﾃｼcker coordinates** are the six minors
$$
p_{ij}=x_iy_j-x_jy_i,\qquad 0\le i<j\le3,
$$
the coordinates of the decomposable bivector $x\wedge y\in\Lambda^2\mathbb{C}^4$, defined up to an overall scalar. This gives the **Plﾃｼcker embedding**
$$
\mathrm{Gr}(2,4)\hookrightarrow\mathbb{P}(\Lambda^2\mathbb{C}^4)=\mathbb{P}^5,
$$
whose image is the **Klein quadric**, the quadric hypersurface of dimension $4$ cut out by the Plﾃｼcker relation
$$
p_{01}p_{23}-p_{02}p_{13}+p_{03}p_{12}=0 .
$$
Over $\mathbb{R}$ the Plﾃｼcker form has signature $(3,3)$. This Klein quadric in $\mathbb{P}^5$ is distinct from the null quadric $Q^2$ in $\mathbb{P}^3$: it is the variety of lines of the projective space in which $Q^2$ sits.

The rulings of $Q^2$ appear in this picture as follows. A line of $Q^2$ is a maximal isotropic two-plane, and its Plﾃｼcker point lies on the Klein quadric. The lines on $Q^2$ form two components, the two rulings, each a $\mathbb{P}^1$; their Plﾃｼcker images are two conics on the Klein quadric. (The maximal isotropic subspaces of the Klein quadric itself are two families of projective planes $\mathbb{P}^2$: the stars of lines through a fixed point and the plane fields of lines in a fixed plane.)

## 10. Tangency and polarity

The form $B$ defines a **polarity**, the correlation
$$
[\tilde{P}]\longmapsto[\tilde{P}]^{\perp}=\{[\tilde{Q}]:B(\tilde{P},\tilde{Q})=0\},
$$
well defined by bilinearity and bijective by non-degeneracy. The quadric is the locus of self-polar points, $[\tilde{P}]\in Q^2\iff B(\tilde{P},\tilde{P})=0$. For $[\tilde{P}]\in Q^2$, since the differential of $N$ at $\tilde{P}$ is $2B(\tilde{P},\cdot\,)$, the polar hyperplane is the **tangent hyperplane**, and its intersection with the quadric is the pair of ruling lines through $[\tilde{P}]$:
$$
Q^2\cap[\tilde{P}]^{\perp}=\ell_{[u]}\cup m_{[v]},\qquad \tilde{P}=uv^{T}.
$$
For two distinct null points $[\tilde{P}],[\tilde{Q}]$, the norm on the line $\tilde{P}+t\tilde{Q}$ is $2t\,B(\tilde{P},\tilde{Q})$, so
$$
[\tilde{P}][\tilde{Q}]\subset Q^2\iff B(\tilde{P},\tilde{Q})=0,
$$
in which case the two points lie on a common ruling line. A line through $[\tilde{P}]\in Q^2$ is therefore tangent exactly when its direction lies in the tangent hyperplane; the two ruling lines are tangent, and every other tangent line meets the quadric only at $[\tilde{P}]$.

---

# Part IV: The Quadric and the Lorentz Group

## 11. Automorphisms of the complex quadric

The projective automorphisms of $Q^2$ are induced by the complex orthogonal group of $N$:
$$
\operatorname{Aut}(Q^2)\cong PO_4(\mathbb{C})=O_4(\mathbb{C})/\{\pm I\}\cong\bigl(PGL_2(\mathbb{C})\times PGL_2(\mathbb{C})\bigr)\rtimes\mathbb{Z}/2,
$$
acting on $\mathbb{P}^1\times\mathbb{P}^1$ by $([u],[v])\mapsto([Au],[Bv])$, with the $\mathbb{Z}/2$ exchanging the rulings. This is the projective form of the double cover $SL_2(\mathbb{C})\times SL_2(\mathbb{C})\to SO_4(\mathbb{C})$. The connected group $PSO_4(\mathbb{C})\cong PGL_2(\mathbb{C})\times PGL_2(\mathbb{C})$ preserves each ruling; the outer component swaps them.

## 12. The Minkowski slice and the conformal group

Take the Lorentzian real form $\mathbb{M}_+\cong\mathbb{R}^{1,3}$ of ﾂｧ2. Its null cone is the Minkowski null cone, whose projectivisation is the sphere
$$
\mathbb{P}(\mathcal{N}\cap\mathbb{M}_+)\cong S^2,
$$
the **celestial sphere** of null directions. This $S^2$ is a real slice of $Q^2$, the real locus of one real form.

The Lorentz group enters as its conformal group:
$$
SO^+(1,3)\cong PSL_2(\mathbb{C})\cong PGL_2(\mathbb{C}),
$$
with $SL_2(\mathbb{C})\to SO^+(1,3)$ the double cover, and this group acts on $S^2=\mathbb{C}\mathbb{P}^1$ by Mﾃｶbius transformations, the orientation-preserving conformal diffeomorphisms. The full Lorentz group $O(1,3)$ acts by all Mﾃｶbius transformations, $PGL_2(\mathbb{C})\rtimes\mathbb{Z}/2$, the extra $\mathbb{Z}/2$ being complex conjugation.

Two qualifications. First, $SO^+(1,3)$ is **not** the automorphism group of the complex quadric; that is the larger $PO_4(\mathbb{C})$ of ﾂｧ11 (complex dimension $6$, real dimension $12$), of which the Lorentz group is the group of a real form (real dimension $6$). Second, "conformal group" refers to conformal transformations of the celestial sphere $S^2$, not of Minkowski space: the conformal group of $\mathbb{R}^{1,3}$ is larger, the fifteen-dimensional $O(2,4)$ of the standard conformal compactification. The Lorentz group is the conformal group only of the projective null cone.

## 13. The split real form

For the split real form of signature $(2,2)$ the real quadric is
$$
S^1\times S^1\cong\mathbb{P}^1_{\mathbb{R}}\times\mathbb{P}^1_{\mathbb{R}},
$$
and the rulings are real, so the quadric is doubly ruled by real lines; the corresponding connected group is $SO^+(2,2)\cong PSL_2(\mathbb{R})\times PSL_2(\mathbb{R})$, acting on the two factors separately. In the Lorentzian case no real line lies on the real quadric: the real points form $S^2$, and the rulings exist only over $\mathbb{C}$. The signature thus decides whether the rulings are visible over $\mathbb{R}$ or only over $\mathbb{C}$.

---

# Part V: Summary

## Summary

- $N$ is a non-degenerate quadratic form on $\mathbb{B}\cong\mathbb{C}^4$, with polar form the complex dot product $B=\sum_\mu P_\mu Q_\mu$ and orthonormal basis $e_0,\dots,e_3$. Its realification has split signature $(4,4)$; the Lorentzian slice $\mathbb{M}_+$ has signature $(1,3)$.
- The associated Clifford algebra is $\mathrm{Cl}_4(\mathbb{C})\cong M_4(\mathbb{C})$, and $\mathrm{Cl}_{4,4}\cong M_{16}(\mathbb{R})$ for the split form; its even part has the two chiral summands. It is not the same as $\mathbb{B}\cong\mathrm{Cl}^+_{1,3}$.
- The null cone is a complex cone of dimension $3$ (real dimension $6$), smooth away from the origin and, punctured, exactly the zero-divisor set; under $\mathbb{B}\cong M_2(\mathbb{C})$ its points are the rank-one matrices.
- The projectivised null cone is the smooth quadric $Q^2\cong\mathbb{P}^1\times\mathbb{P}^1$, and the null cone is the affine cone over it. The two rulings are the two families of maximal isotropic null planes, each a $\mathbb{P}^1$.
- A null biquaternion is a factorisable mixed spinor $\phi_\alpha\pi^{\dot\beta}$; the two rulings are the primed and unprimed spinor lines, corresponding to the two chiralities.
- The quadric sits in the Plﾃｼcker窶適lein geometry of lines in $\mathbb{P}^3$; its rulings are two conics on the Klein quadric, and tangency and polarity come from the form $B$.
- $\operatorname{Aut}(Q^2)\cong PO_4(\mathbb{C})\cong(PGL_2(\mathbb{C})\times PGL_2(\mathbb{C}))\rtimes\mathbb{Z}/2$, while $SO^+(1,3)\cong PSL_2(\mathbb{C})$ is the conformal group of the projective null cone $S^2$, not the automorphism group of the complex quadric.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $N(\tilde{Q}) = \sum_{\mu=0}^{3} Q_\mu^2$ | Norm form on $\mathbb{B} \cong \mathbb{C}^4$; the determinant under $\mathbb{B} \cong M_2(\mathbb{C})$ |
| $B(\tilde{P},\tilde{Q}) = \sum_\mu P_\mu Q_\mu$ | Polar form of $N$, the complex bilinear dot product; $B(e_\mu,e_\nu) = \delta_{\mu\nu}$ |
| $\mathcal{N} = \{\tilde{Q} : N(\tilde{Q}) = 0\}$ | Affine null cone; punctured, it is exactly the zero-divisor set |
| $Q^2 = \mathbb{P}(\mathcal{N})$ | Projective null quadric in $\mathbb{P}^3$ |
| $s : \mathbb{P}^1 \times \mathbb{P}^1 \to \mathbb{P}^3$ | Segre embedding, $([u],[v]) \mapsto [uv^{T}]$; its image is $Q^2$ |
| $u = (\alpha,\beta)^{T}$, $v = (\gamma,\delta)^{T}$ | Two-component spinors parametrising a null biquaternion $A = uv^{T}$ |
| $A_\alpha{}^{\dot\beta}$ | Spinor form of a biquaternion, with one unprimed and one primed index |
| $\ell_{[u]}, m_{[v]}$ | The two rulings of $Q^2$; the lines through $[\tilde{P}] \in Q^2$ |
| $p_{ij} = x_i y_j - x_j y_i$ | Plücker coordinates; the Klein quadric in $\mathbb{P}^5$ is their Plücker locus |
| $\operatorname{Aut}(Q^2) \cong PO_4(\mathbb{C})$ | Projective automorphisms of the quadric |
| $\mathrm{Cl}_{1,3}^{+}$ | Even Clifford algebra, isomorphic to $\mathbb{B}$; distinct from $\mathrm{Cl}_4(\mathbb{C})$ |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed., 2001).
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995).
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989).
- Joe Harris, *Algebraic Geometry: A First Course* (Springer, 1992).
- Phillip Griffiths and Joseph Harris, *Principles of Algebraic Geometry* (Wiley, 1978).
- William Fulton and Joe Harris, *Representation Theory: A First Course* (Springer, 1991).
- Igor R. Shafarevich, *Basic Algebraic Geometry 1: Varieties in Projective Space* (Springer, 3rd ed., 2013).
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, 1997).
