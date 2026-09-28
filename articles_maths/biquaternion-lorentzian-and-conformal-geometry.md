# __Biquaternion Lorentzian and Conformal Geometry__

## Introduction

The biquaternion algebra carries two real slices whose geometries differ, and this article reads both. The Lorentzian slice is Minkowski space with its light cone and its null lines; the split slice carries a neutral signature and a real quadric ruled by real lines. The two are the real loci of the complex null quadric, and on the celestial sphere of the Lorentzian slice the Lorentz group acts as the conformal group. The conformal model of Euclidean space, in which spheres and planes become vectors and the transformations become versors, is the further picture the algebra supports.

The article presupposes the biquaternion norm and its real forms (*Biquaternion Norm and Invertibility*), which fixed the signatures $(4,4)$, $(1,1)$, $(3,3)$, $(4,0)$, $(0,4)$, $(1,3)$ and $(3,1)$, and the projective picture of the null quadric (*Biquaternion Null Quadric and Projective Geometry*), whose rulings and real forms are used here. The pseudo-Riemannian, Lorentzian and conformal articles of Part IV are cited and not restated.

**Conventions.** The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0=1,e_1,e_2,e_3$ and central scalar imaginary $i$; a general element is $\tilde{Q}=\sum_{\mu=0}^{3} Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$. The criterion of *Biquaternion Norm and Invertibility* is used without proof: $N(\tilde{Q})\neq0$ if and only if $\tilde{Q}$ is invertible, and $N(\tilde{Q})=0$ with $\tilde{Q}\neq0$ if and only if $\tilde{Q}$ is a zero divisor.

---

## The Lorentzian Slice and Its Light Cone

By the table of *Biquaternion Norm and Invertibility*, §*The Real Forms and Their Signatures*, the restriction of $N$ to $\mathbb{M}_-$ is real of signature $(3,1)$, and on $\mathbb{M}_+$ it is $(1,3)$; in real coordinates $\tilde{Q}=iq'_0e_0+q_1e_1+q_2e_2+q_3e_3\in\mathbb{M}_-$ this reads $N(\tilde{Q})=-(q'_0)^2+q_1^2+q_2^2+q_3^2$. Either subspace is thereby identified with Minkowski space $\mathbb{R}^{1,3}$, and its null set,

$$
N(\tilde{Q})=0\iff(q'_0)^2=q_1^2+q_2^2+q_3^2,
$$

is the **light cone**, a double cone with apex at the origin. With this identification, the **null biquaternions of the Minkowski subspace** are exactly the elements of the light cone.

Intersecting with the unit sphere of $\mathbb{M}_-\cong\mathbb{R}^4$ gives $q'_0=\pm1/\sqrt2$ and $q_1^2+q_2^2+q_3^2=1/2$, so the link of the light cone is the disjoint union

$$
S^2\sqcup S^2,
$$

one sphere per nappe. Each nappe is the cone on its sphere, and the complement of the light cone in $\mathbb{M}_-$ has exactly three connected components, the future timelike, past timelike and spacelike regions, as in *Biquaternion Norm and Invertibility*.

Two warnings are in order: the light cone is a real cone of real dimension $3$ in $\mathbb{M}_-\cong\mathbb{R}^4$, not the full null cone $\mathcal{N}$ of *Biquaternion Null Quadric and Projective Geometry*, §*The null cone*, which has real dimension $6$; and $\mathcal{N}$ is the complex cone over the Segre quadric, whose intersection with $\mathbb{M}_-$ recovers the light cone, so the Minkowski null biquaternions form a three-dimensional real cone while the null elements of the full algebra form a six-dimensional one.

## The Lorentzian Reading of the Quadric

Take the Lorentzian real form $\mathbb{M}_+\cong\mathbb{R}^{1,3}$ of *Biquaternion Norm and Invertibility*, §*The Real Forms and Their Signatures*. Its null cone is the Minkowski null cone, whose projectivisation is the sphere
$$
\mathbb{P}(\mathcal{N}\cap\mathbb{M}_+)\cong S^2,
$$
the **celestial sphere** of null directions. This $S^2$ is a real slice of $Q^2$, the real locus of one real form.

The Lorentz group enters as its conformal group:
The proper orthochronous Lorentz group $SO^+(1,3)$ acts on $S^2=\mathbb{C}\mathbb{P}^1$ by Möbius transformations, the orientation-preserving conformal diffeomorphisms, and the full Lorentz group $O(1,3)$ acts by all Möbius transformations, the additional ones being complex conjugation.

Two qualifications. First, $SO^+(1,3)$ is **not** the automorphism group of the complex quadric; that is the larger $PO_4(\mathbb{C})$ of *Biquaternion Null Quadric and Projective Geometry*, §*Automorphisms of the complex quadric* (complex dimension $6$, real dimension $12$), of which the Lorentz group is the group of a real form (real dimension $6$). Second, "conformal group" refers to conformal transformations of the celestial sphere $S^2$, not of Minkowski space: the conformal group of $\mathbb{R}^{1,3}$ is larger, the fifteen-dimensional $O(2,4)$ of the standard conformal compactification. The Lorentz group is the conformal group only of the projective null cone.

## The Conformal Group and the Conformal Model

The Lorentz group is the conformal group of the projective null cone. The conformal group of the Minkowski space itself is larger, and it is the group the conformal model of Euclidean space is built from.

**The group.** The conformal compactification of $\mathbb{R}^{1,3}$ is a quadric in $\mathbb{R}^{2,4}$, and its transformation group is $O(2,4)$, of real dimension $15$; its identity component is $SO^+(2,4)\cong SO(4,2)$. Its double cover is
$$
SU(2,2)\cong Spin(4,2),
$$
acting on a four-dimensional complex space that carries a Hermitian form of signature $(2,2)$, the biquaternion algebra read as a complex vector space. The fifteen dimensions are the six of the Lorentz group, the four of the translations, the four of the special conformal transformations, and the dilation.

**The model.** In the conformal model of Euclidean space $\mathbb{R}^n$ the flat space is recovered from a null cone in $\mathbb{R}^{n+1,1}$. Two null vectors are distinguished, the origin $n$ and the point at infinity $n_\infty$, with $B(n,n_\infty)=-1$; a point $X\in\mathbb{R}^n$ is represented by a null vector whose inner products with $n$ and $n_\infty$ fix its coordinates. In this model a sphere is the vector $S=P-\tfrac12 r^2 n_\infty$ for a point $P$ and a radius $r$, a plane is a vector orthogonal to $n_\infty$, and a point lies on a sphere or a plane exactly when the corresponding vectors are orthogonal. The transformations of the model are the versors of the Clifford algebra $\mathrm{Cl}_{n+1,1}$, acting by the twisted adjoint action; in the matrix form of the Vahlen matrices they are the analogues of the Möbius transformations, and the sandwich action of a biquaternion on the projective line (*Biquaternion Automorphisms and Derivations*) is the case $n=2$.

The construction, its null vectors and its versor action are those of *The Conformal Model of Euclidean Space*, and the Lorentzian framework is that of *Pseudo-Riemannian and Lorentzian Geometry*, both of Part IV; nothing beyond the cited statements is used here.

## The Split Slice

For the split real form of signature $(2,2)$ the real quadric is
$$
S^1\times S^1\cong\mathbb{P}^1_{\mathbb{R}}\times\mathbb{P}^1_{\mathbb{R}},
$$
and the rulings are real, so the quadric is doubly ruled by real lines; the corresponding connected group is $SO^+(2,2)$, acting on the two factors separately. In the Lorentzian case no real line lies on the real quadric: the real points form $S^2$, and the rulings exist only over $\mathbb{C}$. The signature thus decides whether the rulings are visible over $\mathbb{R}$ or only over $\mathbb{C}$.

---

## Summary

The algebra carries two real slices with distinct geometries. The Lorentzian slice $\mathbb{M}_\pm$ is Minkowski space: its null set is the light cone, a real double cone of real dimension $3$ whose link is $S^2\sqcup S^2$ and whose complement has three connected components, and it is the real slice of the complex null cone, of dimension $6$. On its celestial sphere $S^2$ the proper orthochronous Lorentz group acts by Möbius transformations, so that the Lorentz group is the conformal group of the projective null cone — not the automorphism group of the complex quadric, which is the larger $PO_4(\mathbb{C})$.

The conformal group of Minkowski space itself is the larger $O(2,4)$, with identity component $SO(4,2)$ and double cover $SU(2,2)\cong Spin(4,2)$. In the conformal model of Euclidean space the flat space is recovered from a null cone, the distinguished null vectors $n$ and $n_\infty$ mark the origin and the point at infinity, the spheres and planes are vectors, and the transformations are versors of a Clifford algebra, acting as the Möbius transformations do on the projective line.

The split slice is the neutral case. Its real quadric is $S^1\times S^1$, ruled by real lines, and its group is $SO^+(2,2)$ acting on the two factors; in the Lorentzian case no real line lies on the real quadric, and the rulings exist only over $\mathbb{C}$. The signature alone decides whether the rulings are visible over $\mathbb{R}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{M}_+\cong\mathbb{R}^{1,3}$, $\mathbb{M}_-\cong\mathbb{R}^{3,1}$ | The Lorentzian real slices of $\mathbb{B}$ |
| Light cone in $\mathbb{M}_\pm$ | Null set of the restricted form; real double cone of dimension $3$, link $S^2\sqcup S^2$ |
| $\mathbb{P}(\mathcal{N}\cap\mathbb{M}_+)\cong S^2$ | Celestial sphere of null directions |
| $SO^+(1,3)$ | Proper orthochronous Lorentz group; acts on $S^2=\mathbb{CP}^1$ by Möbius transformations |
| $PO_4(\mathbb{C})$ | Automorphism group of the complex quadric; larger than the Lorentz group |
| $O(2,4)\supset SO(4,2)$ | Conformal group of Minkowski space; identity component and its double cover |
| $SU(2,2)\cong Spin(4,2)$ | Double cover of $SO(4,2)$; acts on the $(2,2)$ Hermitian space |
| $n$, $n_\infty$ | Distinguished null vectors of the conformal model, origin and point at infinity |
| Versor / Vahlen matrix | Transformation of the conformal model, the Möbius analogue |
| $S^1\times S^1$ | Real quadric of the split slice, signature $(2,2)$ |
| $SO^+(2,2)$ | Group of the split slice, acting on the two factors separately |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed., 2001).
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989).
- P. Anglès, *Conformal Groups in Geometry and Spin Structures* (Birkhäuser, 2008).
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, 1997).
