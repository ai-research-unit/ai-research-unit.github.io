# __The Null Quadric and Its Projective Geometry__

## Introduction

The quaternion bilinear form of the biquaternion algebra, $\langle\tilde P,\tilde Q\rangle_{\natural}=\sum_{\mu=0}^{3}P_\mu Q_\mu$, is non-degenerate, and a non-degenerate form in four variables has a projective geometry: its null set is a quadric. This article is that geometry. The quadric, the two rulings of its null planes, its polarity and its automorphism group are the projective reading of the form, and they sit beside the affine reading of the same form on the algebra and on the six distinguished real subspaces.

The article is the companion of *The Isotropic Structure of the Quaternion Bilinear Form*, which reads the same form affinely — the cone of real dimension $6$, its isotropic lines, its restrictions to the six subspaces — and of *Biquaternion Forms and Algebraic Norms*, which owns the form, its diagonal and the algebraic norm it polarises. The cone whose projectivisation is the quadric is studied as a topological space, with no form entering, in *The Topology of the Zero-Divisor Cone*; the real forms of the form and their signatures are *Biquaternion Norm and Invertibility*; the Lorentzian and conformal reading of the real slices is *Biquaternion Lorentzian and Conformal Geometry*; the algebra and its fixed-point subspaces are *Biquaternions as a Vector Space over $\mathbb{C}$*; and the classical groups that act are *Lie Groups*.

**Scope.** The article owns the Segre embedding of the two rulings into $\mathbb{P}^3$, the projective quadric $Q^2$ with its real points, the Klein–Plücker geometry of the lines of $\mathbb{P}^3$ in which $Q^2$ sits, the polarity and the tangency it induces, and the automorphism group of the complex quadric. No physics is invoked and no new result about the algebra is claimed.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$, $e_k^{2}=-e_0$, and $\tilde Q=\sum_{\mu=0}^{3}Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$. The bilinear form is $\langle\tilde P,\tilde Q\rangle_{\natural}=\mathrm{Sc}(\tilde P\tilde Q^{\natural})=\sum_\mu P_\mu Q_\mu$; the projectivised null cone is $\mathbb{P}(\mathcal{N})\subset\mathbb{P}^3$.

## The Segre Embedding

Choose on $\mathbb{B}$ the linear coordinates

$$
Z_0=Q_0-iQ_3,\qquad Z_1=-iQ_1-Q_2,\qquad Z_2=-iQ_1+Q_2,\qquad Z_3=Q_0+iQ_3,
$$

an invertible $\mathbb{C}$-linear change of the coordinates $Q_0,\dots,Q_3$. In them the form is a split form,

$$
\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=\sum_{\mu=0}^{3}Q_\mu^2=Z_0Z_3-Z_1Z_2,
$$

since $Z_0Z_3=(Q_0-iQ_3)(Q_0+iQ_3)=Q_0^2+Q_3^2$ and $Z_1Z_2=(-iQ_1-Q_2)(-iQ_1+Q_2)=-Q_1^2-Q_2^2$. The null cone is therefore the affine hypersurface $Z_0Z_3=Z_1Z_2$, and each of its nonzero points is a pair of one-dimensional subspaces of $\mathbb{C}^2$. Indeed, for nonzero $u=(\alpha,\beta)$ and $v=(\gamma,\delta)$ the point

$$
(Z_0,Z_1,Z_2,Z_3)=(\alpha\gamma,\alpha\delta,\beta\gamma,\beta\delta)
$$

lies on the null cone, since $\alpha\gamma\cdot\beta\delta=\alpha\delta\cdot\beta\gamma$, and conversely every null point is of this form: if $Z_0\neq0$ the pair $u=(1,Z_2/Z_0)$, $v=(Z_0,Z_1)$ reproduces it, and the other cases are the same argument applied to a coordinate that is nonzero. The pair is determined only up to $(u,v)\mapsto(\lambda u,\lambda^{-1}v)$.

Projectivising gives the **Segre embedding**

$$
s:\mathbb{P}^1\times\mathbb{P}^1\longrightarrow\mathbb{P}^3,\qquad ([u],[v])\mapsto[\alpha\gamma:\alpha\delta:\beta\gamma:\beta\delta],
$$

whose image is exactly the projective null quadric

$$
\mathbb{P}(\mathcal{N})=\{[\tilde{Q}]\in\mathbb{P}^3:\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=0\}.
$$

The affine null cone is the cone over the Segre variety $\mathbb{P}^1\times\mathbb{P}^1$, and the zero-divisor set is that cone with its apex removed (*The Topology of the Zero-Divisor Cone*).

## The Two Rulings of Null Planes

In the coordinates above the polar form of $N$ is

$$
\langle\tilde R,\tilde S\rangle_{\natural}=\tfrac12\bigl(Z_0Z'_3+Z_3Z'_0-Z_1Z'_2-Z_2Z'_1\bigr),
$$

the polarisation of $Z_0Z_3-Z_1Z_2$, which returns the norm on the diagonal, $\langle\tilde R,\tilde R\rangle_{\natural}=N(\tilde R)$. For each $[u]=[\alpha:\beta]\in\mathbb{P}^1$ the two-dimensional subspace

$$
W_{[u]}=\operatorname{span}\{(\alpha,0,\beta,0),\,(0,\alpha,0,\beta)\}=\{(\alpha\sigma,\alpha\tau,\beta\sigma,\beta\tau):\sigma,\tau\in\mathbb{C}\}
$$

is totally isotropic: for $\tilde R$ built from $\sigma,\tau$ and $\tilde S$ from $\sigma',\tau'$ the form above gives $\langle\tilde R,\tilde S\rangle_{\natural}=\tfrac12\alpha\beta(\sigma\tau'+\tau\sigma'-\tau\sigma'-\sigma\tau')=0$. Since $\dim W_{[u]}=2$ is the maximal isotropic dimension for a non-degenerate form in dimension $4$, $W_{[u]}$ is a **null plane**, and the same holds for

$$
W^{[v]}=\operatorname{span}\{(\gamma,\delta,0,0),\,(0,0,\gamma,\delta)\},\qquad [v]=[\gamma:\delta].
$$

Their projectivisations $\ell_{[u]}=\mathbb{P}(W_{[u]})$ and $m_{[v]}=\mathbb{P}(W^{[v]})$ are the **two rulings**: each family is a $\mathbb{P}^1$ of lines; every quadric point lies on exactly one line of each family; lines of the same family are disjoint, while lines of different families meet in exactly one point, the point $[(\alpha\gamma,\alpha\delta,\beta\gamma,\beta\delta)]$ that the pair $([u],[v])$ determines.

## The Projective Null Quadric $Q^2$

The projectivised null cone

$$
Q^2=\{[\tilde{Q}]\in\mathbb{P}^3:\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=0\}
$$

is a smooth irreducible quadric surface, isomorphic to $\mathbb{P}^1\times\mathbb{P}^1$; it is the classical **Segre quadric**. Non-degeneracy of the form gives smoothness, and over $\mathbb{C}$ all smooth quadric surfaces in $\mathbb{P}^3$ are projectively equivalent.

Its real points depend on the real form of the bilinear form (*Biquaternion Norm and Invertibility*, §*The Real Forms and Their Signatures*): empty for the definite form on $\mathbb{H}_{\mathbb{B}}$; the sphere $S^2$ for the Lorentzian form on $\mathbb{M}_+$ (or $\mathbb{M}_-$); the torus $S^1\times S^1$ for the split form of signature $(2,2)$. Only in the split case does the real quadric contain real lines.

## Lines in $\mathbb{P}^3$, the Klein Quadric and the Plücker Embedding

A line in $\mathbb{P}^3$ is $\mathbb{P}(U)$ for a two-dimensional subspace $U\subset\mathbb{C}^4$. With a basis $\tilde Q,\tilde P$ of $U$, the **Plücker coordinates** are the six minors

$$
p_{ij}=Q_iP_j-Q_jP_i,\qquad 0\le i < j\le3,
$$

the coordinates of the decomposable bivector $\tilde Q\wedge\tilde P\in\Lambda^2\mathbb{C}^4$, defined up to an overall scalar. This gives the **Plücker embedding**

$$
\mathrm{Gr}(2,4)\hookrightarrow\mathbb{P}(\Lambda^2\mathbb{C}^4)=\mathbb{P}^5,
$$

whose image is the **Klein quadric**, the quadric hypersurface of dimension $4$ cut out by the Plücker relation

$$
p_{01}p_{23}-p_{02}p_{13}+p_{03}p_{12}=0 .
$$

Over $\mathbb{R}$ the Plücker form has signature $(3,3)$. This Klein quadric in $\mathbb{P}^5$ is distinct from the null quadric $Q^2$ in $\mathbb{P}^3$: it is the variety of lines of the projective space in which $Q^2$ sits.

The rulings of $Q^2$ appear in this picture as follows. A line of $Q^2$ is a maximal isotropic two-plane, and its Plücker point lies on the Klein quadric. The lines on $Q^2$ form two components, the two rulings, each a $\mathbb{P}^1$; their Plücker images are two conics on the Klein quadric. (The maximal isotropic subspaces of the Klein quadric itself are two families of projective planes $\mathbb{P}^2$: the stars of lines through a fixed point and the plane fields of lines in a fixed plane.)

## Tangency and Polarity

The form defines a **polarity**, the correlation

$$
[\tilde{P}]\longmapsto[\tilde{P}]^{\perp}=\{[\tilde{Q}]:\langle\tilde{P},\tilde{Q}\rangle_{\natural}=0\},
$$

well defined by bilinearity and bijective by non-degeneracy. The quadric is the locus of self-polar points, $[\tilde{P}]\in Q^2\iff \langle\tilde{P},\tilde{P}\rangle_{\natural}=0$. For $[\tilde{P}]\in Q^2$, since the differential of $N$ at $\tilde{P}$ is $2\langle\tilde{P},\cdot\,\rangle_{\natural}$, the polar hyperplane is the **tangent hyperplane**, and its intersection with the quadric is the pair of ruling lines through $[\tilde{P}]$,

$$
Q^2\cap[\tilde{P}]^{\perp}=\ell_{[u]}\cup m_{[v]},
$$

one line from each family. For two distinct null points $[\tilde{P}],[\tilde{Q}]$, the form on the line $\tilde{P}+t\tilde{Q}$ is $2t\,\langle\tilde{P},\tilde{Q}\rangle_{\natural}$, so

$$
[\tilde{P}][\tilde{Q}]\subset Q^2\iff \langle\tilde{P},\tilde{Q}\rangle_{\natural}=0,
$$

in which case the two points lie on a common ruling line. A line through $[\tilde{P}]\in Q^2$ is therefore tangent exactly when its direction lies in the tangent hyperplane; the two ruling lines are tangent, and every other tangent line meets the quadric only at $[\tilde{P}]$.

## Automorphisms of the Quadric

The projective automorphisms of $Q^2$ are induced by the complex orthogonal group of the form:

$$
\operatorname{Aut}(Q^2)\cong PO_4(\mathbb{C})=O_4(\mathbb{C})/\{\pm I\},
$$

acting on $\mathbb{P}^1\times\mathbb{P}^1$ by $([u],[v])\mapsto([Au],[Bv])$, with the $\mathbb{Z}/2$ exchanging the rulings. Its identity component $PSO_4(\mathbb{C})$ preserves each ruling; the outer component swaps them. The Lorentz group is not this group: $SO^+(1,3)$ is the conformal group of the projective null cone $S^2$ of the Lorentzian real form, not the automorphism group of the complex quadric.

## Summary

- The projective null cone $Q^2=\mathbb{P}(\mathcal{N})$ is the smooth irreducible quadric surface $\mathbb{P}^1\times\mathbb{P}^1$, the Segre quadric; the affine null cone is the cone over it and the zero-divisor set is that cone minus its apex.
- The **Segre embedding** $s:\mathbb{P}^1\times\mathbb{P}^1\to\mathbb{P}^3$, $([u],[v])\mapsto[\alpha\gamma:\alpha\delta:\beta\gamma:\beta\delta]$, has the quadric as its image; in the coordinates $Z_0,\dots,Z_3$ the form is $Z_0Z_3-Z_1Z_2$ and the quadric is the locus of self-polar points.
- The two **rulings** are the two families of maximal isotropic null planes, each a $\mathbb{P}^1$; every quadric point lies on exactly one line of each family.
- The quadric sits in the **Plücker–Klein geometry** of the lines of $\mathbb{P}^3$; its rulings are two conics on the Klein quadric in $\mathbb{P}^5$.
- The **polarity** of the form gives the tangency: at a point of the quadric the polar hyperplane is the tangent hyperplane and its intersection with the quadric is the pair of ruling lines through the point.
- $\operatorname{Aut}(Q^2)\cong PO_4(\mathbb{C})$, its identity component preserving each ruling and the outer component swapping them; the real points of the quadric are empty, $S^2$ or $S^1\times S^1$ according to the real form of the bilinear form.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle\tilde P,\tilde Q\rangle_{\natural} = \sum_\mu P_\mu Q_\mu$ | Bilinear form; polar form of the algebraic norm |
| $Z_0,\dots,Z_3$ | Linear coordinates in which the form is $Z_0Z_3 - Z_1Z_2$ |
| $\mathbb{P}(\mathcal{N}) = Q^2 \cong \mathbb{P}^1 \times \mathbb{P}^1$ | Projectivised null cone, the Segre quadric |
| $s : \mathbb{P}^1 \times \mathbb{P}^1 \to \mathbb{P}^3$ | Segre embedding, $([u],[v]) \mapsto [\alpha\gamma:\alpha\delta:\beta\gamma:\beta\delta]$ |
| $[u] = [\alpha:\beta]$, $[v] = [\gamma:\delta]$ | The two factors of a null point, up to $(u,v)\mapsto(\lambda u,\lambda^{-1}v)$ |
| $W_{[u]}$, $W^{[v]}$ | The two families of maximal isotropic null planes |
| $\ell_{[u]}, m_{[v]}$ | The two rulings of $Q^2$ |
| $p_{ij} = Q_i P_j - Q_j P_i$ | Plücker coordinates; the Klein quadric in $\mathbb{P}^5$ is their Plücker locus |
| $[\tilde{P}]^{\perp}$ | Polar hyperplane of $[\tilde{P}]$; the tangent hyperplane when $[\tilde{P}] \in Q^2$ |
| $\operatorname{Aut}(Q^2) \cong PO_4(\mathbb{C})$ | Projective automorphisms of the quadric |

## Further Reading

- William Kingdon Clifford, "Preliminary Sketch of Biquaternions", *Proceedings of the London Mathematical Society* **4** (1873) 381–395.
- Joe Harris, *Algebraic Geometry: A First Course* (Springer, 1992).
- Phillip Griffiths and Joseph Harris, *Principles of Algebraic Geometry* (Wiley, 1978).
- Igor R. Shafarevich, *Basic Algebraic Geometry 1: Varieties in Projective Space* (Springer, 3rd ed., 2013).
- William Fulton and Joe Harris, *Representation Theory: A First Course* (Springer, 1991).
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995).
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989).
