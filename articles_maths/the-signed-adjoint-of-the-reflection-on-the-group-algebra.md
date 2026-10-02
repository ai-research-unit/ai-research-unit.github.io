
# __The Signed Adjoint of the Reflection on the Group Algebra__

## Introduction

A reflection of the group algebra is the signed conjugation $\rho_u(f) = u*\alpha(f)*u^{-1}$, a signed sandwich in which the two parameters are mutually inverse, and its adjoint with respect to the Haar pairing is the reflection in the parameter $\alpha(u^*)$, the composite of the grade involution and the involution. Whether a reflection is self-adjoint, unitary or an involution is then decided by three separate conditions on the reflector $u$: self-adjointness by the centrality of the composite $\sigma(u)^{-1}u$, unitarity by the unitarity of $u$, and involution by the centrality of $u*\alpha(u)$. The three are independent in general, and their coincidence is a degenerate phenomenon. This article computes the adjoint of a reflection, states the three criteria and the degenerate cases, and reads the result on the point masses and on the fixed subgroup of the composite involution.

The article assumes the group, its Haar measure and the modular function from *Locally Compact Groups and Haar Measure*; the group algebra, its involution and its completions from *The Convolution Algebra $L^1(G)$* and *The Group Algebra as an Involutive Algebra*; the grade involution, the operator $\mathrm{A}$, the reflectors, the reflections $\rho_u = S_{u,u^{-1}}$, the law $\rho_u^2 = c_{u*\alpha(u)}$ and the parametrisation of the reflections modulo $Z(\mathcal{A})^\times$ from *The Signed Sandwich on the Group Algebra*; the adjoint of the signed sandwich $(S_{a,b})^* = S_{\alpha(a^*),\alpha(b^*)}$ from *The Signed Adjoint Sandwich on the Group Algebra*, immediately preceding; the continuous involution and the associated involutive automorphism $\sigma = \alpha\iota$, its fixed subgroup and the reflections of a topological group from *Involutive Topological Groups* and its companions; and the adjoint on the group algebra from *Hermitian Operators on a Group Algebra*. The signed adjoint of the left multiplication is next; the adjoint of a convolution operator on its own terms is *The Adjoint of a Convolution Operator*, later in this group; the discrete version is *The Signed Adjoint of the Reflection on a Topological Group*.

Throughout, $G$ is a locally compact Hausdorff group with left Haar measure $dx$; $\mathcal{A} = L^1(G)$ carries the involution $f^*(x) = \overline{f(x^{-1})}\Delta(x)^{-1}$ and the Haar pairing; $\alpha$ is a **grade involution**, $\mathrm{A}f = \alpha(f)$, $\sigma = \alpha\circ\,^*$ is the **composite anti-automorphism**, $\sigma(a) = \alpha(a^*)$, and the **reflection** determined by a unit $u$ is

$$
\rho_u = S_{u,\,u^{-1}}, \qquad \rho_u(f) = u*\alpha(f)*u^{-1} , \qquad \rho_u^2 = c_{u*\alpha(u)} , \quad c_t(f) = t*f*t^{-1} .
$$

The element $u$ is a **reflector** when $u*\alpha(u)$ is central, in which case $\rho_u$ is an involutive automorphism. The adjoint is taken with respect to the Haar pairing, and the right-handed identities are read in the **unimodular** case.

## The Adjoint of a Reflection

**Theorem (the adjoint is the reflection in $\sigma(u)$).** With respect to the Haar pairing,

$$
\bigl(\rho_u\bigr)^* = S_{\alpha(u^*),\,\alpha((u^*)^{-1})} = \rho_{\alpha(u^*)} = \rho_{\sigma(u)} ,
$$

so the adjoint of a reflection is the reflection in the parameter $\sigma(u) = \alpha(u^*)$; the adjoint operation is an involution on the family of reflections, $\bigl((\rho_u)^*\bigr)^* = \rho_u$.

**Proof.** Apply the signed-sandwich adjoint to the parameters $a = u$, $b = u^{-1}$: $(\rho_u)^* = S_{\alpha(u^*),\alpha((u^{-1})^*)}$. Since $(u^{-1})^* = (u^*)^{-1}$, the second parameter is $\alpha((u^*)^{-1}) = \alpha(u^*)^{-1}$; hence $(\rho_u)^* = S_{\alpha(u^*),\,\alpha(u^*)^{-1}} = \rho_{\alpha(u^*)}$, which is the reflection determined by $\alpha(u^*)$. The double adjoint uses $\sigma^2 = \mathrm{id}$, that is $\alpha^2 = \mathrm{id}$ and the order two of the involution. $\square$

**Corollary (the reflection family is closed under the adjoint).** The adjoint carries reflections to reflections and reflectors to reflectors,

$$
u \text{ a reflector} \iff \alpha(u^*) \text{ a reflector},
$$

and it is an involution on the reflection family and on the reflector family alike.

**Proof.** By the theorem $(\rho_u)^* = \rho_{\alpha(u^*)}$; the reflection $\rho_{\alpha(u^*)}$ is defined for every unit $\alpha(u^*)$, and it is involutive exactly when its parameter satisfies the reflector condition, which is the displayed equivalence by the reflector criterion $\rho_v^2 = \mathrm{id}\iff v*\alpha(v)$ central and $\rho_u = \rho_v$ iff the ratio is a central unit. $\square$

## The Three Criteria

**Theorem (self-adjointness).** The reflection $\rho_u$ is self-adjoint, $\rho_u^* = \rho_u$, if and only if

$$
\alpha(u^*)^{-1}\,u \in Z(\mathcal{A})^\times ,
$$

equivalently if and only if the reflector $u$ and its composite $\sigma(u) = \alpha(u^*)$ differ by a central unit; on the point masses this is the condition $h^{-1}\sigma(h)\in Z(G)$, and the self-adjoint reflections are parametrised by the units modulo the central relation generated by $\sigma$.

**Proof.** $\rho_u^* = \rho_{\alpha(u^*)}$ equals $\rho_u$ exactly when the two parameters determine the same reflection, which by the reflection identity criterion holds exactly when the ratio $\alpha(u^*)^{-1}u$ is a central unit. For $u = \delta_h$ on a discrete group, $\alpha(u^*) = \delta_{\sigma(h)}$ and the centrality of $\delta_{\sigma(h)^{-1}h}$ is the condition $\sigma(h)^{-1}h\in Z(G)$. $\square$

**Theorem (unitarity).** The reflection $\rho_u$ is unitary if and only if $u$ is a unitary element of $\mathcal{A}$,

$$
\rho_u^*\rho_u = \rho_u\rho_u^* = 1 \iff u^*\!*u = u*\!u^* = 1 ,
$$

so on a non-discrete group algebra no reflection is unitary, and on a discrete group every point mass determines a unitary reflection.

**Proof.** This is the unitarity criterion for the signed sandwich $S_{a,b}$ with $a = u$, $b = u^{-1}$: the sandwich is unitary exactly when both parameters are unitary, and $u^{-1}$ is unitary with $u$. The absence of unitary elements on a non-discrete $L^1(G)$ is *The Group Algebra as an Involutive Algebra*; a point mass $\delta_h$ is unitary because $\delta_h^* = \delta_{h^{-1}}$. $\square$

**Theorem (involution).** The reflection $\rho_u$ is an involution, $\rho_u^2 = \mathrm{id}$, if and only if $u$ is a reflector, $u*\alpha(u)\in Z(\mathcal{A})$, and then its fixed set is the closed subalgebra $\{f : u*\alpha(f) = f*u\}$.

**Proof.** This is the reflection theorem of *The Signed Sandwich on the Group Algebra*, restated: $\rho_u^2 = c_{u*\alpha(u)}$ and the inner automorphism $c_t$ is the identity exactly when $t$ is central; the fixed set is the solution set of the continuous linear equation $u*\alpha(f) = f*u$. $\square$

**Corollary (independence of the three).** The self-adjointness, the unitarity and the involution of $\rho_u$ are independent conditions: a reflection may be self-adjoint without being an involution (when $\alpha(u^*)^{-1}u$ is central but $u*\alpha(u)$ is not), an involution without being self-adjoint, and unitary without either.

**Proof.** The three criteria involve the three independent elements $\alpha(u^*)^{-1}u$, $u^*u$ and $u*\alpha(u)$; for suitable choices of $\alpha$ and $u$ each condition can be imposed while the others fail, for instance with $\alpha = \mathrm{id}$ and $u$ a unit that is neither central nor unitary. $\square$

## The Reflection and the Composite Involution

**Theorem (the composite involution and the fixed subgroup).** The composite $\sigma = \alpha\circ\,^*$ is an anti-automorphism of order two, an automorphism exactly when the grade involution is a sign character, and on the group it is the continuous involution $\sigma = \alpha\iota$; the self-adjoint reflections are those with $u^{-1}\sigma(u)$ central, and the unitarity of the reflection is the unitarity of $u$ alone. When $\alpha$ is the sign character and $u = \delta_h$ with $h$ in the fixed subgroup of $\sigma$, the reflection is self-adjoint and its parameter $\sigma(h) = h$ is fixed.

**Proof.** $\sigma^2 = \alpha\,^*\alpha\,^* = \alpha\alpha\,^*\,^* = \mathrm{id}$ because $\alpha$ commutes with the involution; $\sigma$ is an anti-automorphism as the composite of an automorphism and an anti-automorphism, and a genuine automorphism when $\alpha$ is a sign character, which is central. On point masses $\sigma(\delta_h) = \alpha(\delta_{h^{-1}}) = \delta_{\alpha(h)^{-1}}$, the continuous involution $\sigma = \alpha\iota$; the fixed subgroup makes the self-adjointness condition $h^{-1}\sigma(h) = 1$ hold. $\square$

## The Degenerate Cases

**Proposition (the trivial and inner grade involutions).** If $\alpha = \mathrm{id}$ then $\rho_u = c_u$ is the inner automorphism and $\rho_u^* = c_{u^*} = \rho_{u^*}$: its adjoint is the conjugation by $u^*$, it is self-adjoint exactly when $u^{-1}u^* $ is central, and it is unitary exactly when $u$ is unitary. If $\alpha = c_z$ is inner then $\rho_u = c_{u*\alpha(u)^{-1}}$-transport of an inner automorphism, the adjoint is the reflection in $\alpha(u^*)$, and the reflection is inner in every case; only the self-adjointness criterion survives unchanged.

**Proof.** For $\alpha = \mathrm{id}$, $\rho_u = S_{u,u^{-1}} = c_u$ and the adjoint formula gives $c_u^* = c_{u^*}$; the criteria specialise the three theorems. For $\alpha = c_z$, $\rho_u(f) = u*z*f*z^{-1}*u^{-1} = c_{u*z}(f)$, an inner automorphism, and the adjoint formula is the general one applied to the inner twist. $\square$

**Remark (what the article does not do).** The signed adjoint of the left multiplication is the next article; the adjoint of a convolution operator, its form on $L^p$ and the involutive algebra it generates are *The Adjoint of a Convolution Operator*; the discrete version with the bilinear forms, where the reflection adjoint is $\rho_u^\dagger = \rho_{u^{-1}\sigma(u)}$ and the involution it defines is $\varepsilon T\varepsilon = \alpha T\alpha$, is *The Signed Adjoint of the Reflection on a Topological Group*, and the two are reconciled through the passage from the bilinear form to the Haar pairing by the involution $u\mapsto u^*$. The grade involution is an automorphism and the involution an anti-automorphism; the composite $\sigma$ is what the self-adjointness of a reflection detects.

## Summary

The reflection $\rho_u(f) = u*\alpha(f)*u^{-1} = S_{u,u^{-1}}$ has adjoint $\rho_u^* = S_{\alpha(u^*),\alpha(u^*)^{-1}} = \rho_{\alpha(u^*)} = \rho_{\sigma(u)}$ with respect to the Haar pairing, where $\sigma = \alpha\circ\,^*$ is the composite anti-automorphism; the adjoint is an involution on the reflection family and carries reflectors to reflectors. The three properties of a reflection are decided independently: it is self-adjoint exactly when $\sigma(u) = \alpha(u^*)$ and $u$ differ by a central unit, unitary exactly when the element $u$ is unitary, and an involution exactly when $u$ is a reflector, $u*\alpha(u)$ central; a reflection may have any combination of the three. On the group, $\sigma$ is the continuous involution $\alpha\iota$ of *Involutive Topological Groups* and self-adjointness is the condition that $u$ and $\sigma(u)$ agree modulo the centre, so that the fixed subgroup of $\sigma$ produces the self-adjoint reflections. When the grade involution is trivial the reflection is the inner automorphism $c_u$ with adjoint $c_{u^*}$, and when it is inner the reflection is inner and only the self-adjointness criterion is unchanged. The discrete version, with the bilinear signed form, is the neighbouring Part II article.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\rho_u(f) = u*\alpha(f)*u^{-1} = S_{u,u^{-1}}$ | The reflection determined by $u$ |
| $\rho_u^2 = c_{u*\alpha(u)}$ | The square of a reflection |
| $\sigma = \alpha\circ\,^*$, $\sigma(u) = \alpha(u^*)$ | The composite anti-automorphism |
| $(\rho_u)^* = \rho_{\alpha(u^*)}$ | The adjoint of a reflection |
| $\alpha(u^*)^{-1}u\in Z^\times$ | Self-adjointness criterion |
| $u^*u = 1$ | Unitarity criterion |
| $u*\alpha(u)\in Z(\mathcal{A})$ | The reflector condition, involution criterion |
| $\sigma = \alpha\iota$ | The continuous involution on the group |

## Further Reading

- Rudolf Schatten, *Norm Ideals of Completely Continuous Operators* (Springer, 1960), for self-adjoint and unitary operators and their parametrisation.
- Jacques Dixmier, *Von Neumann Algebras* (North-Holland, 1981), for the involutive algebra structure of the group algebra and the inner automorphisms.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for the composite of an automorphism and an involution and the fixed subgroup.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras I* (Academic Press, 1983), for self-adjointness, unitarity and the inner automorphisms of an operator algebra.
- Edwin Hewitt and Kenneth A. Ross, *Abstract Harmonic Analysis II* (Springer, 1970), for the reflections of the group algebra and the conjugation by the point masses.
