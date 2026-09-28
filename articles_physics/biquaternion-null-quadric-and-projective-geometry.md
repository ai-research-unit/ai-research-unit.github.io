# __Biquaternion Null Quadric and Projective Geometry__

## Introduction

The biquaternion norm $N(\tilde{Q})=\tilde{Q}\bar{\tilde{Q}}=\sum_{\mu=0}^{3} Q_\mu^2$ decides invertibility (*Biquaternion Norm and Invertibility*) and vanishes exactly on the zero divisors together with the origin (*Biquaternion Zero Divisors*). Both treatments are algebraic; this article treats the form geometrically, as the equation of a quadric.

The plan: describe the null cone, a cone over the Segre variety $\mathbb{P}^1\times\mathbb{P}^1$; place the picture in the classical projective geometry of lines in $\mathbb{P}^3$, namely the Klein quadric and the Plücker embedding; and state carefully how the quadric is related to the Lorentz group. Everything here is standard; no new results are claimed. The physical reading of the figure is given at the end of the article. The polarisation of the biquaternion norm, its real forms and its associated Clifford algebra are in *Biquaternion Norm and Invertibility*; the Lorentzian and conformal reading of the real slices is in *Biquaternion Lorentzian and Conformal Geometry*.

Physically the null quadric is the celestial sphere of the light cone: a null direction of Minkowski space is a point of $Q^2\cong\mathbb{P}^1\times\mathbb{P}^1$, and the two rulings of the quadric are the left- and right-handed Weyl spinors. The polarity of the quadric is the Hodge duality of the field strengths, the map that exchanges the electric and magnetic fields.

**Conventions.** The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0=1,e_1,e_2,e_3$ and central scalar imaginary $i$; a general element is $\tilde{Q}=\sum_{\mu=0}^{3} Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$. The criterion of *Biquaternion Norm and Invertibility* is used without proof: $N(\tilde{Q})\neq0$ if and only if $\tilde{Q}$ is invertible, and $N(\tilde{Q})=0$ with $\tilde{Q}\neq0$ if and only if $\tilde{Q}$ is a zero divisor.

---

## The null cone

The null cone is
$$
\mathcal{N}=\{\tilde{Q}\in\mathbb{B}:N(\tilde{Q})=0\}.
$$
It is one complex quadratic equation in four complex variables: a complex hypersurface of complex dimension $3$ and real dimension $6$, and a cone, since $N$ is homogeneous. The polynomial $N$ is irreducible, and its gradient $2(Q_0,Q_1,Q_2,Q_3)$ vanishes only at the origin, so $\mathcal{N}$ is irreducible with $0$ as its only singular point; the punctured cone $\mathcal{N}\setminus\{0\}$ is a smooth complex $3$-manifold. By the criterion above it is exactly the zero-divisor set:
$$
\{\text{zero divisors}\}=\mathcal{N}\setminus\{0\}=\{\tilde{Q}\neq0:N(\tilde{Q})=0\}.
$$

## The Segre embedding

Choose on $\mathbb{B}$ the linear coordinates
$$
X_0=Q_0-iQ_3,\qquad X_1=-iQ_1-Q_2,\qquad X_2=-iQ_1+Q_2,\qquad X_3=Q_0+iQ_3,
$$
an invertible $\mathbb{C}$-linear change of the coordinates $Q_0,\dots,Q_3$. In them the norm is a split form,
$$
N(\tilde{Q})=\sum_{\mu=0}^{3}Q_\mu^2=X_0X_3-X_1X_2,
$$
since $X_0X_3=(Q_0-iQ_3)(Q_0+iQ_3)=Q_0^2+Q_3^2$ and $X_1X_2=(-iQ_1-Q_2)(-iQ_1+Q_2)=-Q_1^2-Q_2^2$. The null cone is therefore the affine hypersurface $X_0X_3=X_1X_2$, and each of its nonzero points is a pair of one-dimensional subspaces of $\mathbb{C}^2$. Indeed, for nonzero $u=(\alpha,\beta)$ and $v=(\gamma,\delta)$ the point
$$
(X_0,X_1,X_2,X_3)=(\alpha\gamma,\alpha\delta,\beta\gamma,\beta\delta)
$$
lies on the null cone, since $\alpha\gamma\cdot\beta\delta=\alpha\delta\cdot\beta\gamma$, and conversely every null point is of this form: if $X_0\neq0$ the pair $u=(1,X_2/X_0)$, $v=(X_0,X_1)$ reproduces it, and the other cases are the same argument applied to a coordinate that is nonzero. The pair is determined only up to $(u,v)\mapsto(\lambda u,\lambda^{-1}v)$. Projectivising gives the **Segre embedding**
$$
s:\mathbb{P}^1\times\mathbb{P}^1\longrightarrow\mathbb{P}^3,\qquad ([u],[v])\mapsto[\alpha\gamma:\alpha\delta:\beta\gamma:\beta\delta],
$$
whose image is exactly the projective null quadric
$$
\mathbb{P}(\mathcal{N})=\{[\tilde{Q}]\in\mathbb{P}^3:N(\tilde{Q})=0\}.
$$
The affine null cone is the cone over the Segre variety $\mathbb{P}^1\times\mathbb{P}^1$, and the zero-divisor set is that cone with its apex removed.

## The two rulings of null planes

In the coordinates above the polar form of $N$ is
$$
B(X,Y)=\tfrac12\bigl(X_0Y_3+X_3Y_0-X_1Y_2-X_2Y_1\bigr),
$$
the polarisation of $X_0X_3-X_1X_2$, with $B(X,X)=N(X)$. For each $[u]=[\alpha:\beta]\in\mathbb{P}^1$ the two-dimensional subspace
$$
W_{[u]}=\operatorname{span}\{(\alpha,0,\beta,0),\,(0,\alpha,0,\beta)\}=\{(\alpha\sigma,\alpha\tau,\beta\sigma,\beta\tau):\sigma,\tau\in\mathbb{C}\}
$$
is totally isotropic: for $X$ built from $\sigma,\tau$ and $Y$ from $\sigma',\tau'$ the form above gives $B(X,Y)=\tfrac12\alpha\beta(\sigma\tau'+\tau\sigma'-\tau\sigma'-\sigma\tau')=0$. Since $\dim W_{[u]}=2$ is the maximal isotropic dimension for a non-degenerate form in dimension $4$, $W_{[u]}$ is a **null plane**, and the same holds for
$$
W^{[v]}=\operatorname{span}\{(\gamma,\delta,0,0),\,(0,0,\gamma,\delta)\},\qquad [v]=[\gamma:\delta].
$$
Their projectivisations $\ell_{[u]}=\mathbb{P}(W_{[u]})$ and $m_{[v]}=\mathbb{P}(W^{[v]})$ are the **two rulings**: each family is a $\mathbb{P}^1$ of lines; every quadric point lies on exactly one line of each family; lines of the same family are disjoint, while lines of different families meet in exactly one point, the point $[(\alpha\gamma,\alpha\delta,\beta\gamma,\beta\delta)]$ that the pair $([u],[v])$ determines.

---

## The projective null quadric $Q^2$

The projectivised null cone
$$
Q^2=\{[\tilde{Q}]\in\mathbb{P}^3:N(\tilde{Q})=0\}
$$
is a smooth irreducible quadric surface, isomorphic to $\mathbb{P}^1\times\mathbb{P}^1$; it is the classical **Segre quadric**. Non-degeneracy of $B$ gives smoothness, and over $\mathbb{C}$ all smooth quadric surfaces in $\mathbb{P}^3$ are projectively equivalent.

Its real points depend on the real form of *Biquaternion Norm and Invertibility*, §*The Real Forms and Their Signatures*: empty for the definite form on $\mathbb{H}_{\mathbb{B}}$; the sphere $S^2$ for the Lorentzian form on $\mathbb{M}_+$ (or $\mathbb{M}_-$); the torus $S^1\times S^1$ for the split form of signature $(2,2)$. Only in the split case does the real quadric contain real lines.

## Lines in $\mathbb{P}^3$, the Klein quadric, and the Plücker embedding

A line in $\mathbb{P}^3$ is $\mathbb{P}(U)$ for a two-dimensional subspace $U\subset\mathbb{C}^4$. With a basis $x,y$ of $U$, the **Plücker coordinates** are the six minors
$$
p_{ij}=x_iy_j-x_jy_i,\qquad 0\le i < j\le3,
$$
the coordinates of the decomposable bivector $x\wedge y\in\Lambda^2\mathbb{C}^4$, defined up to an overall scalar. This gives the **Plücker embedding**
$$
\mathrm{Gr}(2,4)\hookrightarrow\mathbb{P}(\Lambda^2\mathbb{C}^4)=\mathbb{P}^5,
$$
whose image is the **Klein quadric**, the quadric hypersurface of dimension $4$ cut out by the Plücker relation
$$
p_{01}p_{23}-p_{02}p_{13}+p_{03}p_{12}=0 .
$$
Over $\mathbb{R}$ the Plücker form has signature $(3,3)$. This Klein quadric in $\mathbb{P}^5$ is distinct from the null quadric $Q^2$ in $\mathbb{P}^3$: it is the variety of lines of the projective space in which $Q^2$ sits.

The rulings of $Q^2$ appear in this picture as follows. A line of $Q^2$ is a maximal isotropic two-plane, and its Plücker point lies on the Klein quadric. The lines on $Q^2$ form two components, the two rulings, each a $\mathbb{P}^1$; their Plücker images are two conics on the Klein quadric. (The maximal isotropic subspaces of the Klein quadric itself are two families of projective planes $\mathbb{P}^2$: the stars of lines through a fixed point and the plane fields of lines in a fixed plane.)

## Tangency and polarity

The form $B$ defines a **polarity**, the correlation
$$
[\tilde{P}]\longmapsto[\tilde{P}]^{\perp}=\{[\tilde{Q}]:B(\tilde{P},\tilde{Q})=0\},
$$
well defined by bilinearity and bijective by non-degeneracy. The quadric is the locus of self-polar points, $[\tilde{P}]\in Q^2\iff B(\tilde{P},\tilde{P})=0$. For $[\tilde{P}]\in Q^2$, since the differential of $N$ at $\tilde{P}$ is $2B(\tilde{P},\cdot\,)$, the polar hyperplane is the **tangent hyperplane**, and its intersection with the quadric is the pair of ruling lines through $[\tilde{P}]$,
$$
Q^2\cap[\tilde{P}]^{\perp}=\ell_{[u]}\cup m_{[v]},
$$
one line from each family. For two distinct null points $[\tilde{P}],[\tilde{Q}]$, the biquaternion norm on the line $\tilde{P}+t\tilde{Q}$ is $2t\,B(\tilde{P},\tilde{Q})$, so
$$
[\tilde{P}][\tilde{Q}]\subset Q^2\iff B(\tilde{P},\tilde{Q})=0,
$$
in which case the two points lie on a common ruling line. A line through $[\tilde{P}]\in Q^2$ is therefore tangent exactly when its direction lies in the tangent hyperplane; the two ruling lines are tangent, and every other tangent line meets the quadric only at $[\tilde{P}]$.

---

## Automorphisms of the complex quadric

The projective automorphisms of $Q^2$ are induced by the complex orthogonal group of $N$:
$$
\operatorname{Aut}(Q^2)\cong PO_4(\mathbb{C})=O_4(\mathbb{C})/\{\pm I\},
$$
acting on $\mathbb{P}^1\times\mathbb{P}^1$ by $([u],[v])\mapsto([Au],[Bv])$, with the $\mathbb{Z}/2$ exchanging the rulings. Its identity component $PSO_4(\mathbb{C})$ preserves each ruling; the outer component swaps them.
**Physical reading: the celestial sphere and the Hodge duality.** The projective null quadric $Q^2\cong\mathbb{P}^1\times\mathbb{P}^1$ is the celestial sphere of the light cone: a null direction of the material sector $\mathbb{M}_-$ is a point of $Q^2$, and the two rulings are the two chiralities of the massless field, one family of spinor lines for each. The tangency and polarity of the quadric are then the Hodge duality $\star$: on a bivector it is the map that exchanges the electric and magnetic fields, so the self-dual and anti-self-dual parts of a field strength are the two rulings read on the field, the Riemann–Silberstein combination of *Electric–Magnetic Duality and the Modular Group in Biquaternionic Form* and the free-field content of *Biquaternion Electromagnetism*.

## Summary

- $N$ is a non-degenerate quadratic form on $\mathbb{B}\cong\mathbb{C}^4$, with polar form the complex dot product $B=\sum_\mu P_\mu Q_\mu$ and orthonormal basis $e_0,\dots,e_3$; the polarisation and the real forms are in *Biquaternion Norm and Invertibility*.
- The null cone is a complex cone of dimension $3$ (real dimension $6$), smooth away from the origin and, punctured, exactly the zero-divisor set; in the coordinates of §*The Segre embedding* its nonzero points are the points with $X_0X_3 = X_1X_2$.
- The projectivised null cone is the smooth quadric $Q^2\cong\mathbb{P}^1\times\mathbb{P}^1$, and the null cone is the affine cone over it. The two rulings are the two families of maximal isotropic null planes, each a $\mathbb{P}^1$.
- A null point determines and is determined by a pair $([u],[v])\in\mathbb{P}^1\times\mathbb{P}^1$, the two rulings being the families obtained by fixing one member of the pair.
- The quadric sits in the Plücker–Klein geometry of lines in $\mathbb{P}^3$; its rulings are two conics on the Klein quadric, and tangency and polarity come from the form $B$.
- $\operatorname{Aut}(Q^2)\cong PO_4(\mathbb{C})$, while the proper orthochronous Lorentz group $SO^+(1,3)$ is the conformal group of the projective null cone $S^2$, not the automorphism group of the complex quadric; the geometry of the real slices is in *Biquaternion Lorentzian and Conformal Geometry*. The physical reading is that the complex quadric is the celestial sphere of the light cone, its two rulings the two Weyl chiralities, and its polarity the Hodge duality of the electromagnetic field.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $N(\tilde{Q}) = \sum_{\mu=0}^{3} Q_\mu^2$ | Biquaternion norm on $\mathbb{B} \cong \mathbb{C}^4$ |
| $B(\tilde{P},\tilde{Q}) = \sum_\mu P_\mu Q_\mu$ | Polar form of $N$, the complex bilinear dot product; $B(e_\mu,e_\nu) = \delta_{\mu\nu}$ |
| $X_0,\dots,X_3$ | Linear coordinates on $\mathbb{B}$ in which $N = X_0X_3 - X_1X_2$; see §*The Segre embedding* |
| $\mathcal{N} = \{\tilde{Q} : N(\tilde{Q}) = 0\}$ | Affine null cone; punctured, it is exactly the zero-divisor set |
| $Q^2 = \mathbb{P}(\mathcal{N})$ | Projective null quadric in $\mathbb{P}^3$ |
| $s : \mathbb{P}^1 \times \mathbb{P}^1 \to \mathbb{P}^3$ | Segre embedding, $([u],[v]) \mapsto [\alpha\gamma:\alpha\delta:\beta\gamma:\beta\delta]$; its image is $Q^2$ |
| $[u] = [\alpha:\beta]$, $[v] = [\gamma:\delta]$ | The two factors of a null point, determined up to $(u,v)\mapsto(\lambda u,\lambda^{-1}v)$ |
| $\ell_{[u]}, m_{[v]}$ | The two rulings of $Q^2$; the lines through $[\tilde{P}] \in Q^2$ |
| $p_{ij} = x_i y_j - x_j y_i$ | Plücker coordinates; the Klein quadric in $\mathbb{P}^5$ is their Plücker locus |
| $\operatorname{Aut}(Q^2) \cong PO_4(\mathbb{C})$ | Projective automorphisms of the quadric |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed., 2001).
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995).
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989).
- Joe Harris, *Algebraic Geometry: A First Course* (Springer, 1992).
- Phillip Griffiths and Joseph Harris, *Principles of Algebraic Geometry* (Wiley, 1978).
- William Fulton and Joe Harris, *Representation Theory: A First Course* (Springer, 1991).
- Igor R. Shafarevich, *Basic Algebraic Geometry 1: Varieties in Projective Space* (Springer, 3rd ed., 2013).
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, 1997).
