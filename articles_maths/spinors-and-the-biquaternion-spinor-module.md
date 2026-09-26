
# __Spinors and the Biquaternion Spinor Module__

## Introduction

The spinor module of the biquaternion algebra is the vector space on which the double cover of the rotation group acts without passing through the rotation itself, and it is the reason the biquaternion algebra is the natural home of the rotation groups of the preceding article. As a module over $\mathbb{B}\cong M_2(\mathbb{C})$ it is the defining module $\mathbb{C}^2$; equivalently, it is a minimal left ideal $\mathbb{B}p$ of the algebra, and the choice of the minimal idempotent $p$ is the choice of a basis of the module. On this module the group $SL(2,\mathbb{C})=\mathrm{Spin}(1,3)$ acts by matrix multiplication, and it is this action — not the action of $SO^{+}(1,3)$ — that carries the spinors.

This article identifies the module, splits it into its two chiral halves, distinguishes the defining module from its dual and from its conjugate, and computes the invariant forms. The biquaternion algebra, its norm form and its matrix model are from *The Biquaternion Algebra as a Clifford Algebra*; the double cover $SL(2,\mathbb{C})\to SO^{+}(1,3)$ and the rotation groups are from *The Rotation and Reflection Groups in the Biquaternion Algebra*; and the general theory of Clifford modules, chirality and the spin representation is from *Spin Representations and Clifford Modules*. The module-theoretic treatment of $S$ — its freeness over $\mathbb{B}$, the bimodule and double-centralizer structure, and the invariant forms as abstract module data — belongs to *The Defining Module of the Biquaternion Algebra* and is cited rather than reproduced; what is established here is the spinor statement, namely the minimal left ideal, its decomposition $\Delta=V_{1/2}\oplus\overline{V_{1/2}}$ into chiral halves, and the action of $SL(2,\mathbb{C})=\mathrm{Spin}(1,3)$ on it. Only the computations special to $\mathbb{B}$ are performed here.

## The Spinor Module

**Theorem.** The algebra $\mathbb{B}\cong M_2(\mathbb{C})$ has, up to isomorphism, exactly one simple left module, of complex dimension two. It is realised as the minimal left ideal

$$
S=\mathbb{B}p, \qquad p=\tfrac12(e_0+ie_3),
$$

which in the matrix model is the column space $\mathbb{C}^2$.

**Proof.** A full matrix algebra $M_n(\mathbb{C})$ has a unique simple left module, the column space $\mathbb{C}^n$, of dimension $n$; for $n=2$ this is the statement. The explicit realisation by the minimal idempotent $p$ and the Peirce decomposition is in *The Biquaternion Algebra as a Clifford Algebra*, where $\Phi(p)=\operatorname{diag}(1,0)$ and $\mathbb{B}p$ is the first column. $\square$

**Definition.** The **biquaternion spinor module** is $S=\mathbb{B}p\cong\mathbb{C}^2$, and its elements are **spinors**. The **real spinor module** is $S$ regarded as a real vector space of dimension four by forgetting the complex structure.

**Remark.** All minimal left ideals of $\mathbb{B}$ are isomorphic to $S$, and the choice of $p$ among the minimal idempotents, which are parametrised by the projective line $\mathbb{CP}^1$, changes the identification of $S$ with a column of the matrix model but not the isomorphism class of the module. This is the module-theoretic form of the statement that spinors are defined up to a choice of basis, and it is the source of the freedom that in the applications appears as the choice of a spin structure.

## The Double Cover and the Spinor Action

The whole point of the spinor module is that the rotation group acts on it only through its double cover.

**Theorem.** The group $SL(2,\mathbb{C})=\{\tilde G\in\mathbb{B}:N(\tilde G)=1\}$ acts on $S=\mathbb{C}^2$ by left multiplication, and the representation is irreducible; the action on $S$ is faithful, since the simple algebra $\mathbb{B}$ acts faithfully on its simple module, so its kernel on $S$ is $\{e_0\}$ alone. The kernel of the induced action on the Hermitian subspace $\mathbb{M}_+$, $x\mapsto\tilde Gx\tilde G^{\dagger}$, is $\{\pm e_0\}$, and the quotient is the identity component $SO^{+}(1,3)$ acting on $\mathbb{M}_+$.

**Proof.** Left multiplication is a module action for the algebra $\mathbb{B}$, hence for any subgroup of its units; it is irreducible because $S$ is a simple module, and it is faithful because the annihilator of $S$ is a two-sided ideal of the simple algebra $\mathbb{B}\cong M_2(\mathbb{C})$, proper since $e_0$ acts as $\mathrm{id}_S$, hence zero. So an element of $SL(2,\mathbb{C})$ acting as the identity on $S$ is $e_0$ itself, and the central element $-e_0$ acts as $-\mathrm{id}_S$. The action on $\mathbb{M}_+$ is the associated action on the Hermitian forms on $S$; an element $\tilde G$ acts trivially there exactly when $\tilde Gx\tilde G^{\dagger}=x$ for every Hermitian $x$. Taking $x=e_0$ gives $\tilde G\tilde G^{\dagger}=e_0$, that is $\tilde G^{\dagger}=\tilde G^{-1}$, and the condition becomes $\tilde Gx=x\tilde G$; since the Hermitian matrices span $\mathbb{B}$ over $\mathbb{C}$, this makes $\tilde G$ a scalar $\lambda e_0$, and the norm condition $N(\lambda e_0)=\lambda^2=1$ leaves $\lambda=\pm1$. So the kernel on $\mathbb{M}_+$ is $\{\pm e_0\}$, the composite $SL(2,\mathbb{C})\to SO^{+}(1,3)$ is two-to-one, and the quotient acts on $\mathbb{M}_+$ as the identity component of the orthogonal group of the norm form. $\square$

**Corollary.** The spinor module does not carry an action of $SO^{+}(1,3)$: the two elements $\pm\tilde G$ of $SL(2,\mathbb{C})$ lie over the same rotation and act on $S$ by the distinct operators $\pm\Phi(\tilde G)$, so a rotation determines the spinor action only up to sign. It is the lift to $SL(2,\mathbb{C})$ that gives a genuine action. The two-to-one cover is thus the statement that spinors are sections of a bundle whose structure group is the double cover, and the module $S$ is the typical fibre.

## The Two Chiral Halves

The complexification of the algebra splits the spinor module into two inequivalent halves.

**Theorem.** The complexified Clifford algebra is $\mathbb{C}\mathrm{l}_3=\mathbb{C}\mathrm{l}_{3,0}\otimes_{\mathbb{R}}\mathbb{C}\cong M_2(\mathbb{C})\times M_2(\mathbb{C})$, and its two simple modules

$$
S_+=\mathbb{C}^2\otimes 1, \qquad S_-=1\otimes\mathbb{C}^2
$$

are the two **chiral halves**, the two Weyl spinor modules of the classical spinor literature. As representations of $SL(2,\mathbb{C})=\mathrm{Spin}(1,3)$ they are the two inequivalent complex two-dimensional representations, and $S_-\cong\overline{S_+}$ is the complex conjugate of $S_+$.

**Proof.** The complexification of an odd Clifford algebra is the product of two copies of the even complex Clifford algebra of the same dimension minus one, which is $M_2(\mathbb{C})$ for $n=3$; hence the two factors. Their simple modules are as displayed, and under the real form $SL(2,\mathbb{C})$ the two factors are exchanged by complex conjugation, so the two modules are conjugates of each other. They are inequivalent because the two factors of the algebra act differently: $S_+$ is annihilated by the second factor and $S_-$ by the first. $\square$

**Remark.** The two chiral halves are the algebraic remnant of chirality in odd dimension, where the volume element is central and no chirality operator with eigenvalues $\pm1$ exists on a single module. Chirality reappears after complexification, where the center of $\mathbb{C}\mathrm{l}_3$ has two idempotents and the center decomposes the module category into two pieces. The biquaternion algebra, being the real form, sees the two halves only through the complexification; its own simple module $S$ is a real form of $S_+\oplus S_-$ in the sense that $S\otimes_{\mathbb{R}}\mathbb{C}\cong S_+\oplus S_-$.

**Remark (the complex spinor module).** In the notation the two halves are the Weyl spinors $S_+=V_{1/2}=(\tfrac12,0)$ and $S_-=\overline{V_{1/2}}=(0,\tfrac12)$, and their direct sum is the complex spinor module
$$
\Delta=V_{1/2}\oplus\overline{V_{1/2}}=S_+\oplus S_-.
$$
The two notations agree: $\Delta$ is the complexification $S\otimes_{\mathbb{R}}\mathbb{C}$ of the real biquaternion spinor module, of complex dimension four and real dimension eight.

**Corollary.** The biquaternion spinor module of real dimension four complexifies to the direct sum of the two chiral halves of complex dimension two each. This is the precise sense in which the four-component biquaternion spinor decomposes into two two-component Weyl spinors over $\mathbb{C}$.

## The Dual and the Conjugate

The dual and the conjugate of $S$ are governed by two different forms, and distinguishing them is essential.

**Theorem.** Let $S=\mathbb{C}^2$ with the antisymmetric bilinear form

$$
\varepsilon(u,v)=u^{T}\varepsilon_{0}v, \qquad \varepsilon_{0}=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
$$

Then $\varepsilon$ is $SL(2,\mathbb{C})$-invariant, $\varepsilon(\tilde Gu,\tilde Gv)=\varepsilon(u,v)$ for all $\tilde G\in SL(2,\mathbb{C})$, and it induces an isomorphism of $SL(2,\mathbb{C})$-modules $S\to S^{*}$, $u\mapsto\varepsilon(u,\cdot)$.

**Proof.** For $\tilde G$ of determinant one, $\tilde G^{T}\varepsilon_{0}\tilde G=\det(\tilde G)\varepsilon_{0}=\varepsilon_{0}$, so $\varepsilon(\tilde Gu,\tilde Gv)=u^{T}\tilde G^{T}\varepsilon_{0}\tilde Gv=u^{T}\varepsilon_{0}v=\varepsilon(u,v)$. The induced map $S\to S^{*}$ is $\mathbb{C}$-linear, injective, and hence an isomorphism in dimension two; equivariance is the invariance just proved. $\square$

**Theorem.** There is no nonzero $SL(2,\mathbb{C})$-invariant Hermitian form on $S$. The positive definite Hermitian form $h(u,v)=u^{\dagger}v$ is invariant under $SU(2)\subset SL(2,\mathbb{C})$ but not under all of $SL(2,\mathbb{C})$.

**Proof.** An invariant Hermitian form is a Hermitian matrix $M$ with $\tilde G^{\dagger}M\tilde G=M$ for every $\tilde G\in SL(2,\mathbb{C})$. Differentiating the relation along $\tilde G=\exp(tX)$ at $t=0$ gives $X^{\dagger}M+MX=0$ for every $X$ in the Lie algebra $\mathfrak{sl}(2,\mathbb{C})$. For $X=\operatorname{diag}(1,-1)$ this forces $M$ to be off-diagonal; the nilpotent $X=\begin{pmatrix}0&1\\0&0\end{pmatrix}$ then gives $m_{12}+m_{21}=0$, while $X=i\begin{pmatrix}0&1\\0&0\end{pmatrix}$ gives $m_{12}=m_{21}$, so both off-diagonal entries vanish and $M=0$. The positive definite form $h(u,v)=u^{\dagger}v$ is preserved by $U(2)$, whose determinant-one part is $SU(2)\cong Sp(1)$, and not by all of $SL(2,\mathbb{C})$, the orbit of a unit vector under $\operatorname{diag}(t,t^{-1})$ being unbounded. $\square$

**Corollary (dual versus conjugate).** The dual module $S^{*}$ is identified with $S$ by the symplectic form $\varepsilon$, so $S$ is self-dual. The conjugate module $\overline{S}$ is the other chiral half, and it is not isomorphic to $S$ as an $SL(2,\mathbb{C})$-module. The Hermitian form identifies $S^{*}$ with $\overline{S}$ only antilinearly, by $u\mapsto h(u,\cdot)$, and this identification is $SU(2)$-equivariant but not $SL(2,\mathbb{C})$-equivariant.

**Remark.** It is tempting to identify the dual with the conjugate because both involve a form on spinors, and the two forms available — the antisymmetric bilinear form and the Hermitian form — differ in exactly the way that matters. The bilinear form is $SL(2,\mathbb{C})$-invariant and gives self-duality; the Hermitian form is only $SU(2)$-invariant and gives the antilinear identification with the conjugate. The first is the spinor contraction of the next section; the second is the positive definite structure used when one wishes to form a Hilbert space of spinors.

## The Spinor Contraction

**Definition.** The **spinor contraction** is the bilinear pairing

$$
\varepsilon\colon S\times S\longrightarrow\mathbb{C}, \qquad \varepsilon(u,v)=u^{T}\varepsilon_{0}v.
$$

It is antisymmetric, non-degenerate, and $SL(2,\mathbb{C})$-invariant.

**Theorem.** The spinor contraction is the unique $SL(2,\mathbb{C})$-invariant bilinear form on $S$ up to scale, and it identifies the module $S$ with its dual. Under the action of $SL(2,\mathbb{C})$ the spinor $u$ transforms by $u\mapsto\tilde Gu$ and the contraction is invariant:

$$
\varepsilon(\tilde Gu,\tilde Gv)=\varepsilon(u,v).
$$

**Proof.** The space of $SL(2,\mathbb{C})$-invariant bilinear forms on $S$ is the space of homomorphisms $S\to S^{*}$ commuting with the action, which by Schur's lemma and the self-duality is one-dimensional; $\varepsilon$ is a nonzero element of it. The invariance was proved above. $\square$

**Definition.** The **Hermitian spinor norm** of $u\in S$ is

$$
\|u\|_{h}^{2}=h(u,u)=u^{\dagger}u=\sum_{j}|u_j|^{2}\geq0,
$$

the positive definite norm associated with the Hermitian form. There is no positive definite norm associated with the spinor contraction $\varepsilon$, because $\varepsilon$ is alternating.

**Remark.** The antisymmetric contraction has no positivity: $\varepsilon(u,u)=0$ for every $u$, as for any alternating form. The positive definite norm is the Hermitian one, and it is defined only up to the choice of an $SU(2)$ inside $SL(2,\mathbb{C})$. In the applications one uses the antisymmetric contraction to pair spinors into scalars and the Hermitian norm to measure them, and the fact that the two are different structures on the same module is the algebraic content of the distinction between the symplectic and the Riemannian aspects of spin geometry.

## The Real Spinor Module

**Theorem.** The real spinor module of $\mathrm{Cl}_{3,0}$ is $S$ regarded as a real vector space of dimension four, and it is irreducible over $\mathbb{R}$; its commutant is $\mathbb{C}$, in agreement with the complex type of the three-dimensional classification.

**Proof.** The algebra $\mathrm{Cl}_{3,0}\cong M_2(\mathbb{C})$ is a real algebra whose center is $\mathbb{C}$; its irreducible real module is $\mathbb{C}^2$ of real dimension four, and by Schur's lemma its commutant is the center $\mathbb{C}$. This is the $d\equiv3$ entry of the reality table of *Real Spinors and Reality Conditions*, the complex type. $\square$

**Corollary.** There are no Majorana spinors in the biquaternion algebra: a Majorana spinor would be a fixed point of a real structure, and the type being complex means no such structure exists. The four real components of a biquaternion spinor are not the components of a real spinor but the two complex components of a complex spinor, and the conjugation that pairs them is the antilinear identification of $S$ with its conjugate, not an involution on $S$.

**Remark.** The passage to a real spinor requires a change of signature: for the forms of signature difference $d\equiv0,1,2\bmod8$ a real structure exists and Majorana spinors appear. In the biquaternion setting this is achieved by using the split forms, in which the relevant module carries a real structure; the four-dimensional algebra $\mathrm{Cl}_{1,1}\cong M_2(\mathbb{R})$, with its real module $\mathbb{R}^2$, is the model case, and the eight-dimensional split biquaternion algebra $\mathbb{H}_{\mathbb{D}}=\mathbb{D}\otimes_{\mathbb{R}}\mathbb{H}$ of is a different algebra altogether. The present article records only the non-split outcome.

## The Clifford Multiplication in the Matrix Model

The action of the Clifford generators on $S$ is explicit in the matrix model, and it makes the absence of a chiral splitting over $\mathbb{R}$ transparent.

**Proposition.** In the matrix model $\Phi\colon\mathbb{B}\to M_2(\mathbb{C})$ with $\Phi(e_k)=-i\sigma_k$ and $\Phi(i)=iI$, the Clifford generators of $\mathrm{Cl}_{3,0}$ act on $S=\mathbb{C}^2$ by

$$
c(\gamma_k)=\sigma_k \qquad (k=1,2,3), \qquad c(\gamma_1\gamma_2)=c(\gamma_1)c(\gamma_2)=\sigma_1\sigma_2=i\sigma_3,
$$

and they satisfy $c(\gamma_k)^{2}=I$ and $c(\gamma_k)c(\gamma_l)+c(\gamma_l)c(\gamma_k)=2\delta_{kl}I$, as the generators of $\mathrm{Cl}_{3,0}$ of square $+1$ must.

**Proof.** The isomorphism sends $\gamma_k\mapsto ie_k$, and $\Phi(ie_k)=\Phi(i)\Phi(e_k)=iI\cdot(-i\sigma_k)=\sigma_k$; the Pauli matrices satisfy $\sigma_k^2=I$ and the anticommutation relations, which are the Clifford relations. For the product, $\gamma_1\gamma_2\mapsto(ie_1)(ie_2)=-e_1e_2=-e_3$, so $c(\gamma_1\gamma_2)=\Phi(-e_3)=\Phi(e_3)\cdot(-1)=i\sigma_3$, in agreement with the product $c(\gamma_1)c(\gamma_2)=\sigma_1\sigma_2=i\sigma_3$. $\square$

**Theorem.** The volume element $\omega=\gamma_1\gamma_2\gamma_3$ acts on $S$ as the scalar $i$, $c(\omega)=iI$, and consequently the module $S$ has no real chirality splitting: as a real-linear operator on the four-dimensional real module, $c(\omega)$ is multiplication by the complex scalar $i$, so it has no eigenvectors over $\mathbb{R}$ at all, its eigenvalues $\pm i$ appearing only after complexification. The real Clifford module is therefore irreducible, in agreement with the complex type of the three-dimensional classification.

**Proof.** By the proposition, $c(\gamma_1)c(\gamma_2)c(\gamma_3)=\sigma_1\sigma_2\sigma_3=iI$. On the other side $\omega\mapsto(ie_1)(ie_2)(ie_3)=i^3e_1e_2e_3=(-i)(-1)=i\,e_0$, since $e_1e_2e_3=-e_0$ in the quaternion convention of the category, so $c(\omega)=\Phi(ie_0)=iI$ and the two computations agree. Since $c(\omega)=iI$ is a scalar, every vector of $S$ is an eigenvector with eigenvalue $i$; the complexification $S\otimes_{\mathbb{R}}\mathbb{C}=S\oplus\overline{S}$ splits into the two eigenspaces of $\omega$ on the complexified module, which are $S$ and $\overline{S}$. The real module has no splitting because $i$ is not real. $\square$

**Corollary.** The chiral halves $S_+$ and $S_-$ are the two eigenspaces of $c(\omega)$ on the complexified module $S\otimes_{\mathbb{R}}\mathbb{C}$, of eigenvalues $+i$ and $-i$; over $\mathbb{R}$ they are amalgamated into the single irreducible module $S$. This is the module-theoretic form of the statement that the three-dimensional definite Clifford algebra has complex type: the chirality operator is defined, but its eigenvalues are not real, so it does not cut the real module.

**Remark.** The explicit multiplication also exhibits the two-sided structure used in the applications: left multiplication by $\mathbb{B}$ and right multiplication by the commuting scalars commute, the left action being the Clifford action on $S$ and the right action being the commutant of the module, which by Schur's lemma is exactly $\mathbb{C}$ for the irreducible complex module. The pair of actions is the reason the spinor module of $\mathbb{B}$ carries both a spin-group action and a commuting scalar structure.

## Summary

The spinor module of the biquaternion algebra is the unique simple module $S=\mathbb{B}p\cong\mathbb{C}^2$ of $\mathbb{B}\cong M_2(\mathbb{C})$, realised as a minimal left ideal for the idempotent $p=\tfrac12(e_0+ie_3)$; its real dimension is four and its commutant is $\mathbb{C}$, so its reality type is complex and no Majorana spinor exists. The group $SL(2,\mathbb{C})=\mathrm{Spin}(1,3)$ acts irreducibly and faithfully on $S$ by left multiplication, while the two elements $\pm e_0$ lying over the identity rotation act by $\pm\mathrm{id}_S$; this two-to-one cover of $SO^{+}(1,3)$ is the reason spinors are needed at all.

Over the complexified algebra $\mathbb{C}\mathrm{l}_3=M_2(\mathbb{C})\times M_2(\mathbb{C})$ the module splits into two chiral halves $S_+$ and $S_-$, conjugate and inequivalent, whose direct sum is the complexification of $S$. The dual $S^{*}$ is identified with $S$ by the $SL(2,\mathbb{C})$-invariant antisymmetric spinor contraction $\varepsilon(u,v)=u^{T}\varepsilon_{0}v$, which is the unique invariant bilinear form up to scale; the conjugate module is the other chiral half and is not the dual. The positive definite Hermitian form is invariant only under $SU(2)\subset SL(2,\mathbb{C})$, and it gives the antilinear identification of $S^{*}$ with the conjugate. The antisymmetric contraction pairs spinors and the Hermitian norm measures them, and the two structures are distinct.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}\cong M_2(\mathbb{C})$ | Biquaternion algebra |
| $p=\tfrac12(e_0+ie_3)$ | Minimal idempotent |
| $S=\mathbb{B}p\cong\mathbb{C}^2$ | Biquaternion spinor module, the defining module |
| $S_{\mathbb{R}}\cong\mathbb{R}^4$ | Real spinor module |
| $SL(2,\mathbb{C})=\{N=1\}$ | Double cover of $SO^{+}(1,3)$, acts on $S$ by left multiplication |
| $S_+=\mathbb{C}^2\otimes1,\ S_-=1\otimes\mathbb{C}^2$ | Chiral halves over $\mathbb{C}\mathrm{l}_3=M_2(\mathbb{C})\times M_2(\mathbb{C})$ |
| $\overline{S}\cong S_-$ | Conjugate module, the second chiral half |
| $S^{*}$ | Dual module, identified with $S$ by $\varepsilon$ |
| $\varepsilon(u,v)=u^{T}\varepsilon_{0}v$ | Spinor contraction, antisymmetric and $SL(2,\mathbb{C})$-invariant |
| $\varepsilon_{0}$ | Symplectic form matrix, $\varepsilon_{0}^{2}=-1$ |
| $h(u,v)=u^{\dagger}v$ | Hermitian form, invariant under $SU(2)$ only |
| $\|u\|_h^2=h(u,u)$ | Hermitian spinor norm, positive definite |
| $d=p-q$, $N(\tilde Q)=\sum_\mu Q_\mu^2$ | Signature difference and norm form |



## Further Reading

- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for spinor modules, chirality and the invariant forms on spinors.
- Élie Cartan, *The Theory of Spinors* (Hermann, 1966; Dover reprint 1981), for the classical theory of two-component spinors and their invariant forms.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the module theory of the low-dimensional Clifford algebras and the duality of the spinor module.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for explicit spinor modules and their bilinear and Hermitian forms.
- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings* (Springer, 1991), for Hermitian and bilinear forms on modules over central simple algebras.
