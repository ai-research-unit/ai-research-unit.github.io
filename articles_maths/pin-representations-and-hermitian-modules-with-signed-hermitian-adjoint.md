# __Pin Representations and Hermitian Modules with Signed Hermitian Adjoint__

## Introduction

The spin representation is the Clifford action restricted to the even part of the group, and the pin representation is the same action restricted to the whole pin group. That construction, together with its chirality and its real forms, is *Pin Representations and Clifford Modules with Signed Inner Conjugation*, where the module is an ordinary Clifford module and the two-sided operator governing the geometry is the signed inner conjugation.

This article reads the same representation on a **Hermitian Clifford module**, that is on a Clifford module equipped with the Hermitian form for which the Clifford action is self-adjoint,

$$
(x\cdot s,t)=(s,x^{\dagger}\cdot t),\qquad x\in\mathrm{Cl}(V,q),\ s,t\in S,
$$

the module theory of *Hermitian Modules over a Hilbert Algebra with Hermitian Adjoint*. The definition of the pin representation does not change,

$$
\rho:\mathrm{Pin}(V,q)\longrightarrow GL(S),\qquad \rho(x)s=x\cdot s ,
$$

and it is still one-sided by construction, since the algebra acts on a module by left multiplication. What the Hermitian structure changes is the **adjoint** of the group action and the form of the intertwining identity. The adjoint of the action of $x$ is the action of the dagger,

$$
\rho(x)^{*}=\rho(x^{\dagger}),
$$

by the self-adjointness axiom; consequently the elements of the **unitary slice** act by unitary operators, $\rho(x)^{*}=\rho(x)^{-1}$ for $x\in U$, and the two-sided operator that the module naturally produces is the Hermitian sandwich

$$
\rho(x)\,\rho(v)\,\rho(x)^{*}=\rho\bigl(\Theta_x(v)\bigr),
\qquad\text{hence}\qquad
\rho\bigl(\Theta^{\alpha}_x(v)\bigr)=\varepsilon_x\,\rho(x)\,\rho(v)\,\rho(x)^{*},
$$

with $\varepsilon_x=(-1)^{k}$ the parity sign of $x$. The signed Hermitian sandwich of *Two-Sided Operators on a Hilbert Algebra with Signed Hermitian Adjoint* is therefore the two-sided operator whose action on $V$ matches the module conjugation **up to the parity sign**, exactly as in the inverse formulation, and the odd part of the pin group is again the part that the unsigned operator cannot describe.

The Clifford algebra, its parity grading and the grade involution are *Clifford Algebras* and *Clifford Algebras in Finite Dimensions*; the general theory of modules, of the simple and semisimple modules and of the density theorem is *Modules over an Algebra* and *Simple and Semisimple Modules*; the Clifford modules, the explicit spinor module, chirality and the eightfold table are *Spin Representations and Clifford Modules with Inner Conjugation*; the Hermitian structure on a module and the self-adjointness axiom are *Hermitian Modules over a Hilbert Algebra with Hermitian Adjoint*; the adjoint of the one-sided action is *The Adjoint of the One-Sided Action with Hermitian Adjoint* and *One-Sided Operators on a Hilbert Algebra with Signed Hermitian Adjoint*; the groups and the norm are *The Pin and Spin Groups with Signed Hermitian Adjoint*; the two-sided operator is *Two-Sided Operators on a Hilbert Algebra with Signed Hermitian Adjoint*; the ideal description is *Spinors as Minimal Left Ideals with Signed Hermitian Adjoint*. Nothing owned by those entries is re-derived. The base is a commutative ring $A$ with involution $\sigma$, $F$ the field of scalars of characteristic not two, $q$ non-degenerate of dimension $n$ on $V$, and $\mathrm{Cl}_{p,q}$ for the real forms.

## The Pin Representation

**Definition.** Let $S$ be a Hermitian Clifford module over $\mathrm{Cl}(V,q)$. The **pin representation** is the restriction of the algebra action to the pin group,

$$
\rho(x)s=x\cdot s,\qquad x\in\mathrm{Pin}(V,q),\ s\in S,
$$

and the **spin representation** is its restriction to $\mathrm{Spin}(V,q)=\mathrm{Pin}(V,q)\cap\mathrm{Cl}^0(V,q)$.

**Proposition (the basics).** The pin representation is a well-defined group representation, $\rho(1)=\mathrm{id}_S$, $\rho(xz)=\rho(x)\rho(z)$, and

$$
\rho(-1)=-\mathrm{id}_S ,
$$

since $S\neq0$ and $-1$ is the scalar $-1$ of the algebra. Hence the pin representation does not descend to $O(V,q)$, exactly as the spin representation does not descend to $SO(V,q)$.

*Proof.* The algebra action is associative, so $x\cdot(z\cdot s)=(xz)\cdot s$; $-1$ is central and acts as $-\mathrm{id}$ on a nonzero module; and $-1$ lies in the kernel of the projection of $\mathrm{Pin}$ to $O(V,q)$.

**Proposition (self-adjointness and the dagger).** With respect to the form of the module,

$$
\bigl(\rho(x)\bigr)^{*}=\rho(x^{\dagger}),\qquad x\in\mathrm{Cl}(V,q),
$$

and consequently the elements of the unitary slice act by unitary operators,

$$
\rho(x)^{*}=\rho(x)^{-1}\quad\text{for }x\in U .
$$

*Proof.* $(\rho(x)s,t)=(x\cdot s,t)=(s,x^{\dagger}\cdot t)=(s,\rho(x^{\dagger})t)$ by the self-adjointness axiom; on the slice $x^{\dagger}=x^{-1}$, so $\rho(x)^{*}=\rho(x)^{-1}$.

**Remark (why the Hermitian form is the right home for the pin theory).** The pin group contains the odd elements, and an odd element $u\in V$ has $u^{\dagger}=-\sigma(u)$, so its module operator satisfies $\rho(u)^{*}=-\rho(\sigma(u))$, which is the skew-adjointness of the Clifford action of a vector read on the group. On the slice, where $q(u)=-1$, this gives $\rho(u)^{*}=\rho(u)^{-1}$ and the odd elements act by unitary operators as well; the pin representation of a definite form is thus a unitary representation of the pin group on a Hermitian module, and it is the Hermitian form, not the group, that supplies the unitarity.

**Theorem (faithfulness and the kernel).** Suppose $S$ is irreducible. If $\mathrm{Cl}(V,q)$ is simple the pin representation is faithful, and its restriction to $\mathrm{Spin}(V,q)$ is the spin representation. If $\mathrm{Cl}(V,q)\cong A'\times A'$ is a product of two simple algebras and $S$ is the irreducible module of the first factor, then

$$
\ker\rho=\mathrm{Pin}(V,q)\cap\bigl(\{1\}\times A'\bigr).
$$

*Proof.* The annihilator of an irreducible module is a proper two-sided ideal, hence vanishes over a simple algebra; over a product the module of one factor is annihilated by the other. Restricting a faithful action to a subgroup is faithful. The argument is independent of the Hermitian form.

**Remark.** The kernel has the same shape as in the inverse formulation; the Hermitian structure adds no kernel, it adds the adjoint.

## The Parity of the Odd Part

**Proposition (chirality).** Suppose $n$ is even and $S=\Delta_+\oplus\Delta_-$ is the chiral decomposition, on which $\mathrm{Cl}^0$ acts preserving the summands and $\mathrm{Cl}^1$ acts interchanging them. Then every element of $\mathrm{Spin}(V,q)$ preserves $\Delta_\pm$ and every odd element of $\mathrm{Pin}(V,q)$ interchanges them. The two chiral summands are orthogonal for the Hermitian form, because the form pairs only elements of the same parity in the sense of $\mathrm{Cl}^0$, as recorded in *The Blade Form and the Hilbert Structure with Hermitian Adjoint*.

*Proof.* $\mathrm{Cl}^{i}\cdot S^{j}\subseteq S^{i+j}$, the exponent read modulo two; the orthogonality is the even-ness of the form.

**Corollary (irreducibility).** If $S$ is an irreducible Clifford module of even dimension, the pin representation on $S$ is irreducible, while its restriction to $\mathrm{Spin}(V,q)$ is the sum of the two half-spin representations on $\Delta_\pm$, each irreducible over the even part.

*Proof.* The algebra is spanned by products of vectors, hence by $\mathrm{Pin}(V,q)$, so the $\mathrm{Pin}$-submodules of $S$ are the $\mathrm{Cl}(V,q)$-submodules and the irreducibility carries over; the restriction splits along $\Delta_\pm$.

**Remark.** A pinor is a vector of an irreducible module of the whole algebra and a half-spinor is a vector of an irreducible module of the even part; the Hermitian form of the module restricts to each chiral summand, and the two are orthogonal, so the pinor module is the orthogonal sum of the two half-spin modules as a Hermitian module. This is the structural difference between pinors and spinors in the form in which the Hermitian reading presents it.

## The Sign in the Intertwining Identity

**Proposition (the intertwining identities).** Let $v\in V$ and $x\in\mathrm{Pin}(V,q)$. Then

$$
\rho(x)\,\rho(v)\,\rho(x)^{*}=\rho\bigl(\Theta_x(v)\bigr),
\qquad
\rho\bigl(\Theta^{\alpha}_x(v)\bigr)=\varepsilon_x\,\rho(x)\,\rho(v)\,\rho(x)^{*},
$$

with $\varepsilon_x=(-1)^{k}$ the parity sign. For $x\in U$ the first identity reads $\rho(x)\rho(v)\rho(x)^{-1}=\rho(\Theta_x(v))$.

*Proof.* $\rho(x)\rho(v)\rho(x)^{*}=\rho(x)\rho(v)\rho(x^{\dagger})=\rho(x\,v\,x^{\dagger})=\rho(\Theta_x(v))$ by the adjoint proposition and the multiplicativity of $\rho$. The second identity is $\Theta^{\alpha}_x=\varepsilon_x\Theta_x$.

**Corollary (the reflection in the module).** Let $u\in V$ with $q(u)\neq0$ and let $\rho_u$ be the reflection in $u^{\perp}$. Then for every $v\in V$

$$
\rho(u)\,\rho(v)\,\rho(u)^{*}=\rho\bigl(-q(u)\,\rho_u(v)\bigr),
$$

and on the unitary slice, $q(u)=-1$, this is $\rho(u)\rho(v)\rho(u)^{-1}=\rho(\rho_u(v))$: the odd element of the pin group realises the reflection in the module exactly when it is a slice-normalised vector.

*Proof.* $\Theta_u=-q(u)\rho_u$ by the vector proposition of the two-sided article, and $\rho(u)^{*}=\rho(u^{\dagger})=-\rho(\sigma(u))$; the slice statement is the reflection proposition of the group article.

**Proposition (the odd elements are square roots).** For $u\in V$ one has $\rho(u)^{2}=\rho(u^{2})=q(u)\mathrm{id}_S$, and for a product $x=u_1\cdots u_k\in\mathrm{Pin}$ one has $\rho(x)^{2}=\prod_iq(u_i)\,\mathrm{id}_S$, an invertible scalar. For $u$ on the slice $\rho(u)^{2}=-\mathrm{id}_S$, so $\rho(u)$ is a complex structure on the module.

*Proof.* The algebra action is a representation of the algebra, so $\rho(u)^{2}=\rho(u^{2})=q(u)\rho(1)$; the slice value is $q(u)=-1$.

**Remark (the sign is what the odd part needs).** On the even part $\varepsilon_x=1$ and the module conjugation intertwines the unsigned Hermitian sandwich itself; on the odd part $\varepsilon_x=-1$ and the module conjugation gives the negative of the geometric sandwich, so it is the **signed** Hermitian sandwich that restores the agreement between the action of $\mathrm{Pin}$ on $S$ and its action on $V$. This is the module-theoretic reason for the signed member, and it is unchanged from the inverse formulation; the Hermitian reading adds that the same operators are the adjoints of the group action and that the slice elements act unitarily.

## Real Pin Modules

**Proposition.** Let $S$ be a real Hermitian Clifford module. The restriction of the pin representation to $\mathrm{Spin}(V,q)$ is the real spin representation, and for an odd $x\in\mathrm{Pin}(V,q)$ the operator $\rho(x)$ reverses the chirality when $n$ is even. On an irreducible module over a simple real Clifford algebra the pin representation is faithful, so the real pinor and the real spinor are vectors of the same module and differ only in the group that is allowed to act on them.

*Proof.* The restriction statement is the definition; the parity statement is the chirality proposition; faithfulness is the kernel theorem with the classification of the real Clifford algebras.

**Remark (the definite case).** For a definite real form the standard module form of *Hilbert Algebras* makes each Clifford coefficient skew-adjoint, $(e_j\cdot s,t)=-(s,e_j\cdot t)$, so an even element of $\mathrm{Pin}$ acts by an orthogonal operator and an odd element by the composition of an odd number of skew operators, with $\rho(u)^{2}=q(u)\mathrm{id}_S$ of the sign of $q(u)$. In the negative definite convention of the corpus, $q(u)=-1$ on the slice, and the slice elements — the normalised roots of the reflection-group article among them — act unitarily, and their products span the compact groups. The compact real form is *The Unitary Slice and the Compact Real Form with Hermitian Adjoint*.

**Remark (the dictionary with the inverse formulation).** Whenever $\sigma=\mathrm{id}$ and the elements considered lie on the slice, the two formulations give the same representation: $\Theta^{\alpha}_x=\mathrm{Ad}^{\alpha}_x$, and the intertwining identities above are those of *Pin Representations and Clifford Modules with Signed Inner Conjugation*. The Hermitian reading adds the adjoint $\rho(x)^{*}=\rho(x^{\dagger})$, the unitarity on the slice, and the coupling of the module form to the algebra form; it adds no new representation.

## Summary

The pin representation of a Hermitian Clifford module is the restriction of the algebra action to the pin group, $\rho(x)s=x\cdot s$, and it is one-sided by construction. The Hermitian structure contributes its **adjoint**, $\rho(x)^{*}=\rho(x^{\dagger})$, so the elements of the unitary slice act by unitary operators and the two-sided operator that the module produces is the Hermitian sandwich,

$$
\rho(x)\,\rho(v)\,\rho(x)^{*}=\rho\bigl(\Theta_x(v)\bigr),
\qquad
\rho\bigl(\Theta^{\alpha}_x(v)\bigr)=\varepsilon_x\,\rho(x)\,\rho(v)\,\rho(x)^{*},
$$

with $\varepsilon_x=(-1)^{k}$. The module conjugation intertwines the unsigned sandwich on the even part and its negative on the odd part, so the **signed** Hermitian sandwich is the operator whose action on $V$ agrees with the module action up to the parity sign; for a slice-normalised vector $u$, $\rho(u)\rho(v)\rho(u)^{-1}=\rho(\rho_u(v))$, so the odd elements of the pin group realise the reflections in the module exactly on the slice, and $\rho(u)^{2}=-\mathrm{id}_S$ is a complex structure there. Chirality, irreducibility, the kernel and the real forms are as in the inverse formulation: the odd elements interchange the two chiral summands, which are Hermitian-orthogonal, the pin representation is irreducible where the spin representation splits into the two half-spin representations, and the kernel is the intersection of the pin group with the annihilator of the module. A pinor is a spinor of the whole algebra, a half-spinor one of the even part, and the Hermitian form restricts to each half and pairs them trivially.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\rho(x)s=x\cdot s$ | Pin representation, one-sided |
| $(x\cdot s,t)=(s,x^{\dagger}\cdot t)$ | Hermitian Clifford module, self-adjointness |
| $\rho(x)^{*}=\rho(x^{\dagger})$ | Adjoint of the group action |
| $\rho(x)^{*}=\rho(x)^{-1}$, $x\in U$ | Unitary operators on the slice |
| $\rho(x)\rho(v)\rho(x)^{*}=\rho(\Theta_x(v))$ | Intertwining by the unsigned sandwich |
| $\rho(\Theta^{\alpha}_x(v))=\varepsilon_x\rho(x)\rho(v)\rho(x)^{*}$ | The parity sign |
| $\rho(u)\rho(v)\rho(u)^{-1}=\rho(\rho_u(v))$, $q(u)=-1$ | Reflection in the module on the slice |
| $\mathrm{Cl}^1\cdot S^{\pm}\subseteq S^{\mp}$ | Odd elements reverse chirality |

## Further Reading

- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the Clifford module with a Hermitian form, the self-adjoint Clifford action and the pin representations.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for pinors, spinors, chirality and the definite real forms.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for the adjoint with respect to a Hermitian form and the unitary group.
- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for the modules over a Clifford algebra and the kernel of the pin representation.
