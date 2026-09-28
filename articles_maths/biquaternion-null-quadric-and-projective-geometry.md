# __Biquaternion Null Quadric and Projective Geometry__

## Introduction

The biquaternion norm $N(\tilde{Q})=\tilde{Q}\bar{\tilde{Q}}=\sum_{\mu=0}^{3} Q_\mu^2$ decides invertibility (*Biquaternion Norm and Invertibility*) and vanishes exactly on the zero divisors together with the origin (*Biquaternion Zero Divisors*). Both treatments are algebraic; this article treats the form geometrically, as the equation of a quadric.

The plan: place the quadric in the classical projective geometry of lines in $\mathbb{P}^3$, namely the Klein quadric and the Plücker embedding; describe its two rulings, its tangency and its polarity; and state carefully how it is related to the Lorentz group. Everything here is standard; no new results are claimed and no physics is invoked. The polarisation of the biquaternion norm, its real forms and its associated Clifford algebra are in *Biquaternion Norm and Invertibility*; the null cone, its Segre parametrisation and the zero-divisor set are in *Biquaternion Zero Divisors* and *Biquaternion Topology*; the chirality of the rulings is in *Biquaternion Representation Theory*; and the Lorentzian and conformal reading of the real slices is in *Biquaternion Lorentzian and Conformal Geometry*.

**Conventions.** The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0=1,e_1,e_2,e_3$ and central scalar imaginary $i$; a general element is $\tilde{Q}=\sum_{\mu=0}^{3} Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$. The criterion of *Biquaternion Norm and Invertibility* is used without proof: $N(\tilde{Q})\neq0$ if and only if $\tilde{Q}$ is invertible, and $N(\tilde{Q})=0$ with $\tilde{Q}\neq0$ if and only if $\tilde{Q}$ is a zero divisor.

---

## The two rulings of null planes

For fixed $[u]$ the set $\ell_{[u]}=\{[uv^{T}]:v\in\mathbb{C}^2\}$ is a line in $\mathbb{P}^3$, and for fixed $[v]$ the set $m_{[v]}=\{[uv^{T}]:u\in\mathbb{C}^2\}$ is another. These are the **two rulings**, with the classical incidence properties: each is a $\mathbb{P}^1$ of lines; every quadric point lies on exactly one line of each family; lines of the same family are disjoint, while lines of different families meet in exactly one point.

In algebra language, $\ell_{[u]}=\mathbb{P}(W_u)$ with $W_u=\{uv^{T}:v\in\mathbb{C}^2\}$, and $W_u$ is totally isotropic:
$$
B(uv_1^{T},uv_2^{T})=0\qquad\text{for all }v_1,v_2\in\mathbb{C}^2,
$$
by the trace formula of *Biquaternion Norm and Invertibility*, §*The Polarisation and the Complex Quadratic Space*, and $\operatorname{tr}(uv^{T})=v^{T}u$. Since $\dim W_u=2$ is the maximal isotropic dimension for a non-degenerate form in dimension $4$, these are the **null planes**; the two rulings are the two families $\{W_u\}$ and $\{W^v\}$.

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
p_{ij}=x_iy_j-x_jy_i,\qquad 0\le i<j\le3,
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
well defined by bilinearity and bijective by non-degeneracy. The quadric is the locus of self-polar points, $[\tilde{P}]\in Q^2\iff B(\tilde{P},\tilde{P})=0$. For $[\tilde{P}]\in Q^2$, since the differential of $N$ at $\tilde{P}$ is $2B(\tilde{P},\cdot\,)$, the polar hyperplane is the **tangent hyperplane**, and its intersection with the quadric is the pair of ruling lines through $[\tilde{P}]$:
$$
Q^2\cap[\tilde{P}]^{\perp}=\ell_{[u]}\cup m_{[v]},\qquad \tilde{P}=uv^{T}.
$$
For two distinct null points $[\tilde{P}],[\tilde{Q}]$, the biquaternion norm on the line $\tilde{P}+t\tilde{Q}$ is $2t\,B(\tilde{P},\tilde{Q})$, so
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

## Summary

- $N$ is a non-degenerate quadratic form on $\mathbb{B}\cong\mathbb{C}^4$, with polar form the complex dot product $B=\sum_\mu P_\mu Q_\mu$ and orthonormal basis $e_0,\dots,e_3$; the polarisation and the real forms are in *Biquaternion Norm and Invertibility*.
- The projectivised null cone is the smooth quadric $Q^2\cong\mathbb{P}^1\times\mathbb{P}^1$, and the null cone is the affine cone over it. The two rulings are the two families of maximal isotropic null planes, each a $\mathbb{P}^1$.
- The quadric sits in the Plücker–Klein geometry of lines in $\mathbb{P}^3$; its rulings are two conics on the Klein quadric, and tangency and polarity come from the form $B$.
- $\operatorname{Aut}(Q^2)\cong PO_4(\mathbb{C})$, while the proper orthochronous Lorentz group $SO^+(1,3)$ is the conformal group of the projective null cone $S^2$, not the automorphism group of the complex quadric; the geometry of the real slices is in *Biquaternion Lorentzian and Conformal Geometry*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $N(\tilde{Q}) = \sum_{\mu=0}^{3} Q_\mu^2$ | Biquaternion norm on $\mathbb{B} \cong \mathbb{C}^4$ |
| $B(\tilde{P},\tilde{Q}) = \sum_\mu P_\mu Q_\mu$ | Polar form of $N$, the complex bilinear dot product; $B(e_\mu,e_\nu) = \delta_{\mu\nu}$ |
| $\mathcal{N} = \{\tilde{Q} : N(\tilde{Q}) = 0\}$ | Affine null cone; punctured, it is exactly the zero-divisor set |
| $Q^2 = \mathbb{P}(\mathcal{N})$ | Projective null quadric in $\mathbb{P}^3$ |
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
