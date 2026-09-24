
# __Conformal Geometry__

## Introduction

A Riemannian metric is a positive-definite quadratic form on each tangent space of a manifold, and the **conformal structure** it determines is the class of all metrics obtained from it by multiplication by positive smooth functions: two metrics $g$ and $g'$ are conformally equivalent when $g' = \Omega^2 g$ for a positive function $\Omega$, and a **conformal map** is a diffeomorphism whose pullback changes the metric by such a factor. Conformal geometry is the study of the invariants of a conformal class, and it begins with a linear-algebraic observation: the conformal class remembers the quadratic form only up to a positive scalar at each point, so it is the invariant of the form on which the theory of the quadratic-form articles earlier in this Part bears, and the conformal group — the group of conformal automorphisms of the round sphere — is a group of quadratic forms in disguise, namely a group of pseudo-orthogonal transformations of a space of two dimensions more. The purpose of the article is to develop the conformal structure, the conformal group and the conformal invariants of a form, using the Clifford algebra and the spinor formalism of this Part, and to keep the manifold theory itself to the companion articles *Riemannian Geometry* and *Smooth Manifolds and Differential Geometry*, earlier in this Part.

The central facts are these. The conformal group of the round sphere $S^n$ for $n \geq 3$ is the group $O(n+1,1)/\{\pm 1\}$ of the pseudo-orthogonal transformations of the form of signature $(n+1,1)$ of one dimension more, and its action on the sphere is the action of the **Möbius transformations**, the compositions of the rotations, the dilations, the translations and the inversions; by **Liouville's theorem** these are all the conformal maps of a domain of $\mathbb{R}^n$ for $n \geq 3$, and the dimension two is the exceptional case in which the conformal maps are the holomorphic maps of complex analysis. The sphere is the **conformal compactification** of $\mathbb{R}^n$, and it is realised as the projectivised null cone of the space $\mathbb{R}^{n+1,1}$; the conformal group is realised inside the Clifford algebra $\mathrm{Cl}_{n+1,1}$ as a Clifford or Pin group, and the conformal transformations themselves are realised by the two-by-two matrices over the Clifford algebra $\mathrm{Cl}_{0,n}$ of **Vahlen's theorem**. The invariants of the conformal class are carried by the **Weyl tensor** and by the **conformally invariant operators**, of which the conformal Laplacian and the Cauchy–Riemann operator in its conformal weight are the basic examples, and the twistor construction of Penrose is the reduction of the four-dimensional conformal geometry to the complex geometry of a three-dimensional complex manifold.

## Conformal Structures

### Conformal Equivalence and Conformal Maps

**Definition.** Let $M$ be a smooth manifold. Two Riemannian metrics $g$ and $g'$ on $M$ are **conformally equivalent** if $g' = \Omega^2 g$ for a positive smooth function $\Omega : M \to (0,\infty)$; a **conformal structure** on $M$ is a conformal equivalence class $\mathcal{C} = [g]$ of metrics. A diffeomorphism $f : (M,\mathcal{C}) \to (N,\mathcal{D})$ of conformal manifolds is a **conformal map** if $f^*g' = \Omega^2 g$ for representatives $g \in \mathcal{C}$, $g' \in \mathcal{D}$ and a positive function $\Omega$, and the **conformal group** $\operatorname{Conf}(M,\mathcal{C})$ is the group of conformal diffeomorphisms of $M$ onto itself.

**Proposition.** Conformal equivalence is an equivalence relation on the metrics of $M$; the conformal structure determines the same angles and the same ratio of lengths at a point as any representative metric, and the conformal structure is the same data as the metric up to the pointwise scale; the tangent space at each point with the conformal structure is a vector space with a quadratic form up to positive scalar, that is, an element of the **conformal class of the form**, and the linear algebra of this article is the linear algebra of a quadratic form up to scale.

**Proof.** The relation $g' = \Omega^2 g$ is symmetric, reflexive and transitive with the positive functions forming a group under multiplication, so it is an equivalence relation; the angle between two tangent vectors is $\arccos g(u,v)(g(u,u)g(v,v))^{-1/2}$ up to the sign of $g(u,v)$, which is unchanged by a positive scaling of $g$, and a ray of vectors has the same ratio of lengths under the scaling; conversely the conformal structure determines the angles and the ratios, which is the metric up to the pointwise scale. $\square$

**Example (the two-dimensional case).** On a surface the conformal structure is the same data as a complex structure and an orientation: the existence of the **isothermal coordinates** in which every metric of the class is $\Omega^2 (dx^2 + dy^2)$ is the classical theorem of the existence of conformal coordinates on a surface, and it identifies the conformal structures on an oriented surface with the complex structures, that is, with the Riemann surfaces. The two-dimensional case is the case in which the conformal maps are the holomorphic maps and the conformal group is infinite-dimensional; the present article treats the dimensions $n \geq 3$, in which the conformal group is a finite-dimensional Lie group, and the two-dimensional theory belongs to the complex analysis of Part III.

### The Weyl Tensor and Conformal Flatness

**Definition.** Let $(M,g)$ be a Riemannian manifold of dimension $n \geq 3$ with Riemann curvature $\operatorname{Riem}$, Ricci curvature $\operatorname{Ric}$ and scalar curvature $\operatorname{scal}$. The **Weyl tensor** is the $(0,4)$-tensor
$$
W = R - \frac{1}{n-2}\left(\operatorname{Ric} - \frac{\operatorname{scal}}{2(n-1)}g\right) \wedge g ,
$$
the trace-free part of the curvature with respect to the contractions, where the wedge is the Kulkarni–Nomizu product of the two symmetric $(0,2)$-tensors; equivalently the Weyl tensor is the trace-free part of the curvature tensor under the contractions of the metric, so that its traces with respect to the metric vanish.

**Theorem (Weyl–Schouten; conformal flatness).** A Riemannian manifold of dimension $n \geq 4$ is **conformally flat**, that is, every point has a neighbourhood conformal to the Euclidean space, if and only if the Weyl tensor vanishes identically; in dimension $3$ the obstruction is the **Cotton tensor**, the derivative of the traceless Ricci tensor, and in dimension $2$ the vanishing is automatic. The Weyl tensor is a conformal invariant: it is unchanged by the replacement of $g$ by $\Omega^2 g$, so it is an invariant of the conformal structure, and it is the obstruction to the local flatness of that structure.

The theorem is the local conformal flatness theorem, and its proof is the transformation formula for the curvature under a conformal change of the metric, computed from the Christoffel symbols of the two metrics; the computation and the result are in *Riemannian Geometry*, and the article records the statement as the source of the invariants of the conformal structure.

**Example.** The round sphere $S^n$ with the standard metric is conformally flat: the stereographic projection is a conformal diffeomorphism from the sphere minus a point to $\mathbb{R}^n$ with the Euclidean metric, so the sphere is locally conformal to the Euclidean space and its Weyl tensor vanishes; the Euclidean space, the sphere, the hyperbolic space and the cylinder are the standard conformally flat spaces, and they are conformally equivalent after the compactification of the next sections. A product of two spaces of constant curvature is conformally flat only in exceptional cases, and the Weyl tensor of a generic product does not vanish.

### Conformal Killing Fields and the Conformal Algebra

**Definition.** A vector field $X$ on a Riemannian manifold $(M,g)$ is a **conformal Killing field** if the Lie derivative of the metric is a multiple of the metric,
$$
\mathcal{L}_X g = \lambda\, g
$$
for a smooth function $\lambda$; the conformal Killing fields form a Lie algebra $\mathfrak{conf}(M,g)$ under the commutator of vector fields, the **conformal algebra** of the metric, and it is the Lie algebra of the conformal group, a Lie algebra of vector fields of the type of those of *Metric, Uniform and Complete Spaces* and of the theory of *Lie Groups*, earlier in this Part.

**Proposition.** The conformal algebra of a Riemannian manifold of dimension $n \geq 3$ is finite-dimensional and of dimension at most
$$
\dim \mathfrak{conf}(M,g) \leq \frac{(n+1)(n+2)}{2},
$$
with equality exactly when the metric is conformally flat (on a connected open set with the generic metric, and on the conformally flat manifolds); the conformal algebra of the Euclidean space $\mathbb{R}^n$ is the Lie algebra $\mathfrak{so}(n+1,1)$ of dimension $(n+1)(n+2)/2$, spanned by the constant vector fields (translations), the linear fields $x \mapsto \omega x$ with $\omega \in \mathfrak{so}(n)$ (rotations), the radial fields $x \mapsto c x$ (dilations) and the fields $x \mapsto |x|^2 a - 2\langle a,x\rangle x$ (the special conformal transformations).

**Proof sketch.** The conformal Killing equation is an overdetermined linear system of first-order partial differential equations for the components of $X$; differentiating it repeatedly expresses all the higher derivatives of $X$ at a point in terms of the values of $X$, $\lambda$, and their first derivatives together with the curvature, so the space of solutions is finite-dimensional and bounded by the number of the initial data, which is $(n+1)(n+2)/2$; in the flat case the listed fields span a space of that dimension and satisfy the equation. The identification of the flat conformal algebra with $\mathfrak{so}(n+1,1)$ is the linearisation of the conformal compactification of the next section, and the details are in the references. $\square$

## The Conformal Group and Liouville's Theorem

### The Möbius Transformations

**Definition.** The **inversion** in the unit sphere is the map $i : \mathbb{R}^n \setminus \{0\} \to \mathbb{R}^n \setminus \{0\}$, $i(x) = x/|x|^2$; a **Möbius transformation** of $\mathbb{R}^n$ is a composition of inversions, rotations, dilations and translations, and the **Möbius group** $\operatorname{Möb}(n)$ is the group of such transformations. The inversion is a conformal map with $\Omega(x) = |x|^{-2}$, and a composition of inversions is conformal; the Möbius transformations preserve the family of spheres and of hyperplanes of $\mathbb{R}^n$, carrying them to spheres or hyperplanes.

**Theorem (Liouville).** Let $n \geq 3$ and let $U \subseteq \mathbb{R}^n$ be a connected open set. Every conformal map $f : U \to \mathbb{R}^n$ of class $C^3$ is the restriction of a Möbius transformation of $\mathbb{R}^n$; consequently the conformal group of a domain of $\mathbb{R}^n$, for $n \geq 3$, is the restriction of the finite-dimensional group $\operatorname{Möb}(n)$.

The theorem is the rigidity of the conformal maps in dimension at least three, and it fails in dimension two, where the conformal maps are the holomorphic maps and the group is infinite-dimensional. The proof analyses the third derivatives of a conformal map and shows that the derivatives beyond the second are determined by the lower ones, the conformal condition being strong enough to force the Möbius form; the statement and the proof are in the references.

**Theorem.** The Möbius group of the sphere $S^n$ is the group $O(n+1,1)/\{\pm 1\}$ of the pseudo-orthogonal transformations of the form of signature $(n+1,1)$, and the Möbius group of $\mathbb{R}^n$ is the subgroup of the transformations of $S^n$ fixing the point at infinity; the conformal group of the sphere is a Lie group of dimension $(n+1)(n+2)/2$, containing the isometries $O(n+1)$ of the round sphere as a maximal compact subgroup.

**Proof sketch.** The action is constructed on the model of the next section: the sphere $S^n$ is the projectivised null cone of $\mathbb{R}^{n+1,1}$, the group $O(n+1,1)$ acts linearly on the cone and hence on its projectivisation, and the induced transformations are the Möbius transformations; the kernel of the action is the centre $\{\pm 1\}$, the dimension count is $\dim O(n+1,1) = (n+1)(n+2)/2$, and the stabiliser of an isotropic line is the conformal group of the point, isomorphic to the similarity group of $\mathbb{R}^n$. The details are in the references. $\square$

### The Conformal Compactification

**Definition.** The **conformal compactification** of the Euclidean space $\mathbb{R}^n$ is the sphere $S^n$, with the embedding $\mathbb{R}^n \hookrightarrow S^n$ given by the inverse of the stereographic projection; the **model of the conformal sphere** is the projectivised null cone of the space $\mathbb{R}^{n+1,1} = \mathbb{R}^{n+1} \oplus \mathbb{R}$ with the form $|u|^2 - v^2$. The null cone is
$$
\mathcal{N} = \{(u,v) \in \mathbb{R}^{n+1,1} \setminus \{0\} : |u|^2 = v^2\},
$$
a cone of null vectors on which the group $O(n+1,1)$ acts linearly, and the **Möbius sphere** is the space of its lines, the projectivised null cone. The round sphere $S^n \subseteq \mathbb{R}^{n+1}$ embeds by $y \mapsto (y,1)$, whose image is null because $|y|^2 = 1 = v^2$, and the Euclidean space embeds by
$$
z(x) = \left(x,\, \frac{|x|^2 - 1}{2},\, \frac{|x|^2 + 1}{2}\right) \in \mathbb{R}^n \oplus \mathbb{R} \oplus \mathbb{R} = \mathbb{R}^{n+1,1},
$$
which is null because $|x|^2 + \tfrac14(|x|^2-1)^2 - \tfrac14(|x|^2+1)^2 = |x|^2 - |x|^2 = 0$, and which is the inverse stereographic embedding after clearing the denominators; the point at infinity corresponds to the null line of $(0,1,1)$. The points of the Möbius sphere are the null lines, and the spheres and hyperplanes of $\mathbb{R}^n$ are the intersections of the null cone with the hyperplanes of $\mathbb{R}^{n+1,1}$, which is why the Möbius transformations preserve them.

**Proposition.** The conformal structure of the sphere is the conformal structure induced by the quadratic form of $\mathbb{R}^{n+1,1}$ through the null cone model: the Möbius group $O(n+1,1)/\{\pm 1\}$ acts by conformal transformations, the conformal Killing fields of the sphere are the linear fields of $\mathfrak{so}(n+1,1)$, and the conformal compactification is the maximal extension of the Euclidean space on which the conformal group acts by diffeomorphisms.

**Proof sketch.** A null vector $z \in \mathbb{R}^{n+1,1}$ represents a point of the sphere, and the tangent space of the sphere at that point is the quotient of the orthogonal complement $z^{\perp}$ by the line $\mathbb{R}z$, on which the form of $\mathbb{R}^{n+1,1}$ restricts to a positive-definite form up to scale; a linear transformation of $O(n+1,1)$ preserves the form and hence the conformal structure, and the map $x \mapsto z(x)$ of the display intertwines the Euclidean metric with the restriction of the form to the section, which gives the conformality. The identification of the conformal Killing fields with $\mathfrak{so}(n+1,1)$ is the derivative of the action. $\square$

## The Clifford Realisation and Vahlen Matrices

### The Conformal Group as a Clifford Group

**Remark.** The pseudo-orthogonal group of the form of signature $(n+1,1)$ is generated by its reflections, and by *The Clifford, Pin and Spin Groups* the Pin group $\operatorname{Pin}(n+1,1)$ is a double cover of $O(n+1,1)$ contained in the units of the Clifford algebra $\mathrm{Cl}_{n+1,1}$; the Möbius group of the sphere is therefore a quotient of a Clifford group,
$$
\operatorname{Conf}(S^n) = O(n+1,1)/\{\pm 1\} = \operatorname{Pin}(n+1,1)/\{\pm 1\} ,
$$
and the elements of the conformal group are realised as products of unit vectors of $\mathbb{R}^{n+1,1}$ acting by the twisted adjoint action on the null cone. This is the reason the conformal group belongs to the category of the Clifford algebras: it is the reflection group of the form of one dimension more, and its spin double cover is the spin group $\operatorname{Spin}(n+1,1)$ of the conformal form.

**Theorem (Vahlen).** For $n \geq 3$ the conformal group of $\mathbb{R}^n$ is isomorphic to the group of invertible two-by-two matrices
$$
\begin{pmatrix} a & b\\ c & d\end{pmatrix}, \qquad a, b, c, d \in \mathrm{Cl}_{0,n} \ \text{or the twisted algebra},
$$
satisfying the **Vahlen conditions** (the Hermitian conditions with respect to the conjugation of the Clifford algebra) modulo the nonzero scalars, in such a way that the matrix acts on $\mathbb{R}^n \cup \{\infty\}$ by the fractional transformation
$$
x \longmapsto (a x + b)(c x + d)^{-1},
$$
with the Clifford multiplication in the numerator and the inverse in the Clifford algebra; the matrices form a group isomorphic to the Möbius group, and the action is the conformal action on the sphere.

The theorem is due to Vahlen and was developed by Ahlfors; the conditions on the matrix are that the products $a\bar c$, $b\bar d$ and the antidiagonal products are the appropriate scalars, so that the matrix preserves the "Hermitian" structure of the Clifford algebra $\mathrm{Cl}_{0,n}$ in the sense of *Hermitian Forms and Involutions*. The matrix group is the $\operatorname{Pin}(n+1,1)$-group in the matrix coordinates, and the theorem is the concrete form of the identification of the conformal group with the Clifford group of the form of signature $(n+1,1)$; the statement and the proof are in the references.

**Example (the low dimensions).** For $n = 2$ the Clifford algebra $\mathrm{Cl}_{0,2}$ is the quaternion algebra $\mathbb{H}$ and the Vahlen matrices are the two-by-two matrices over $\mathbb{H}$ with the Vahlen conditions; the group they form is the double cover $SL(2,\mathbb{H})$ of the conformal group of the four-sphere, and its restriction gives the Möbius action on the conformal two-sphere. For $n = 3$ the Clifford algebra $\mathrm{Cl}_{0,3}$ is the doubled quaternion algebra $\mathbb{H}\oplus\mathbb{H}$, and the Vahlen matrices over it realise the conformal group of the three-sphere with the spin double cover $\operatorname{Spin}(4,1)$; the biquaternion algebra $\mathbb{B} \cong \mathrm{Cl}_{3,0}$ of *The Biquaternion Algebra as a Clifford Algebra* plays the corresponding role for the split signature, where the Vahlen construction is carried out over the Clifford algebra of the split form of the same dimension, and the spinor theory of the conformal group in those dimensions is the spinor theory of the corresponding Clifford algebra. The low-dimensional coincidences of *The Low-Dimensional Classification* are thus the concrete form of the conformal group in dimensions two and three.

## Conformal Invariants and Conformally Invariant Operators

### The Conformal Laplacian

**Definition.** Let $(M,g)$ be a Riemannian manifold of dimension $n \geq 3$. The **conformal Laplacian** (or **Yamabe operator**) is the second-order operator
$$
L_g = \Delta_g + \frac{n-2}{4(n-1)}\operatorname{scal}_g ,
$$
acting on functions, where $\Delta_g$ is the Laplacian of the metric and $\operatorname{scal}_g$ is the scalar curvature; the normalisation of the zero-order term is the one that makes the operator conformally invariant in the following sense.

**Theorem (conformal covariance).** Under the conformal change $g' = \Omega^2 g$ the conformal Laplacian transforms by
$$
L_{g'}(\Omega^{(n-2)/2}u) = \Omega^{(n+2)/2}\,L_g(u) , \qquad u \in C^\infty(M),
$$
so that the operator is conformally covariant with the **conformal weight** of the function $u \mapsto \Omega^{(n-2)/2}u$; the operator is invariant as an operator on the densities of the appropriate weight, and it is the unique second-order conformally invariant operator of its form on functions, the general classification belonging to the conformal invariant theory of the references.

**Proof sketch.** The transformation formula is computed from the transformation of the Laplacian and the scalar curvature under a conformal change: with $g' = \Omega^2 g$ one has $\operatorname{scal}_{g'} = \Omega^{-2}(\operatorname{scal}_g - 2(n-1)\Omega^{-1}\Delta_g\Omega - (n-1)(n-4)\Omega^{-2}|\nabla\Omega|^2)$, and the substitution $u \mapsto \Omega^{(n-2)/2}u$ cancels the extra terms against those produced by the Laplacian, leaving the factor $\Omega^{(n+2)/2}$. The computation is in the references. $\square$

**Corollary (the Yamabe problem; the statement).** The conformal Laplacian is the operator whose linear equation $L_g u = 0$ determines the **conformal factor** that makes a metric of constant scalar curvature in the conformal class: if $g' = u^{4/(n-2)}g$ and $L_g u = 0$, then $\operatorname{scal}_{g'} = 0$; more generally the constant-scalar-curvature equation is $L_g u = c\,u^{(n+2)/(n-2)}$ for the constant $c$, the **Yamabe equation**. The existence and the regularity of the solutions of the Yamabe equation are the analysis of the problem and belong to Part III, where the measure and the limit are available; the article records the operator and its conformal covariance, which is the form-theoretic content.

### The Cauchy–Riemann Operator and Conformal Covariance

**Theorem.** Let $(M,g)$ be a spin manifold of dimension $n$ with the spinor bundle $\mathcal{S}$ and the Cauchy–Riemann operator $D$, the operator classically named after Dirac, and let $g' = \Omega^2 g$ be a conformal metric with the corresponding spin structure and spinor bundle. Under the conformal change the Cauchy–Riemann operator is conformally covariant in the weight $(n-1)/2$:
$$
D_{g'}\bigl(\Omega^{-(n-1)/2}\sigma\bigr) = \Omega^{-(n+1)/2}\,D_g(\sigma) , \qquad \sigma \in \Gamma(\mathcal{S}),
$$
the identification of the spinor bundles being the natural one of the conformal spin structures. Consequently the **twistor operator** $\nabla_X \sigma - \frac1n X \cdot D\sigma$ is conformally invariant, its kernel consists of the **twistor spinors**, and the twistor spinors are the conformally invariant spinors of the theory.

**Proof sketch.** The conformal change of the Levi-Civita connection contributes a term involving the gradient of $\log\Omega$ and the Clifford multiplication, and the weight $-(n-1)/2$ on the spinors is exactly the one that cancels the contribution of the change of the connection against the change of the volume element in the trace defining the spinor connection; the computation is the spinor analogue of the conformal Laplacian computation, and it is in the references. $\square$

**Remark.** The conformal covariance of the two operators is the beginning of the conformal invariant theory: the conformal Laplacian and the Cauchy–Riemann operator are the conformally weighted operators acting on the scalar functions and on the spinor sections, and their invariance is why the conformal geometry is the natural setting for the conformally invariant operators of the first and second order. The general theory of the conformally invariant operators, the **GJMS operators** of Graham–Jenne–Mason–Sparling, classifies the operators of higher order with the conformal invariance; the classification is in the references, and the article records the two basic cases.

### The Twistor Construction

**Remark.** In dimension four the conformal geometry has a complex description. The **twistor space** of the conformal four-sphere is the complex projective space $\mathbb{CP}^3$, with the twistor fibration $\mathbb{CP}^3 \to S^4$ whose fibres are the projective lines, and the conformal structure of the four-sphere is encoded in the complex geometry of the twistor space; the twistor space of the conformal four-space is the complement of a line in $\mathbb{CP}^3$. The **Penrose correspondence** relates the conformally invariant equations of the four-dimensional geometry to the sheaf cohomology of the twistor space: the solutions of the twistor equation, the conformal Killing fields and the solutions of the conformally invariant field equations correspond to cohomology classes, and the twistor space is the projectivisation of the spinor bundle of the conformal structure in the sense. The Riemannian twistor theory of the compact anti-self-dual four-manifolds is the analogue of the construction, and the details are in the references.

## Summary

A **conformal structure** on a manifold is the class of metrics $g' = \Omega^2 g$ for positive functions $\Omega$; it remembers the quadratic form of the tangent space up to a positive scalar, so the linear algebra of the conformal structure is the linear algebra of a quadratic form up to scale. A **conformal map** is a diffeomorphism changing the metric by a positive factor, and the conformal maps of a domain of $\mathbb{R}^n$ for $n \geq 3$ are by **Liouville's theorem** the restrictions of the **Möbius transformations**, the compositions of rotations, dilations, translations and inversions; the **Möbius group** of the sphere is $\operatorname{Conf}(S^n) = O(n+1,1)/\{\pm 1\}$, of dimension $(n+1)(n+2)/2$, and the sphere is the **conformal compactification** of $\mathbb{R}^n$, realised as the projectivised null cone of the form of signature $(n+1,1)$, with the section $x \mapsto (x, (|x|^2-1)/2, (|x|^2+1)/2)$. The conformal group is the reflection group of the form of one dimension more: it is the quotient of the **Pin group** $\operatorname{Pin}(n+1,1)$ of the Clifford algebra $\mathrm{Cl}_{n+1,1}$, and by **Vahlen's theorem** it is the group of the two-by-two matrices over the Clifford algebra $\mathrm{Cl}_{0,n}$ satisfying the Vahlen conditions, acting by fractional transformations $x \mapsto (ax+b)(cx+d)^{-1}$. The local invariants of the conformal structure are carried by the **Weyl tensor**, whose vanishing is equivalent to the conformal flatness in dimension $n \geq 4$, and by the conformally invariant operators: the **conformal Laplacian** $L_g = \Delta_g + \frac{n-2}{4(n-1)}\operatorname{scal}_g$ transforms by $L_{\Omega^2g}(\Omega^{(n-2)/2}u) = \Omega^{(n+2)/2}L_g(u)$, and the **Cauchy–Riemann operator** of a spin manifold transforms by $D_{\Omega^2g}(\Omega^{-(n-1)/2}\sigma) = \Omega^{-(n+1)/2}D_g(\sigma)$, with the **twistor operator** as the conformally invariant first-order operator it defines. In dimension four the conformal geometry has the complex **twistor** description, with the twistor space $\mathbb{CP}^3$ of the conformal four-sphere and the Penrose correspondence.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $g$, $g' = \Omega^2 g$ | Metrics; $\Omega > 0$ a conformal factor |
| $\mathcal{C} = [g]$ | Conformal structure, the conformal class of $g$ |
| $\operatorname{Conf}(M,\mathcal{C})$ | Conformal group of a conformal manifold |
| $\operatorname{Conf}(S^n) = O(n+1,1)/\{\pm 1\}$ | Möbius group of the sphere, $n \geq 3$ |
| $\operatorname{Riem}$, $\operatorname{Ric}$, $\operatorname{scal}$ | Riemann, Ricci and scalar curvature of $g$ |
| $W$ | Weyl tensor; vanishing = conformal flatness for $n \geq 4$ |
| $\mathcal{L}_X g = \lambda g$ | Conformal Killing equation |
| $\mathfrak{conf}(M,g) \subseteq \mathfrak{so}(n+1,1)$ | Conformal algebra, dimension $\leq (n+1)(n+2)/2$ |
| $\mathbb{R}^{n+1,1}$ | Conformal model space, signature $(n+1,1)$ |
| $\mathcal{N}$ | Null cone; Möbius sphere = projectivised null cone |
| $\operatorname{Pin}(n+1,1)$, $\operatorname{Spin}(n+1,1)$ | Pin and Spin groups of the conformal form |
| $\mathrm{Cl}_{0,n}$ | Clifford algebra of the Vahlen matrices |
| $L_g = \Delta_g + \frac{n-2}{4(n-1)}\operatorname{scal}_g$ | Conformal Laplacian (Yamabe operator) |
| $D_{g'}(\Omega^{-(n-1)/2}\sigma) = \Omega^{-(n+1)/2}D_g\sigma$ | Conformal covariance of the Cauchy–Riemann operator |
| twistor operator | $\nabla_X\sigma - \frac1n X\cdot D\sigma$; kernel = twistor spinors |
| $\mathbb{CP}^3$ | Twistor space of the conformal four-sphere |



## Further Reading

- Manfredo P. do Carmo, *Riemannian Geometry* (Birkhäuser, 1992), for the Weyl tensor, the conformal change of the curvature and the conformal flatness theorem.
- Marcel Berger, *A Panoramic View of Riemannian Geometry* (Springer, 2003), for the conformal group, Liouville's theorem and the Yamabe problem.
- Lars V. Ahlfors, "Möbius Transformations in $\mathbb{R}^n$ Expressed through $2\times2$ Matrices of Clifford Numbers", *Complex Variables* 5 (1986), 215–224, for Vahlen's theorem.
- Jan Cnops, *An Introduction to Dirac Operators on Manifolds* (Birkhäuser, 2002), for the conformal covariance of the Cauchy–Riemann operator and the twistor operator.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, Volume 2 (Cambridge University Press, 1986), for the twistor construction and the Penrose correspondence.
- C. Robin Graham, Ralph Jenne, Lionel J. Mason and George A. J. Sparling, "Conformally Invariant Powers of the Laplacian, I: Existence", *Journal of the London Mathematical Society* 46 (1992), 557–565, for the GJMS operators and the classification of the conformally invariant operators.
- Michael Atiyah, Nigel Hitchin and Isadore Singer, "Self-Duality in Four-Dimensional Riemannian Geometry", *Proceedings of the Royal Society A* 362 (1978), 425–461, for the Riemannian twistor theory.
