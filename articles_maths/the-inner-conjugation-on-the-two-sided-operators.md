# __The Inner Conjugation on the Two-Sided Operators__

## Introduction

Among the two-sided operators of *The Sandwich on a Clifford Algebra* the first to be singled out by the geometry is the one whose two parameters are a unit and its inverse,

$$
\mathrm{Ad}_x(y) = x\,y\,x^{-1}, \qquad x \in \mathrm{Cl}(V,q)^{\times},
$$

the **inner conjugation**. It is the composite $T_{x,x^{-1}} = L_xR_{x^{-1}}$, and it is the only member of the two-parameter family that is a homomorphism of the multiplicative monoid as well as of the additive group: the sandwich with two independent parameters forgets the unit, the inner conjugation fixes it and is an algebra automorphism.

The inner conjugation alone, however, does not carry the orthogonal group correctly. On the quadratic space it realises the isometry $v \mapsto x\,v\,x^{-1}$, and for an odd versor this is the **negative** of the reflection; the central volume element of an odd-dimensional algebra is invisible to it. The action that repairs both defects is the **twisted action** $\chi_x(y) = x\,y\,\alpha(x)^{-1}$, which differs from the inner conjugation by the parity sign and returns the reflection itself. This article treats the two maps together: the algebraic operator and its kernel, the orthogonal action, and the two-sided operators that realise the automorphisms of the algebra.

The sandwich and its composition law are *The Sandwich on a Clifford Algebra*; the group of two-sided operators and the spin group built from it are *The Two-Sided Operators and the Spin Group*; the Clifford, pin and spin groups and their exact sequences are *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*, and the kernel and the reflection formula for the signed member $\mathrm{Ad}^{\alpha}$ are *Two-Sided Operators on a Clifford Algebra with Signed Inner Conjugation*. Those results are quoted, not re-derived. The algebra and its grading are *Clifford Algebras* and *Clifford Algebras in Finite Dimensions*.

## The Inner Conjugation as a Two-Sided Operator

**Definition.** For a unit $x \in \mathrm{Cl}(V,q)^{\times}$ the **inner conjugation** by $x$ is the $F$-linear map $\mathrm{Ad}_x(y) = x\,y\,x^{-1}$. It is the sandwich $T_{x,x^{-1}}$, and it is defined on the unit group alone, because the right factor is the inverse.

**Proposition (the automorphism).** $\mathrm{Ad}_x$ is an algebra automorphism of $\mathrm{Cl}(V,q)$: it is $F$-linear, bijective, multiplicative, and it fixes $1$.

**Proof.** Multiplicativity is $\mathrm{Ad}_x(yz) = x\,yz\,x^{-1} = (xyx^{-1})(xzx^{-1}) = \mathrm{Ad}_x(y)\mathrm{Ad}_x(z)$; the inverse is $\mathrm{Ad}_{x^{-1}}$, and $\mathrm{Ad}_x(1) = xx^{-1} = 1$.

**Proposition (composition).** $\mathrm{Ad}_x \circ \mathrm{Ad}_z = \mathrm{Ad}_{xz}$, so $x \mapsto \mathrm{Ad}_x$ is a homomorphism from the unit group to $\mathrm{Aut}(\mathrm{Cl}(V,q))$.

**Proof.** $\mathrm{Ad}_x\bigl(\mathrm{Ad}_z(y)\bigr) = x\,z\,y\,z^{-1}\,x^{-1} = (xz)y(xz)^{-1}$.

**Proposition (parity and the value at the unit).** $\mathrm{Ad}_x$ preserves the grading modulo two, $\mathrm{Ad}_x(\mathrm{Cl}^{i}) \subseteq \mathrm{Cl}^{i}$, and $\mathrm{Ad}_x(1) = 1$.

**Proof.** Conjugation by an invertible element preserves the degree of every homogeneous element because the factors $x$ and $x^{-1}$ have the same parity and their parities cancel; the value at the unit is the previous proposition.

**Remark (what the inner conjugation loses).** The value at the unit is the identity on both parities, and this is exactly the difference from the signed member $\mathrm{Ad}^{\alpha}_x = \alpha(x)yx^{-1}$, whose value at the unit is the parity sign $\varepsilon_x$. The two agree on the even part and differ by $-1$ on the odd part, as *Two-Sided Operators on a Clifford Algebra with Signed Inner Conjugation* states; the operator studied here is the unsigned one, and the sign is deliberately absent.

### The Kernel and the Inner Automorphism Group

**Definition.** The **inner automorphism group** of the algebra is $\mathrm{Inn}(\mathrm{Cl}(V,q)) = \{\mathrm{Ad}_x : x \in \mathrm{Cl}(V,q)^{\times}\}$.

**Theorem (the exact sequence).** There is a short exact sequence of groups

$$
1 \longrightarrow Z\bigl(\mathrm{Cl}(V,q)\bigr)^{\times} \longrightarrow \mathrm{Cl}(V,q)^{\times} \xrightarrow{\ \mathrm{Ad}\ } \mathrm{Inn}\bigl(\mathrm{Cl}(V,q)\bigr) \longrightarrow 1 ,
$$

where the kernel is the group of units of the centre; consequently $\mathrm{Inn}(\mathrm{Cl}) \cong \mathrm{Cl}^{\times}/Z^{\times}$. In even dimension the kernel is $F^{\times}$; in odd dimension it is $F^{\times} \cup F^{\times}\omega$, with $\omega$ the volume element.

**Proof.** $\mathrm{Ad}_x = \mathrm{id}$ says $xy = yx$ for every $y$, which is centrality; the description of the centre of a Clifford algebra of a non-degenerate form is that of *Clifford Algebras in Finite Dimensions*, and the computation of this kernel is stated in *Two-Sided Operators on a Clifford Algebra with Signed Inner Conjugation*.

**Corollary (the volume element is invisible).** Let $\dim V$ be odd and let $\omega$ be the volume element. Then $\omega$ is an odd central unit, $\mathrm{Ad}_\omega = \mathrm{id}$, and $\omega$ is not a scalar. So the inner conjugation is not faithful on the Clifford group in odd dimension.

## The Twisted Action and the Orthogonal Group

**Definition.** The **twisted action** of a unit $x$ is $\chi_x(y) = x\,y\,\alpha(x)^{-1}$, the sandwich by the pair $(x, \alpha(x)^{-1})$.

**Proposition (the relation to the inner conjugation).** Let $x$ be homogeneous of degree $k$ and let $\varepsilon_x = (-1)^{k}$. Then

$$
\chi_x = \varepsilon_x\,\mathrm{Ad}_x ,
$$

so the two actions agree on the even part of the unit group and are negatives on the odd part.

**Proof.** For a homogeneous $x$, $\alpha(x)^{-1} = \varepsilon_x x^{-1}$, as in *The Sandwich on a Clifford Algebra*, and $\varepsilon_x$ is central.

**Theorem (the orthogonal group).** The assignment $x \mapsto \chi_x\big|_{V}$ is a surjective homomorphism

$$
\Gamma(V,q) \longrightarrow O(V,q)
$$

with kernel $F^{\times}$, and its restriction to the even part of the Clifford group is a surjection onto $SO(V,q)$. On the norm-one part the kernel is $\{\pm1\}$ and the map is the double cover

$$
1 \longrightarrow \{\pm1\} \longrightarrow \mathrm{Spin}(V,q) \longrightarrow SO(V,q) \longrightarrow 1 .
$$

**Proof.** The twisted action of a versor is an isometry of $V$, and the kernel is $F^{\times}$ by *The Two-Sided Operators and the Spin Group*, where the double cover is also proved; the conclusion for $SO$ is the theorem of *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*.

**Corollary (the inner conjugation realises the same group, up to the sign).** The composite $x \mapsto \mathrm{Ad}_x\big|_V$ has the same image $O(V,q)$ and the same kernel $F^{\times}$, because $\mathrm{Ad}_x = \varepsilon_x\chi_x$ and $\varepsilon_x^{2} = 1$; but for an odd versor it returns $-\rho_u$ where $\chi$ returns $\rho_u$. So the group is the same and the map is the wrong one on the odd part.

**Remark (why the twisted action and not the inner conjugation).** The two-sided operator on the algebra does not distinguish the two, since they differ by a central scalar and their images in $\mathcal{T}$ generate the same subgroup. What distinguishes them is the vector space: only the twisted action maps a vector $u$ to the reflection $\rho_u$. This is the reason the pin and spin groups are stated with the twisted action and the reflections are carried by it, as *The Clifford, Pin and Spin Groups with Signed Inner Conjugation* records.

## The Two-Sided Operators Realising the Automorphisms

**Proposition (the inner automorphisms are sandwiches).** The map $x \mapsto \mathrm{Ad}_x$ is a surjection $\mathrm{Cl}(V,q)^{\times} \to \mathrm{Inn}(\mathrm{Cl}(V,q))$ with kernel the central units; in the operator notation of *The Two-Sided Operators and the Spin Group* it is the restriction of the parametrisation $(a,b) \mapsto T_{a,b}$ to the diagonal pairs $b = a^{-1}$.

**Proof.** The first statement is the exact sequence above; the second is the definition of the restriction.

**Corollary (the interior automorphisms inside the two-sided group).** Inside the group $\mathcal{T}$ of invertible sandwiches the pairs $(x, x^{-1})$ form a subgroup isomorphic to $\mathrm{Cl}(V,q)^{\times}/Z^{\times}$, and the versors form inside it the subgroup generated by the twisted conjugations of *The Two-Sided Operators and the Spin Group*. The sandwiches not of this form, with $b \neq a^{-1}$, act on the algebra by maps that are not multiplicative and are not automorphisms; they are the maps of the Hermitian and intrinsic families once those structures are available.

## Worked Cases

### An Odd Versor

In $\mathrm{Cl}_{0,3}(\mathbb{R})$ with $e_j^{2} = -1$ let $x = e_1$. Then $\varepsilon_x = -1$ and $\mathrm{Ad}_{e_1}$ acts on the basis by $(e_1, -e_2, -e_3)$, while $\chi_{e_1} = -\mathrm{Ad}_{e_1}$ acts by $(-e_1, e_2, e_3) = \rho_{e_1}$. The inner conjugation returns a map that is not a reflection of the quadratic space but its negative, and only the twisted action is the isometry that the pin group needs.

### The Volume Element

In the same algebra the volume element $\omega = e_1e_2e_3$ is a unit of odd parity with $\omega^{2} = 1$, so $\mathrm{Ad}_\omega = \mathrm{id}$ while $\chi_\omega = -\mathrm{id}$ on the whole algebra. Hence $\omega$ lies in the kernel of the inner conjugation and not in the kernel of the twisted action; it is an odd central unit, so it witnesses both the failure of faithfulness of $\mathrm{Ad}$ in odd dimension and the need for the sign in $\chi$.

### A Central Scalar

For $c \in F^{\times}$, $\mathrm{Ad}_c = \mathrm{id}$ and $\chi_c = \mathrm{id}$. So the scalar group is the kernel of both actions and the quotient $\Gamma \to O(V,q)$ is by $F^{\times}$, as the exact sequence records.

## Summary

The **inner conjugation** $\mathrm{Ad}_x(y) = x\,y\,x^{-1}$ is the sandwich with $b = a^{-1}$; it is an algebra automorphism, it composes by $\mathrm{Ad}_x\mathrm{Ad}_z = \mathrm{Ad}_{xz}$, it preserves the parity grading, and it fixes the unit. Its kernel is the group of units of the centre, so it defines the exact sequence $1 \to Z(\mathrm{Cl})^{\times} \to \mathrm{Cl}^{\times} \to \mathrm{Inn}(\mathrm{Cl}) \to 1$; in odd dimension the central volume element lies in that kernel and the map is not faithful. The **twisted action** $\chi_x(y) = x\,y\,\alpha(x)^{-1}$ is the sandwich by $(x, \alpha(x)^{-1})$, equal to $\varepsilon_x\mathrm{Ad}_x$; it differs from the inner conjugation by the parity sign, agrees with it on the even part, and is the action that maps a vector to the reflection. The two actions give the same groups, $\Gamma(V,q) \to O(V,q)$ with kernel $F^{\times}$ and $\mathrm{Spin}(V,q) \to SO(V,q)$ with kernel $\{\pm1\}$, but only the twisted one is orthogonal on the odd part. Inside the group of invertible two-sided operators the inner conjugations form the subgroup of the diagonal pairs, isomorphic to $\mathrm{Cl}^{\times}/Z^{\times}$; the results on the groups themselves are those of *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{Ad}_x(y) = x\,y\,x^{-1}$ | Inner conjugation, the operator of this article |
| $\chi_x(y) = x\,y\,\alpha(x)^{-1}$ | Twisted action |
| $\alpha$, $\varepsilon_x = (-1)^{k}$ | Grade involution and its sign on a homogeneous element |
| $\chi_x = \varepsilon_x\mathrm{Ad}_x$ | Relation between the two actions |
| $\mathrm{Inn}(\mathrm{Cl}) = \mathrm{Cl}^{\times}/Z^{\times}$ | Inner automorphism group |
| $Z(\mathrm{Cl}(V,q))^{\times}$ | Central units, the kernel of $\mathrm{Ad}$ |
| $\Gamma(V,q)$ | Clifford group, the versors |
| $\mathrm{Ad}_u\big|_V = -\rho_u$, $\chi_u = \rho_u$ | An odd vector, the reflection and its negative |
| $O(V,q)$, $SO(V,q)$, $\mathrm{Spin}(V,q)$ | Orthogonal, special orthogonal and spin groups |
| $\mathcal{T}$ | Group of invertible two-sided operators |

## Further Reading

- Claude Chevalley, *The Algebraic Theory of Spinors and Clifford Algebras*, Collected Works vol. 2 (Springer, 1997), for the inner automorphisms of a Clifford algebra and the twisted action on vectors.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced Mathematics 50 (Cambridge University Press, 1995), for the centre and the inner automorphism group.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the reflection formula and the two conjugation actions.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for the automorphisms of a Clifford algebra and the sign of the reflection.
- Nathan Jacobson, *Lectures in Abstract Algebra II: Linear Algebra* (Van Nostrand, 1953), for the inner automorphism group of a finite-dimensional algebra.
