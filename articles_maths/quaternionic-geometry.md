
# __Quaternionic Geometry__

## Introduction

A quaternionic structure on a manifold is a family of complex structures on its tangent spaces modelled on the imaginary quaternions. Where a complex structure singles out one operator $J$ with $J^2 = -\mathrm{id}$, a quaternionic structure provides a three-dimensional bundle $\mathcal{Q}$ of such operators, locally spanned by a triple $J_1, J_2, J_3$ satisfying the multiplication table of $e_1, e_2, e_3$ in the quaternion algebra $\mathbb{H}$. A manifold with such a structure has real dimension divisible by four, and the geometry is the geometry of the quaternionic general linear group $GL(n,\mathbb{H})$ and its compact unitary subgroup $Sp(n)$.

The subject has two levels, and the distinction between them is the organising principle of this article. An **almost quaternionic structure** is the pointwise datum, a rank-three subbundle $\mathcal{Q} \subseteq \mathrm{End}(TM)$ with the quaternionic relations. A **quaternionic structure** is an almost quaternionic structure that admits a torsion-free connection preserving it — the **Obata connection** — and Obata's theorem says that such a connection is unique when it exists. The integrability theory is therefore different in character from the complex case: there is no Nijenhuis tensor for the rank-three bundle, and integrability is expressed by the existence of a canonical connection rather than by the vanishing of a tensor.

Above the quaternionic level sit the metric conditions. A **quaternionic Kähler manifold** is a Riemannian manifold whose Levi-Civita connection preserves the quaternionic structure — equivalently, whose holonomy group lies in $Sp(n)\cdot Sp(1)$ — and such a manifold is automatically Einstein in dimension at least eight. The **hypercomplex** and **hyperkähler** conditions, in which the three complex structures are themselves integrable or Kähler, are the subject, and the quaternionic Kähler manifolds with vanishing scalar curvature are exactly the hyperkähler ones.

**The boundaries of the article.** The quaternion algebra $\mathbb{H}$, its basis $e_0=1,e_1,e_2,e_3$, the conjugations and the norm form are those andin Part I, and the quaternionic inner products and their Hermitian and anti-Hermitian subspaces those of the Part I quaternionic companions; nothing of the algebra is re-derived here. The Riemannian metric, the Levi-Civita connection, the holonomy group and the Ricci tensor are those of the companion article *Riemannian Geometry*; the pseudo-Riemannian and Lorentzian variants are those of *Pseudo-Riemannian and Lorentzian Geometry*. The complex and Hermitian structures, the fundamental form and the Chern connection are those of *Hermitian Geometry and Almost Complex Structures*, and the Kähler condition those of *Kähler Geometry*. The homogeneous spaces $G/H$ and their isotropy representations are the Lie-theoretic input of *Lie Groups* and its companions, cited throughout. The hyperkähler and Calabi–Yau conditions are developed andbeing, and are introduced here only far enough to locate them. The existence of the Obata connection, the Einstein property and the twistor correspondence are proved by the elliptic and parabolic methods of the analysis of Part III, where the measure and the limit are available; the statements are given here and the proofs cited. The base field is $\mathbb{R}$ and no physics is invoked.

## Quaternionic Vector Spaces

Let $\mathbb{H}$ be the algebra of quaternions with basis $e_0 = 1, e_1, e_2, e_3$ and relations $e_1e_2 = e_3$, $e_2e_3 = e_1$, $e_3e_1 = e_2$, $e_ie_j = -e_je_i$ for $i \neq j$, $e_1^2=e_2^2=e_3^2=-e_0$; the algebra is the real division algebra of Part I'sand conjugation and the norm are its conjugation and norm form.

**Definition.** A **quaternionic vector space** is a left module over $\mathbb{H}$, that is, a real vector space $V$ with an action of $\mathbb{H}$ on the left. If $V \cong \mathbb{H}^n$ then $\dim_{\mathbb{R}} V = 4n$, and the group of $\mathbb{H}$-linear automorphisms is $GL(n,\mathbb{H})$.

**Definition.** A **quaternionic structure** on a real vector space $V$ is an $\mathbb{R}$-algebra homomorphism

$$
\rho : \mathbb{H} \longrightarrow \mathrm{End}(V), \qquad \rho(1) = \mathrm{id},
$$

equivalently a triple of endomorphisms $J_1 = \rho(e_1)$, $J_2 = \rho(e_2)$, $J_3 = \rho(e_3)$ with

$$
J_1^2 = J_2^2 = J_3^2 = -\mathrm{id}, \qquad J_1J_2 = J_3, \quad J_2J_3 = J_1, \quad J_3J_1 = J_2, \qquad J_iJ_j = -J_jJ_i \ (i\neq j).
$$

The last relation shows in particular that the $J_i$ pairwise anticommute.

**Proposition.** Let $V$ be a real vector space of dimension $4n$. Giving $V$ the structure of a left $\mathbb{H}$-module is equivalent to giving it a quaternionic structure, and the two structures have the same automorphism group $GL(n,\mathbb{H})$.

**Proof.** A left $\mathbb{H}$-module structure is an $\mathbb{R}$-algebra homomorphism $\rho : \mathbb{H}\to\mathrm{End}(V)$ whose value at $\lambda$ is the operator $v\mapsto\lambda v$; it satisfies $\rho(\lambda\mu) = \rho(\lambda)\rho(\mu)$ and $\rho(1)=\mathrm{id}$. Conversely such a homomorphism defines the left action $\lambda\cdot v = \rho(\lambda)v$, which is associative because $\rho$ is an algebra homomorphism. The $\mathbb{H}$-linear automorphisms are exactly the real automorphisms intertwining $\rho$, which is the centraliser of $\rho(\mathbb{H})$, and for $\rho$ the standard representation on $\mathbb{H}^n$ this centraliser is $GL(n,\mathbb{H})$. $\square$

**Example.** On $\mathbb{H}^n$ with the basis $e_0,e_1,e_2,e_3$ for each copy of $\mathbb{H}$, left multiplication by $e_1, e_2, e_3$ gives a quaternionic structure. In the real basis $(1, e_1, e_2, e_3)$ of $\mathbb{H}$, the three operators are the $4\times 4$ matrices

$$
J_1 = \begin{pmatrix} 0 & -1 & 0 & 0\\ 1 & 0 & 0 & 0\\ 0 & 0 & 0 & -1\\ 0 & 0 & 1 & 0 \end{pmatrix}, \quad
J_2 = \begin{pmatrix} 0 & 0 & -1 & 0\\ 0 & 0 & 0 & 1\\ 1 & 0 & 0 & 0\\ 0 & -1 & 0 & 0 \end{pmatrix}, \quad
J_3 = \begin{pmatrix} 0 & 0 & 0 & -1\\ 0 & 0 & -1 & 0\\ 0 & 1 & 0 & 0\\ 1 & 0 & 0 & 0 \end{pmatrix},
$$

as a direct computation with the multiplication table shows. They satisfy $J_1^2=J_2^2=J_3^2=-I_4$, $J_1J_2=J_3$, $J_2J_1=-J_3$ and $J_1J_2J_3 = -I_4$.

**Definition.** A **quaternionic Hermitian structure** on a left $\mathbb{H}$-module $V$ is a quaternion-valued form $h$ with

$$
h(\lambda v, \mu w) = \lambda\,h(v,w)\,\bar\mu \quad \text{for all } \lambda,\mu \in \mathbb{H}, \qquad \overline{h(w,v)} = h(v,w),
$$

positive definite in the sense that $h(v,v)$ is real and positive for $v \neq 0$; the group preserving it is the compact symplectic group $Sp(n)$, of dimension $n(2n+1)$. Equivalently, the real part $g = \mathrm{Re}\,h$ is a Riemannian metric with $g(J_iv,J_iw) = g(v,w)$ for $i=1,2,3$, and the three $J_i$ are then skew-adjoint.

**Remark.** The inclusion of groups is

$$
Sp(n) \subset SU(2n) \subset U(2n) \subset SO(4n),
$$

and its dimension count $n(2n+1) + 3 = \dim(Sp(n)\cdot Sp(1)) = \dim Sp(n) + \dim Sp(1)$ exhibits the product $Sp(n)\cdot Sp(1)$ as the group generated by the quaternionic unitary transformations and the unit quaternions $\mathbb{H}^*/\mathbb{R}^* = Sp(1) = S^3$. This product group is the structure group of a quaternionic Kähler manifold, and $Sp(n)$ alone is the structure group of a hyperkähler one; both are groups of Part I, and their Lie theory is that of *Lie Groups*.

## Almost Quaternionic and Quaternionic Structures

**Definition.** An **almost quaternionic structure** on a smooth manifold $M$ of dimension $4n$ is a rank-three subbundle

$$
\mathcal{Q} \subseteq \mathrm{End}(TM)
$$

such that every point has a neighbourhood with a local frame $J_1, J_2, J_3$ of $\mathcal{Q}$ satisfying the quaternionic relations $J_1^2=J_2^2=J_3^2=-\mathrm{id}$, $J_1J_2=J_3$, $J_2J_3=J_1$, $J_3J_1=J_2$. Equivalently, $\mathcal{Q}$ is a subbundle with the local model of the imaginary quaternions under the adjoint action of $Sp(1)$, so that the structure group of $TM$ reduces to

$$
GL(n,\mathbb{H})\cdot \mathbb{H}^* \quad \text{or, for a Riemannian structure, to } GL(n,\mathbb{H})\cdot Sp(1).
$$

A manifold with an almost quaternionic structure is an **almost quaternionic manifold**.

**Proposition.** Let $\mathcal{Q}$ be an almost quaternionic structure. Then every local section $J = a_1J_1+a_2J_2+a_3J_3$ of $\mathcal{Q}$ with $a_1^2+a_2^2+a_3^2=1$ satisfies $J^2 = -\mathrm{id}$, and the subbundle $\mathcal{Q}$ is preserved by the local action of $Sp(1)$ by conjugation. Conversely, a rank-three subbundle $\mathcal{Q}\subseteq\mathrm{End}(TM)$ whose unit sections all square to $-\mathrm{id}$ and which is closed under the Lie bracket of endomorphisms is almost quaternionic.

**Proof.** In a local quaternionic frame, a section of $\mathcal{Q}$ is $a_1J_1+a_2J_2+a_3J_3$ for functions $a_i$; its square is $(a_1^2+a_2^2+a_3^2)(-\mathrm{id})$ by the relations, and this is $-\mathrm{id}$ exactly when $\sum a_i^2=1$, a condition which can be imposed on any nowhere vanishing section by rescaling it pointwise. The conjugation statement is the action of the unit quaternions on the imaginary part; the converse follows from the same computation applied to a local frame. $\square$

**Example.** The flat model is $\mathbb{H}^n = \mathbb{R}^{4n}$ with the constant frame of the previous section; the subbundle $\mathcal{Q}$ is trivial, spanned by constant $J_1, J_2, J_3$, and is preserved by all of $GL(n,\mathbb{H})\cdot Sp(1)$.

**Definition.** An almost quaternionic structure is a **hypercomplex structure** if the bundle $\mathcal{Q}$ admits a global frame $J_1,J_2,J_3$ of **integrable** almost complex structures; a manifold with such a structure is a **hypercomplex manifold**. Equivalently, $\mathcal{Q}$ is trivial as a bundle and each complex structure in the trivialisation is a complex structure.

**Remark.** The distinction between an almost quaternionic structure and a hypercomplex one is the distinction between a bundle with structure group $GL(n,\mathbb{H})\cdot Sp(1)$ and one whose structure group reduces to $GL(n,\mathbb{H})$; the former has an $S^2$-family of almost complex structures through each point (a $\mathbb{CP}^1$ after the metric is chosen), the latter a distinguished triple. The hyperkähler case, in which the triple is simultaneously Kähler for one metric, is not covered here.

## The Obata Connection

For complex structures the integrability of $J$ is detected by the vanishing of the Nijenhuis tensor, as in *Hermitian Geometry and Almost Complex Structures*. For the rank-three bundle $\mathcal{Q}$ there is no single tensor whose vanishing is the integrability condition; the correct notion is the existence of a connection.

**Theorem (Obata).** Let $\mathcal{Q}$ be an almost quaternionic structure on a manifold of dimension $4n$ with $n\geq2$. There is at most one torsion-free connection $\nabla^{\mathrm{Ob}}$ on $M$ with

$$
\nabla^{\mathrm{Ob}}\mathcal{Q} \subseteq \mathcal{Q},
$$

that is, with $\nabla^{\mathrm{Ob}}_X J$ a local section of $\mathcal{Q}$ for every local section $J$ of $\mathcal{Q}$ and every vector field $X$. Such a connection exists if and only if the Nijenhuis-type tensor $\mathcal{N}$ of $\mathcal{Q}$, defined as the component of the Lie bracket of local sections of $\mathcal{Q}$ outside $\mathcal{Q}$, vanishes; when it exists it is called the **Obata connection**, or the **quaternionic connection**. In dimension $4$ the tensor $\mathcal{N}$ vanishes for every almost quaternionic structure, so every four-dimensional almost quaternionic structure is quaternionic.

**Proof sketch.** Uniqueness: if $\nabla$ and $\nabla'$ are two such connections, then $A = \nabla' - \nabla$ is a $(1,2)$-tensor field; the torsion-free conditions give $A(X,Y) = A(Y,X)$, and the condition of preserving $\mathcal{Q}$ restricts $A$ to take values in a bundle $E$ determined by $\mathcal{Q}$. In dimension $4n$ with $n\geq2$ the two conditions force $A=0$. Existence: one constructs $\nabla^{\mathrm{Ob}}$ from the Levi-Civita connection of any Riemannian metric by adding the correct multiple of the Nijenhuis-type tensor, exactly as the Chern connection is obtained from the Levi-Civita connection; the tensor $\mathcal{N}$ is precisely the obstruction, and it vanishes automatically when $\dim M = 4$ because the relevant representation space is zero there. $\square$

**Definition.** A **quaternionic manifold** is an almost quaternionic manifold whose Nijenhuis-type tensor vanishes, equivalently one carrying an Obata connection; an **almost quaternionic structure** that is quaternionic. A hypercomplex manifold is a quaternionic manifold whose bundle $\mathcal{Q}$ is trivial.

**Proposition.** Let $M$ be hypercomplex with global frame $J_1,J_2,J_3$. Then the Obata connection is the unique torsion-free connection with $\nabla^{\mathrm{Ob}}J_i = 0$ for $i=1,2,3$, and its holonomy group is contained in $GL(n,\mathbb{H})$.

**Proof.** If $\nabla J_i = 0$ for the three independent local sections, then $\nabla$ preserves $\mathcal{Q}$, so it is the Obata connection by the theorem. Conversely the Obata connection of a hypercomplex structure annihilates each $J_i$ because the subbundle is trivial and hence generated by parallel sections. A connection whose parallel transport commutes with the ℍ-action has holonomy in the centraliser $GL(n,\mathbb{H})$. $\square$

**Remark.** The Obata connection is not in general compatible with any Riemannian metric: it preserves the quaternionic structure and is torsion-free, but metric compatibility is an additional condition. When a metric $g$ with $\nabla^{\mathrm{Ob}} g = 0$ exists together with $\nabla^{\mathrm{Ob}}\mathcal{Q}\subseteq\mathcal{Q}$, the structure is hyperkähler, and the Obata connection is the Levi-Civita connection of $g$; this is developed. The absence of a canonical metric is the main structural difference between the quaternionic and the complex cases, where a Hermitian metric supplies the Chern connection.

## Quaternionic Kähler Manifolds

**Definition.** A Riemannian manifold $(M,g)$ of dimension $4n \geq 8$ is **quaternionic Kähler** if its holonomy group is contained in $Sp(n)\cdot Sp(1)$. Equivalently, there is an almost quaternionic structure $\mathcal{Q}$ on $M$ with

$$
\nabla \mathcal{Q} \subseteq \mathcal{Q},
$$

where $\nabla$ is the Levi-Civita connection of $g$; equivalently the local frame $J_1,J_2,J_3$ satisfies $\nabla J_i = \sum_j a_{ij}\otimes J_j$ for local $1$-forms $a_{ij}$.

**Theorem.** Every quaternionic Kähler manifold of dimension $4n \geq 8$ is Einstein: $\mathrm{Ric} = \lambda g$ for a constant $\lambda$. A quaternionic Kähler manifold with nonvanishing scalar curvature is locally irreducible as a Riemannian manifold, and its holonomy group equals $Sp(n)\cdot Sp(1)$; in the Ricci-flat case the holonomy reduces to $Sp(n)$ and the manifold is locally hyperkähler.

**Proof sketch.** The Ricci tensor of a quaternionic Kähler manifold is invariant under the holonomy group, hence a multiple of $g$ at each point; the Berger–Simons argument using the second Bianchi identity then makes the multiple constant. Irreducibility follows from the fact that $Sp(n)\cdot Sp(1)$ acts irreducibly on $\mathbb{R}^{4n}$ but with the commutator structure required for a locally reducible manifold excluded. $\square$

**Definition.** A quaternionic Kähler manifold is **positive** if $\lambda > 0$, **negative** if $\lambda < 0$, and **Ricci-flat** if $\lambda = 0$. The Ricci-flat case is exactly the hyperkähler case.

**Theorem (Wolf; the Alekseevskii conjecture).** The compact quaternionic Kähler symmetric spaces are exactly the **Wolf spaces**, the symmetric spaces $G/H$ with $G$ simple and $H$ of the form $Sp(n)\cdot Sp(1)$:

| $G/H$ | $\dim$ | $n$ |
|---|---|---|
| $\mathbb{HP}^n = Sp(n+1)/(Sp(n)\cdot Sp(1))$ | $4n$ | $n$ |
| $\mathrm{Gr}_2(\mathbb{C}^{n+2}) = SU(n+2)/S(U(n)\cdot U(2))$ | $4n$ | $n$ |
| $\mathrm{Gr}_4(\mathbb{R}^{n+4}) = SO(n+4)/(SO(n)\cdot SO(4))$ | $4n$ | $n$ |
| $G_2/SO(4)$ | $8$ | $2$ |
| $F_4/(Sp(3)\cdot Sp(1))$ | $28$ | $7$ |
| $E_6/(SU(6)\cdot Sp(1))$ | $40$ | $10$ |
| $E_7/(SO(12)\cdot Sp(1))$ | $64$ | $16$ |
| $E_8/(E_7\cdot Sp(1))$ | $112$ | $28$ |

**Proof sketch.** The holonomy principle and the theory of isotropy representations of symmetric spaces reduce the classification to the list of irreducible Riemannian symmetric spaces whose isotropy representation is quaternionic; the compact simple Lie algebras admit exactly the entries above, and the classification of the symmetric cases is Wolf's. The **Alekseevskii conjecture** asserts that every positive quaternionic Kähler manifold of dimension $4n\geq8$ is one of these symmetric spaces; it holds in the low-dimensional cases that have been settled, and it remains open in general. $\square$

**Theorem (Alekseevskii, Cortés).** A homogeneous quaternionic Kähler manifold of negative scalar curvature is, up to a quotient by a discrete subgroup, a simply connected solvable Lie group $S$ with a left-invariant metric, where $S$ is a semidirect product of a Heisenberg-type group with $\mathbb{R}$; the symmetric case is the quaternionic hyperbolic space $\mathbb{H}H^n = Sp(n,1)/(Sp(n)\cdot Sp(1))$, and the metric on $S$ is the solvable extension of the quaternionic Heisenberg metric.

**Proof sketch.** The negative case is the theory of the quaternionic Kähler quotients and the classification of the homogeneous examples built from the solvable extensions of Heisenberg-type groups; the model is the quaternionic hyperbolic space of the noncompact symmetric space theory, and the rigidity of the homogeneous negative case is the Alekseevskii–Cortés classification. $\square$

**Remark.** In dimension four the holonomy inclusion is vacuous, because $Sp(1)\cdot Sp(1) = SO(4)$. The geometric content of the quaternionic Kähler condition must then be stated separately: a four-dimensional quaternionic Kähler manifold is by definition an oriented Riemannian four-manifold whose metric is Einstein and whose Weyl curvature is self-dual. The round $S^4 = \mathbb{HP}^1$ and the complex projective plane $\mathbb{CP}^2$ with the Fubini–Study metric are the standard compact examples, and the classification of the compact ones is the subject of the theory of self-dual Einstein four-manifolds. This special position of dimension four — where quaternionic Kähler and self-dual Einstein coincide — recurs throughout the theory.

## The Twistor Space

**Definition.** Let $(M,g,\mathcal{Q})$ be a quaternionic Kähler manifold. The **twistor space** is the total space of the unit sphere bundle of $\mathcal{Q}$ with respect to a fibrewise metric,

$$
Z(M) = \{ J \in \mathcal{Q}_x : x \in M,\ J^2 = -\mathrm{id}\},
$$

with bundle projection $\pi : Z(M) \to M$ whose fibre is $S^2 = \mathbb{CP}^1$.

**Theorem (Salamon).** Let $(M,g,\mathcal{Q})$ be a quaternionic Kähler manifold of dimension $4n$. Then $Z(M)$ carries a natural almost complex structure, integrable because $M$ is quaternionic Kähler, making $\pi : Z(M)\to M$ a holomorphic $\mathbb{CP}^1$-bundle. When the scalar curvature of $M$ is positive the twistor space is a Kähler manifold, indeed a Fano manifold; in the nonpositive case it is still a complex manifold, and the Kähler condition is not part of the correspondence.

**Proof sketch.** The almost complex structure on $Z(M)$ is built from the horizontal lift of the Levi-Civita connection and the complex structure of the fibre $\mathbb{CP}^1$; the integrability is equivalent to the vanishing of the Nijenhuis tensor, which is the quaternionic Kähler condition. The metric statement uses the existence of a $1$-parameter family of complex structures on the twistor space and the standard constructions of twistor theory. $\square$

**Remark.** The twistor correspondence converts questions about the quaternionic Kähler manifold $M$ into questions about complex submanifolds of the twistor space $Z(M)$; in dimension four it becomes the Penrose correspondence between the anti-self-dual Einstein equations and the holomorphic geometry of a three-dimensional complex manifold with a family of rational curves. Only the differential-geometric statement is recorded here. For a quaternionic Kähler manifold of dimension four with positive scalar curvature, the twistor space is a Fano threefold, and conversely a Fano threefold containing a suitable holomorphic $\mathbb{CP}^1$-family gives back a self-dual Einstein four-manifold. The complex geometry used is that of *Hermitian Geometry and Almost Complex Structures* and *Kähler Geometry*.

## Examples

**Example (flat quaternionic space and its quotients).** On $\mathbb{H}^n$ with the Euclidean metric and the constant triple $(J_1,J_2,J_3)$, the Levi-Civita connection preserves the triple, so the structure is quaternionic Kähler with $\lambda = 0$; it is the flat hyperkähler manifold. Quotients by lattices in $\mathbb{H}^n$ produce compact flat examples with trivial holonomy, and they are Kähler with respect to each of the three complex structures of the quaternionic family.

**Example (quaternionic projective space).** The projective space $\mathbb{HP}^n$ is the Wolf space $Sp(n+1)/(Sp(n)\cdot Sp(1))$, of dimension $4n$; it is quaternionic Kähler with $\lambda > 0$ and with $\mathbb{HP}^1 = S^4$ as the four-dimensional case. The quaternionic Kähler metric is the quotient of the bi-invariant metric on $Sp(n+1)$ and is the quaternionic analogue of the Fubini–Study metric of *Kähler Geometry*.

**Example (the exceptional Wolf spaces).** The compact symmetric spaces $G_2/SO(4)$, $F_4/(Sp(3)\cdot Sp(1))$, $E_6/(SU(6)\cdot Sp(1))$, $E_7/(SO(12)\cdot Sp(1))$ and $E_8/(E_7\cdot Sp(1))$, of dimensions $8, 28, 40, 64$ and $112$, are the exceptional entries of the Wolf classification, and each is quaternionic Kähler with positive scalar curvature. They are the only positive quaternionic Kähler symmetric spaces outside the classical families, and their dimensions are the fourfold multiples of the ranks $2, 7, 10, 16, 28$.

**Example (quaternionic hyperbolic space).** The noncompact symmetric space $\mathbb{H}H^n = Sp(n,1)/(Sp(n)\cdot Sp(1))$ is quaternionic Kähler with $\lambda<0$ and is the simply connected model of negative quaternionic curvature; it is the quaternionic analogue of the real and complex hyperbolic spaces and the noncompact dual of $\mathbb{HP}^n$, and it carries no Kähler metric. It is one of the noncompact symmetric spaces classified by the theory of *Lie Groups* and its companions.

**Example (four dimensions).** Every oriented Riemannian four-manifold is locally quaternionic, because $Sp(1)\cdot Sp(1)=SO(4)$; the quaternionic Kähler condition is Einstein plus self-dual Weyl. Besides $S^4$ and $\mathbb{CP}^2$ and the quotients of $\mathbb{H}H^1$, the theory includes the Page metric and the LeBrun and Pedersen metrics, which are complete non-symmetric examples of positive and negative scalar curvature.

**Example (Grassmannians).** The real Grassmannian $\mathrm{Gr}_4(\mathbb{R}^{n+4})$ and the complex Grassmannian $\mathrm{Gr}_2(\mathbb{C}^{n+2})$ are Wolf spaces, of dimension $4n$ each; the first is the quaternionic structure of real four-planes in a real vector space, the second the structure induced by the complex two-planes in $\mathbb{C}^{n+2}$. Both carry the symmetric metrics by which they appear in the Wolf table.

## The Doorway to Hyperkähler Geometry

**Definition.** A **hyperkähler manifold** is a Riemannian manifold $(M,g)$ with a hypercomplex structure $J_1,J_2,J_3$ for which each $J_i$ is a Kähler structure: $\nabla J_i = 0$ for the Levi-Civita connection of $g$ for $i=1,2,3$, where $\Omega_i(X,Y) = g(J_iX,Y)$ are the three Kähler forms.

**Theorem.** The following are equivalent for a Riemannian manifold $(M,g)$ of dimension $4n$:

**(a)** $(M,g)$ is hyperkähler;

**(b)** the holonomy group of $g$ is contained in $Sp(n)$;

**(c)** $M$ carries three complex structures $J_1,J_2,J_3$ with the quaternionic relations whose Kähler forms are the three closed $2$-forms of the structure;

**(d)** $(M,g)$ is quaternionic Kähler with vanishing scalar curvature.

**Proof sketch.** (a)$\Leftrightarrow$(b): the three parallel complex structures are the reduction of the holonomy group to their common centraliser $Sp(n)$. (a)$\Leftrightarrow$(c) is the definition together with the fact that a hypercomplex structure with a compatible Kähler metric has closed fundamental forms. (b)$\Leftrightarrow$(d): the holonomy $Sp(n)$ sits inside $Sp(n)\cdot Sp(1)$ with vanishing $Sp(1)$-part; that part is exactly the scalar curvature and the Einstein constant, so the vanishing of the scalar curvature is the reduction. $\square$

**Corollary.** A hyperkähler manifold is Ricci-flat, hence a Calabi–Yau manifold in the sense, beside being quaternionic Kähler. In complex dimension two a hyperkähler manifold is a complex surface with a Ricci-flat Kähler metric, and the compact examples are the $K3$ surfaces and the four-torus.

**Remark.** The hyperkähler manifolds are the quaternionic Kähler manifolds whose structure group reduces from $Sp(n)\cdot Sp(1)$ to $Sp(n)$: the scalar curvature is the obstruction. The metric is then unique in its Kähler class by Yau's theorem. The detailed theory — the twistor space as a complex manifold of a different kind, the hyperkähler quotient, the relation to the Bogomolov decomposition — is not treated here, and neither is the full Calabi–Yau theory.

## Summary

A quaternionic structure on a real vector space is an embedding of the quaternion algebra in its endomorphism algebra, equivalently a triple $J_1,J_2,J_3$ of complex structures with $J_1J_2=J_3$ and its cyclic variants; a quaternionic vector space is a left $\mathbb{H}$-module, and the automorphism group of the standard one is $GL(n,\mathbb{H})$. On a manifold the pointwise version is an almost quaternionic structure, a rank-three subbundle $\mathcal{Q}\subseteq\mathrm{End}(TM)$ locally spanned by a quaternionic triple, with the structure group reducing to $GL(n,\mathbb{H})\cdot Sp(1)$. It is quaternionic — integrable — when it carries a torsion-free connection preserving it, the Obata connection, which is unique when it exists in dimension at least eight; in particular there is no torsion-free connection preserving a non-integrable almost quaternionic structure, and every almost quaternionic structure in dimension four is integrable.

A quaternionic Kähler manifold is a Riemannian manifold with holonomy in $Sp(n)\cdot Sp(1)$, equivalently with a Levi-Civita-parallel quaternionic structure; such a manifold is Einstein in dimension at least eight and irreducible unless hyperkähler. The positive case is the Wolf classification, the eight families of quaternionic symmetric spaces listed above, of which the quaternionic projective spaces and the two classical Grassmannians are the familiar ones; the negative case is modelled on quaternionic hyperbolic space, the homogeneous examples being the solvable extensions of the Heisenberg-type groups. In dimension four the holonomy condition degenerates, and quaternionic Kähler means self-dual Einstein.

The twistor space $Z(M)$, an $S^2$-bundle of almost complex structures over a quaternionic Kähler manifold, carries a natural integrable complex structure — Kähler when the scalar curvature is positive — and converts the quaternionic geometry of $M$ into the complex geometry of $Z(M)$. Hypercomplex manifolds are those with a global integrable triple, and hyperkähler manifolds are the Ricci-flat quaternionic Kähler ones, equivalently those with holonomy in $Sp(n)$; they are the doorway .

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | The quaternions, with basis $e_0=1,e_1,e_2,e_3$ |
| $G$ | A simple Lie group (this article only in the Wolf list) |
| $\mathcal{Q}$ | The rank-three subbundle of $\mathrm{End}(TM)$ defining an almost quaternionic structure |
| $J_1, J_2, J_3$ | Local quaternionic frame: $J_i^2=-\mathrm{id}$, $J_1J_2=J_3$, $J_2J_3=J_1$, $J_3J_1=J_2$ (notation fixed by the shared block) |
| $g$ | Riemannian metric (from *Riemannian Geometry*); $\mathrm{Re}$ of the quaternionic Hermitian form $h$ |
| $h$ | Quaternionic Hermitian form, $h(\lambda v,\mu w)=\lambda h(v,w)\bar\mu$; $\mathrm{Re}\,h = g$ |
| $\nabla$ | Levi-Civita connection (from *Riemannian Geometry*) |
| $\nabla^{\mathrm{Ob}}$ | Obata connection: the torsion-free connection with $\nabla^{\mathrm{Ob}}\mathcal{Q}\subseteq\mathcal{Q}$, unique when it exists in dimension at least eight |
| $GL(n,\mathbb{H})$ | Quaternionic general linear group; structure group of a quaternionic manifold |
| $Sp(n)$ | Compact symplectic group, $\dim = n(2n+1)$; quaternionic unitary group |
| $Sp(n)\cdot Sp(1)$ | Structure group of a quaternionic Kähler manifold, $\dim = n(2n+1)+3$ |
| $\mathrm{Ric}=\lambda g$ | Einstein condition of a quaternionic Kähler manifold, $\dim\geq8$ |
| $\mathbb{HP}^n$ | Quaternionic projective space $Sp(n+1)/(Sp(n)\cdot Sp(1))$, $\dim=4n$ |
| $Z(M)$ | Twistor space, an $S^2$-bundle of almost complex structures; complex, Kähler for $\lambda>0$ |
| Wolf spaces | The positive quaternionic Kähler symmetric spaces $G/H$, listed in the table |
| Hypercomplex | $\mathcal{Q}$ trivial with integrable global frame $J_1,J_2,J_3$ |
| Hyperkähler | Hypercomplex with all $J_i$ Kähler for $g$; holonomy in $Sp(n)$, $\lambda=0$ |





## Further Reading

- Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of Differential Geometry, Volume II* (Interscience, 1969), for quaternionic structures, the Obata connection and the classification of the quaternionic symmetric spaces.
- Morio Obata, "Affine Connections on Manifolds with Almost Complex, Quaternion or Hermitian Structure", *Japanese Journal of Mathematics* 26 (1956), 43–77, for the existence and uniqueness of the canonical connection of an almost quaternionic structure.
- Dmitri V. Alekseevskii, "Compact Quaternion Spaces", *Functional Analysis and Its Applications* 2 (1968), 106–114, for the classification of the compact quaternionic Kähler symmetric spaces.
- Joseph A. Wolf, "Complex Homogeneous Contact Manifolds and Quaternionic Symmetric Spaces", *Journal of Mathematics and Mechanics* 14 (1965), 1033–1047, for the Wolf spaces and their dimensions.
- Simon Salamon, "Quaternionic Kähler Manifolds", *Inventiones Mathematicae* 67 (1982), 143–171, for the holonomy characterisation and the twistor space.
- Claude LeBrun and Simon Salamon (eds.), *Einstein Metrics and Yang–Mills Connections* (Longman, 1993), for the four-dimensional self-dual Einstein theory.
- Andrei S. Alekseevskii and Vincente Cortés, "Classification of Stationary Compact Homogeneous Quaternionic Kähler Manifolds", *Journal of Geometry and Physics* 76 (2004), 1–24, for the non-symmetric and negative cases.
- Dominic Joyce, *Compact Manifolds with Special Holonomy* (Oxford University Press, 2000), for the place of quaternionic Kähler geometry among the holonomy geometries and the twistor construction.
