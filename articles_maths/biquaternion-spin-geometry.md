# __Biquaternion Spin Geometry__

## Introduction

The biquaternion algebra is a Clifford algebra in two separate senses, and the spin geometry of the algebra is the geometry the second of them carries. The algebra is the even Clifford algebra $\mathbb{B}\cong\mathrm{Cl}^+_{1,3}$ of Minkowski space (*The Clifford Structure of the Biquaternion Algebra*), and it also carries its own biquaternion norm, whose Clifford algebra $\mathrm{Cl}(\mathbb{B},N)$ has a spinor module and a chirality grading (*Biquaternion Norm and Invertibility*). This article reads the spinor module of the algebra, its two chiral halves, the Clifford multiplication that defines it, and the operator that the Clifford structure puts on it.

The article is a slot article: it states the geometry the Clifford structure defines and cites the articles that construct it. The module itself is realised in the matrix model in *Biquaternion 2×2 Matrix Element Representation*, the Clifford multiplication being stated here; the analytic theory of the operator is *Fueter Theory for Biquaternions* and *Biquaternion Regular Functions* in Analysis; the rulings that the spinor lines trace are in *Biquaternion Topology*.

**Conventions.** The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0=1,e_1,e_2,e_3$ and central scalar imaginary $i$; a general element is $\tilde{Q}=\sum_{\mu=0}^{3} Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$. The criterion of *Biquaternion Norm and Invertibility* is used without proof: $N(\tilde{Q})\neq0$ if and only if $\tilde{Q}$ is invertible, and $N(\tilde{Q})=0$ with $\tilde{Q}\neq0$ if and only if $\tilde{Q}$ is a zero divisor.

---

## The Spinor Module and Its Two Chiral Halves

As a module over the complexified Lorentz algebra, the complexification of the Minkowski slice is the tensor product of the two Weyl spinor spaces of *Spin Representations and Clifford Modules with Inner Conjugation*,
$$
\mathbb{B}\cong\Delta^+\otimes\Delta^-,\qquad \dim_{\mathbb{C}}\Delta^\pm=2 .
$$
A biquaternion is therefore a **mixed spinor** with one unprimed and one primed index, $A_\alpha{}^{\dot\beta}$, and the null condition is exactly factorisability:
$$
A_\alpha{}^{\dot\beta}=\phi_\alpha\,\pi^{\dot\beta},\qquad \phi\in\Delta^+,\ \pi\in\Delta^- .
$$
Matching the matrix form $\Phi(\tilde{Q})=uv^{T}$ of *Biquaternion 2×2 Matrix Element Representation*, the column $u$ is the unprimed spinor $\phi$ and the row $v^{T}$ the primed spinor $\pi$. Hence fixing $\phi$ and varying $\pi$ traces $\ell_{[\phi]}\cong\mathbb{P}(\Delta^-)=\mathbb{P}^1$, while fixing $\pi$ and varying $\phi$ traces $m_{[\pi]}\cong\mathbb{P}(\Delta^+)=\mathbb{P}^1$. The two rulings are the **primed and unprimed spinor lines**, and they correspond to the two chiralities, since the complexified algebra splits into two simple summands, the two chirality eigenspaces. Which half-spin module is named $\Delta^+$ is a convention.

---

## Spinors as the Minimal Left Ideals

The minimal left ideals of $\mathbb{B}\cong M_2(\mathbb{C})$ are the two lines $\mathbb{B}\tilde\Pi_+$ and $\mathbb{B}\tilde\Pi_-$, where $\tilde\Pi_\pm=\tfrac12(e_0\pm i\hat{\mathbf{u}})$ are a complete pair of orthogonal idempotents (*Biquaternion Idempotents and Projections*, *Biquaternion Ideals and Peirce Decomposition*). Each is a copy of $\mathbb{C}^2$ as a left $\mathbb{B}$-module, and the algebra is their direct sum,
$$
\mathbb{B}=\mathbb{B}\tilde\Pi_+\oplus\mathbb{B}\tilde\Pi_-,
$$
so that the module of the spin representation is realised inside the algebra as a minimal left ideal. The two ideals themselves are not the chiral halves: each of them complexifies to the sum $S_+\oplus S_-$ of the two chiral spaces. The chirality belongs to the algebra, $\mathbb{B}\cong\Delta^+\otimes\Delta^-$, and the two families of null planes of the quadric are the projectivisations of the two chiral spaces $\Delta^\pm$. The construction of the module is *Biquaternion 2×2 Matrix Element Representation*, §*The Simple Module*, and *Biquaternion Ideals and Peirce Decomposition*; only the identification with the ideals is used here.

## The Spin Representation and Its Dimension

The spin representation of the biquaternion algebra is the natural representation of $M_2(\mathbb{C})$ on $\mathbb{C}^2$, of complex dimension $2$ and real dimension $4$. Its two chiral halves $\Delta^\pm$ are each of complex dimension $2$; the algebra acts on $\Delta^+$ from one side and on $\Delta^-$ from the other, and a general biquaternion is the mixed tensor $A_\alpha{}^{\dot\beta}\in\Delta^+\otimes\Delta^-$. The representation is irreducible as a module over the full algebra, since $\mathbb{B}$ is simple, and it splits into the two chiral summands only after complexification, $S\otimes_{\mathbb{R}}\mathbb{C}=S_+\oplus S_-$, the two halves being the two simple modules of the complexified Clifford algebra.

**Clifford multiplication.** The module carries the **Clifford multiplication** of $\mathrm{Cl}_{3,0}$, in which the generators act by the Pauli matrices,
$$
c(\gamma_k)=\sigma_k\quad(k=1,2,3),\qquad c(\gamma_1\gamma_2)=c(\gamma_1)c(\gamma_2)=\sigma_1\sigma_2=i\sigma_3,
$$
in the matrix model $\mathbb{B}\cong M_2(\mathbb{C})$; the images satisfy $c(\gamma_k)^2=I$ and $c(\gamma_k)c(\gamma_l)+c(\gamma_l)c(\gamma_k)=2\delta_{kl}I$, as generators of $\mathrm{Cl}_{3,0}$ of square $+1$ must, and $c$ extends to the whole Clifford algebra by the universal property.

**Theorem (the volume element acts as a scalar).** The volume element $\omega=\gamma_1\gamma_2\gamma_3$ acts on $S$ by the scalar $i$,
$$
c(\omega)=c(\gamma_1)c(\gamma_2)c(\gamma_3)=\sigma_1\sigma_2\sigma_3=iI,
$$
agreement of the two computations being $\omega\mapsto(ie_1)(ie_2)(ie_3)=i^3e_1e_2e_3=(-i)(-e_0)=i$. Consequently $S$ carries **no chirality splitting**: every vector of $S$ is an eigenvector of $c(\omega)$ with the one eigenvalue $i$, and the volume element does not grade the module.

## Chirality, Reality and the Two Halves

Chirality appears on complexification. On the complexified module $S\otimes_{\mathbb{R}}\mathbb{C}=S\oplus\overline{S}$ the operator $c(\omega)$ has the two eigenvalues $\pm i$, and its eigenspaces are the two **chiral halves**,
$$
S_+=\Delta^+,\qquad S_-=\Delta^-,\qquad S\otimes_{\mathbb{R}}\mathbb{C}=S_+\oplus S_-,
$$
the two Weyl spinor spaces: as representations of $SL(2,\mathbb{C})$ they are conjugate to one another and inequivalent. The real module $S$, of real dimension four, carries no splitting, because the eigenvalue $i$ is not real and the division into halves requires the complex scalars. This is the module-theoretic form of the statement that $\mathrm{Cl}_{3,0}$ has complex type: the chirality operator exists, but its eigenvalues are not real, so it does not cut the real module. The reality type of the module is therefore **complex**, its commutant is $\mathbb{C}$ by Schur's lemma, and there is **no Majorana spinor**: a Majorana spinor would be the fixed space of a real structure on $S$, and the complex type means no such structure exists (*Real Spinors and Reality Conditions with Inner Conjugation*).

**Remark (the two faces of chirality).** The same two Weyl spaces appear twice, and the two appearances must not be confused. As the tensor factors of the even Clifford algebra, $\mathbb{B}\cong\Delta^+\otimes\Delta^-$, they describe a biquaternion as a mixed spinor (§*The Spinor Module and Its Two Chiral Halves*); as the summands of the complexified module, $S\otimes_{\mathbb{R}}\mathbb{C}=\Delta^+\oplus\Delta^-$, they describe the Dirac spinor of complex dimension four. The tensor splitting is a statement about the algebra, the direct splitting a statement about its module, and both express the same chirality.

**Remark (the spin group acts, the Lorentz group does not).** The module carries the defining action of $SL(2,\mathbb{C})=\mathbb{B}^\times_1$ by Clifford multiplication, which is the spin representation of *Biquaternion Rotations and Lorentz Transformations*, §*The Group of Units and Its Representations*. The Lorentz group $SO^+(1,3)$ is the quotient by $\{\pm e_0\}$ and acts on the module only up to sign: it acts on the algebra by automorphisms, but it does not act on the module by algebra automorphisms, which is the standard statement that the Lorentz group itself has no two-dimensional spin representation.

## The Dirac Operator

The Clifford structure puts a first-order operator on the spinor module: the Dirac operator, the composition of the covariant derivative with the Clifford multiplication by the basis vectors. On the flat algebra it is the constant-coefficient operator
$$
D=\sum_{\mu=0}^{3} e_\mu\,\partial_\mu ,
$$
whose square is the d'Alembertian, $D^2=\Box$, and whose kernel is the space of regular functions of the algebra. The operator is a geometric object: it is defined by the Clifford multiplication alone, it is invariant under the motions the form defines, and it is the operator the spin structure exists to carry. Its properties as an operator — the kernel and its integral representation, the Cauchy integral, the decomposition of the space of functions — are the subject of *Fueter Theory for Biquaternions* and *Biquaternion Regular Functions* in Analysis, and the general theory is *Spin Geometry* and *The Dirac Operator* of Part IV; it is cited here and not restated.

## Against the General Spin Geometry of Part IV

The two Clifford structures of the algebra give two different spinor modules, and they must not be confused. The first attaches the spinor module to Minkowski space, using $\mathbb{B}\cong\mathrm{Cl}^+_{1,3}$: the module is the pair of Weyl spinors of the Lorentz group, and the geometry is the spin geometry of Minkowski space. The second attaches a module to the algebra itself as a quadratic space, using $\mathrm{Cl}(\mathbb{B},N)\cong\mathrm{Cl}_4(\mathbb{C})$, whose even part has the two chiral summands. Both modules are two-dimensional over $\mathbb{C}$ and both carry a Dirac operator, and the algebra is the bridge between them: it is the even Clifford algebra of one quadratic space and a quadratic space in its own right. The general construction, with the spin group, the Clifford multiplication and the Dirac operator on a manifold, is that of *Spin Geometry* and *The Dirac Operator* of Part IV, and the relation to the classification of the Clifford algebras is *The Clifford Structure of the Biquaternion Algebra*.

## Summary

The spin geometry of the biquaternion algebra rests on the identification of the algebra with an even Clifford algebra. The spinor module is the natural module of $M_2(\mathbb{C})$, of complex dimension $2$; it carries the Clifford multiplication $c(\gamma_k)=\sigma_k$, $c(\omega)=iI$, so the volume element acts as a scalar and does not grade the module; the chiral halves appear only on complexification, where they are the $\pm i$ eigenspaces of $c(\omega)$, and the reality type is complex, so there is no Majorana spinor. Its two chiral halves $\Delta^\pm$ are the two simple summands of the even part, and a biquaternion is the mixed spinor $A_\alpha{}^{\dot\beta}\in\Delta^+\otimes\Delta^-$. The null condition on a mixed spinor is factorisability, $A_\alpha{}^{\dot\beta}=\phi_\alpha\pi^{\dot\beta}$, and the two rulings of the null quadric — the primed and unprimed spinor lines — are the families traced by fixing one factor.

The module is realised inside the algebra as a minimal left ideal, the algebra being the direct sum $\mathbb{B}\tilde\Pi_+\oplus\mathbb{B}\tilde\Pi_-$ of the two ideals cut out by a complete pair of orthogonal idempotents; the two ideals are isomorphic, and each of them complexifies to $S_+\oplus S_-$, so neither is itself a chiral half. The Dirac operator is the constant-coefficient operator $D=\sum_\mu e_\mu\partial_\mu$ with $D^2=\Box$, defined by the Clifford multiplication alone and invariant under the motions of the form. Its analytic theory is in Analysis and the general theory in Part IV, both cited.

The algebra carries two Clifford structures, and with them two spinor modules: the module of Minkowski space, from $\mathbb{B}\cong\mathrm{Cl}^+_{1,3}$, and the module of the algebra as a quadratic space, from $\mathrm{Cl}(\mathbb{B},N)$. Both are two-dimensional over $\mathbb{C}$; the algebra is the even Clifford algebra of the one quadratic space and a quadratic space in its own right, and it is the bridge between the two.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Delta^\pm$ | The two Weyl spinor spaces; $\dim_{\mathbb{C}}\Delta^\pm=2$ |
| $c(\gamma_k)=\sigma_k$ | Clifford multiplication of the generators by the Pauli matrices |
| $c(\omega)=iI$ | The volume element acts as the scalar $i$; no chirality grading on the module |
| $S_\pm=\Delta^\pm$ | The two chiral halves, the $\pm i$ eigenspaces of $c(\omega)$ on $S\otimes_{\mathbb{R}}\mathbb{C}$ |
| complex; no Majorana | Reality type of the module; no real chirality splitting, no Majorana spinor |
| $SL(2,\mathbb{C})$ | Acts on the module by Clifford multiplication; $SO^+(1,3)$ only up to sign |
| $\mathbb{B}\cong\Delta^+\otimes\Delta^-$ | Biquaternion as a mixed spinor |
| $A_\alpha{}^{\dot\beta}=\phi_\alpha\pi^{\dot\beta}$ | Factorisation of a null biquaternion |
| $\ell_{[\phi]}\cong\mathbb{P}(\Delta^-)$, $m_{[\pi]}\cong\mathbb{P}(\Delta^+)$ | The two rulings, as the primed and unprimed spinor lines |
| $\tilde\Pi_\pm$ | Complete pair of orthogonal idempotents; $\mathbb{B}=\mathbb{B}\tilde\Pi_+\oplus\mathbb{B}\tilde\Pi_-$ |
| $\mathbb{B}\tilde\Pi_+\cong\mathbb{C}^2$ | Minimal left ideal; the module of the spin representation |
| $D=\sum_\mu e_\mu\partial_\mu$ | Dirac operator; $D^2=\Box$ |
| $\mathrm{Cl}(\mathbb{B},N)\cong\mathrm{Cl}_4(\mathbb{C})$ | Clifford algebra of the biquaternion norm; even part holds the two chiralities |
| $\mathbb{B}\cong\mathrm{Cl}^+_{1,3}$ | The algebra as the even Clifford algebra of Minkowski space |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed., 2001).
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989).
- F. Reese Harvey, *Spinors and Calibrations* (Academic Press, 1990).
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, 1997).
