
# __Reflections as Signed Two-Sided Operators on a Topological Ring__

## Introduction

A **reflection** of an object carrying a grade involution is an involutive signed two-sided operator: an element acts on $x$ by sending it to $u\,\alpha(x)\,u^{-1}$, and the operator so obtained is an involution exactly when $u\alpha(u)$ is central. The elements of the object are therefore matched with the reflections that invert them, and the match — the **correspondence between the elements and the reflections** — is a bijection up to the units inducing the grade involution when the grade involution is not inner, and loses injectivity in the degenerate cases. This article treats the reflections of a topological ring as signed two-sided operators: it fixes the reflection attached to a unit, computes when it is an involution and what it fixes, states the correspondence with the carrying elements together with its kernel, and works out the degenerate cases — the inner grade involution and the commutative ring — where the correspondence collapses, with the topological gain that the reflections are continuous, the fixed subrings are closed and the correspondence is a homeomorphism onto its image up to the kernel.

The article assumes the signed sandwich, its composition law, the signed sandwich group and the signed conjugations from *The Signed Sandwich on a Topological Ring*; the correspondence between the reflections and the elements acting by an involution, and its failure, from *Reflections as Signed Two-Sided Operators on a Ring*; the same correspondence on a group, treated in parallel, from *Reflections as Signed Two-Sided Operators on a Topological Group*; the grade involution, its fixed and skew parts and the geometric reading from *The Grade Involution* and *The Signed Sandwich on a Ring*; the operator layer, the inner automorphisms $c_u$, the homeomorphisms and the closed fixed sets from *Operators on a Topological Ring*; and the continuous grade involution, the closedness of the fixed set and the relation to the anti-automorphic involution from *Involutive Topological Rings and Fields*. The adjoints of the reflections are *The Signed Adjoint of the Reflection on a Topological Ring*, later in this category, and are not used here. No measure, no norm and no form occurs.

Throughout, $R$ is a topological ring, unital and Hausdorff, with grade involution $\alpha$, assumed continuous, group of units $R^\times$, centre $Z(R)$ and inner automorphisms $c_u(x) = uxu^{-1}$; the signed conjugation carried by a unit $u$ is

$$
\rho_u = \Sigma^\alpha_{u,u^{-1}} : R \longrightarrow R, \qquad \rho_u(x) = u\,\alpha(x)\,u^{-1} ,
$$

and the set of **carrying units** is $I_\alpha(R) = \{ u \in R^\times : u\alpha(u) \in Z(R) \}$, the units whose signed conjugation is an involution.

## Reflections

**Definition.** A **reflection** of $R$ is an operator of the form $\rho_u$ that is an involution, that is a signed conjugation with $u \in I_\alpha(R)$. The unit $u$ is the **carrying unit** of the reflection, and the reflection is said to **invert** the elements $x$ with $\rho_u(x) = -x$ and to **fix** those with $\rho_u(x) = x$.

**Proposition (reflections are continuous involutions with closed fixed set).** For $u \in I_\alpha(R)$ the operator $\rho_u$ is a continuous additive operator, $\rho_u^2 = \mathrm{id}$, it is a homeomorphism of $R$ with $\rho_u^{-1} = \rho_u$, and its fixed set is the closed subring

$$
R^{\rho_u} = \{ x : \alpha(x) = u^{-1}xu \} = \{ x : \alpha(x) = c_{u^{-1}}(x) \} ,
$$

which contains the fixed subring $R^\alpha \cap Z(R)$ of the grade involution.

**Proof.** The operator $\rho_u = L_u\alpha R_{u^{-1}}$ is a composite of continuous operators, hence continuous, and additive; its square is $c_{u\alpha(u)}$, the identity when $u\alpha(u)$ is central, by *The Signed Sandwich on a Topological Ring*. The fixed set is the equalizer of the two continuous maps $\alpha$ and $c_{u^{-1}}$, hence closed, and it is a subring because both maps are automorphisms; an element of $R^\alpha\cap Z(R)$ satisfies $\alpha(x) = x = u^{-1}xu$, so it is fixed.

**Proposition (the associated inner automorphism).** The reflection is the composite of the grade involution with an inner automorphism in two ways,

$$
\rho_u = c_u\circ\alpha = \alpha\circ c_{\alpha(u)} ,
$$

and its composites with the grade involution are the inner automorphisms

$$
\rho_u\circ\alpha = c_u , \qquad \alpha\circ\rho_u = c_{\alpha(u)} .
$$

So the reflection differs from the inner automorphism $c_u$ exactly by the grade involution, and $\rho_u$ is an involution precisely when $c_{u\alpha(u)} = \mathrm{id}$.

**Proof.** $\rho_u(x) = u\alpha(x)u^{-1} = c_u(\alpha(x))$, so $\rho_u = c_u\alpha$; and $\alpha(\alpha(u)x\alpha(u)^{-1}) = u\alpha(x)u^{-1}$, so $c_u\alpha = \alpha c_{\alpha(u)}$. Composing with $\alpha$ gives $\rho_u\alpha = c_u\alpha^2 = c_u$ and $\alpha\rho_u = \alpha c_u\alpha = c_{\alpha(u)}$. The involution condition is $\rho_u^2 = c_{u\alpha(u)}$ from the square computation.

**Remark (the distinction from the involution of the theory group).** The **involution** of the `- * Theory` group is an anti-automorphism $\sigma$ of order two, and its fixed set is a subring; the reflection here is an automorphism, the composite of the grade involution with an inner automorphism, and its fixed set is the subring on which the grade involution agrees with the inner automorphism. The two constructions both produce involutive operators and both have closed fixed sets, and they are different operators: $\sigma$ reverses the product, $\rho_u$ preserves it. They meet in *Involutive Topological Rings and Fields*, where the anti-automorphism is the object.

## The Correspondence

**Theorem (the correspondence between the elements and the reflections).** The map

$$
I_\alpha(R) \longrightarrow \{\text{reflections of } R\}, \qquad u \longmapsto \rho_u ,
$$

is surjective by definition, and its kernel is the set of units inducing the grade involution,

$$
\{ u \in R^\times : \rho_u = \mathrm{id} \} = \{ u \in R^\times : c_u = \alpha \} ,
$$

which is trivial when $\alpha$ is not inner. Hence the reflections of $R$ are in bijection with the carrying units modulo this kernel: with $R^\times$ when $\alpha$ is not inner, and with the cosets of the central units when $\alpha$ is inner.

**Proof.** $\rho_u = \mathrm{id}$ is $u\alpha(x)u^{-1} = x$ for all $x$, that is $c_u = \alpha$, by the computation of the kernel of the sandwich map in *The Signed Sandwich on a Topological Ring*. When $\alpha$ is not inner, $c_u = \alpha$ for no unit $u$, so the kernel is trivial; when $\alpha = c_z$ is inner, $c_u = c_z$ exactly when $u z^{-1}$ is central, so the kernel is the coset $z\,(Z(R)\cap R^\times)$.

**Corollary (the reflection attached to a unit).** Assigning to a unit $u$ with $u\alpha(u)$ central the reflection $\rho_u$ is the map that carries the element $u$ to the operator inverting the elements $x$ with $u\alpha(x)u^{-1} = -x$; the reflection is uniquely determined by the coset $u\{a : c_a = \alpha\}$, and the assignment is injective exactly when the grade involution is not inner.

**Proof.** Immediate from the theorem; the inversion condition is $\rho_u(x) = -x$, which is $u\alpha(x)u^{-1} = -x$.

**Proposition (the reflections compose).** For carrying units $u, v$ the product of the reflections is the reflection carried by $u\alpha(v)$,

$$
\rho_u\circ\rho_v = \rho_{u\alpha(v)} ,
$$

and the reflections form a subgroup of the signed sandwich group when the grade involution is not inner, namely the image of $I_\alpha(R)$ under $u \mapsto \rho_u$, a homomorphic image of the carrying units in which $u$ acts through the automorphism $\alpha$; every reflection lies in the continuous automorphism group $\operatorname{Aut}_c(R)$.

**Proof.** By the composition law, $\rho_u\rho_v = \Sigma^\alpha_{u\alpha(v),\,\alpha(v^{-1})u^{-1}}$, and for $t = u\alpha(v)$ the right parameter is $\alpha(v)^{-1}u^{-1} = (u\alpha(v))^{-1} = t^{-1}$, so the product is $\Sigma^\alpha_{t,t^{-1}} = \rho_t$. The product of two carrying units is again carrying when $\alpha$ is not inner, and in general the image is a subgroup of the sandwich group by the homomorphism property; each reflection is an automorphism and continuous.

## The Degenerate Cases

The correspondence is a bijection in the generic case and loses injectivity or content in the degenerate ones.

**Theorem (the inner grade involution).** If the grade involution is inner, $\alpha = c_z$ with $z \in R^\times$, then every reflection is an unsigned conjugation,

$$
\rho_u(x) = u z x z^{-1}u^{-1} = (uz)x(uz)^{-1} = c_{uz}(x) ,
$$

the reflections coincide with the inner automorphisms that are involutions, and the correspondence $u \mapsto \rho_u$ has kernel the central units, so it loses injectivity already on the level of the units. In particular when the ring is commutative with $\alpha$ inner, and hence $\alpha = \mathrm{id}$, every reflection is the identity and the reflection group is trivial.

**Proof.** For $\alpha = c_z$, $\rho_u = c_u c_z = c_{uz}$, so the reflections are the inner automorphisms $c_{uz}$ that are involutions, that is those with $(uz)^2$ central; the kernel is $\{u : c_u = c_z\} = z(Z(R)\cap R^\times)$. A commutative ring has every inner automorphism trivial, so $\alpha = \mathrm{id}$ and $\rho_u = \mathrm{id}$ for all $u$, and the reflection group is trivial.

**Theorem (the commutative ring).** If $R$ is commutative then for every unit $u$ one has $\rho_u = \alpha$, independently of $u$; the reflection group is the two-element group $\{\mathrm{id}, \alpha\}$ when $\alpha \neq \mathrm{id}$ and is trivial when $\alpha = \mathrm{id}$, and the correspondence is maximally degenerate: every carrying unit gives the same reflection $\alpha$.

**Proof.** In a commutative ring $u\alpha(x)u^{-1} = \alpha(x)$, so $\rho_u = \alpha$ for all units $u$; the involution condition $u\alpha(u)$ central is automatic because the ring is commutative, so every unit is a carrying unit, and all are mapped to the same operator. The reflection group is generated by $\alpha$, which has order two when nontrivial and is the identity otherwise.

**Theorem (the failure of injectivity and the cosets).** The correspondence $u \mapsto \rho_u$ fails to be injective exactly when the grade involution is inner; in that case the kernel is the coset $z(Z(R)\cap R^\times)$, and the reflections are the cosets of the central units in the carrying units. If $\alpha$ is not inner, the reflections are in bijection with the carrying units and two distinct carrying units give distinct reflections, except in the commutative case, where all give the same reflection.

**Proof.** Combine the kernel theorem with the two degeneracy theorems. The only overlap is non-empty exactly when $c_u = \alpha$ for some unit, which is the inner case; the commutative case is the extreme of the inner case with $z = 1$.

**Remark (the failure on one side).** Even when $\alpha$ is not inner and the ring is noncommutative, the correspondence can fail to be onto the involutions: a continuous automorphism of order two of $R$ that is not of the form $\rho_u$ is a reflection in the geometric sense but is not a signed conjugation, and it is not in the image. The correspondence is between the elements and the reflections that they carry, not between the elements and all the involutive automorphisms of $R$.

## The Topological Reading

**Proposition (the reflections are continuous and their fixed sets closed).** With $\alpha$ continuous, every reflection is a continuous automorphism of $R$, hence a homeomorphism; its fixed subring is closed; the subset $I_\alpha(R)$ of carrying units is closed in $R^\times$ when $R^\times$ is open, being the preimage of the centre under $u \mapsto u\alpha(u)$; and the map $u \mapsto \rho_u$ is continuous for the topology of pointwise convergence, so it is a homeomorphism onto its image up to the kernel.

**Proof.** Continuity and the closedness of the fixed subring are the first proposition; $I_\alpha(R)$ is the preimage of $Z(R)$ under the continuous map $u \mapsto u\alpha(u)$ restricted to the open $R^\times$, hence closed when $R^\times$ is open and $Z(R)$ is closed, which holds on a Hausdorff ring for the centre of a unital ring that is its own centraliser. The continuity of $u \mapsto \rho_u$ follows from the continuity of the ring operations and of $\alpha$.

**Corollary (the reflection group is a topological group).** The group generated by the reflections, modulo the kernel of the correspondence, is a topological group for the topology of pointwise convergence; when $R^\times$ is open it is a quotient of the topological group $I_\alpha(R)$, and on the generic case it is a continuous image of the topological group of carrying units.

**Proof.** A quotient of a topological group by a closed normal subgroup is a topological group; the kernel is closed by the previous proposition, and the generating set is a continuous image.

**Remark (the boundary to the adjoints and to the involution).** The adjoint of a reflection with respect to the form of the category, the unitarity condition it satisfies and its self-adjointness are *The Signed Adjoint of the Reflection on a Topological Ring*, later in this category; the involution of the `- * Theory` group and its fixed subring are *Involutive Topological Rings and Fields*; and the geometric realisation of the reflections as the elements of a quadratic space is the model in the Clifford algebra, named in *The Signed Sandwich on a Topological Ring* and not used here.

## Examples

**Example (the sign change on a polynomial ring).** On $k[x]$ with the grade involution $\alpha(f)(x) = f(-x)$, the reflection carried by $u = x$ is $\rho_x(f) = x f(-x) x^{-1}$ on the localisation at $x$; the ring is commutative, so $\rho_x = \alpha$ by the commutative theorem, and the reflection group is $\{\mathrm{id}, \alpha\}$; the fixed subring is the even polynomials.

**Example (the Clifford algebra of a quadratic space).** In the Clifford algebra $Cl(V, q)$ with the grade involution, the reflection carried by a vector $v$ with $q(v)\neq 0$ is $\rho_v(x) = v\alpha(x)v^{-1}$, and $v\alpha(v) = -q(v)$ is central, so $\rho_v$ is an involution; its fixed set is the hyperplane of $x$ with $vx = xv$, and the correspondence with the vectors is the geometric correspondence between the elements of $V$ and the reflections of the quadratic space.

**Example (the matrix ring with the transpose).** On $M_n(k)$ with the grade involution $\alpha(A) = A^{\top}$, the reflection carried by a unit $U$ is $\rho_U(A) = U A^{\top}U^{-1}$; it is an involution when $UA^{\top}$... precisely when $U\alpha(U) = U U^{\top}$ is central; the symmetric matrices $U = U^{\top}$ with $U^2$ central give the reflections, and the correspondence fails when $UU^{\top}$ is not central.

**Example (an inner grade involution).** On $M_n(k)\times M_n(k)$ with $\alpha(A,B) = (B,A)$, the grade involution is inner exactly when the two factors are conjugated by an invertible element; in that case every reflection is an inner automorphism by the inner theorem, so the signed reflection is not new, and the article's degenerate case is realised.

## Summary

A reflection of a topological ring with a continuous grade involution $\alpha$ is a signed conjugation $\rho_u(x) = u\alpha(x)u^{-1}$ with $u\alpha(u)$ central; it is a continuous involutive automorphism, a homeomorphism, and its fixed set is the closed subring $\{x : \alpha(x) = u^{-1}xu\}$. The reflections correspond to the carrying units $I_\alpha(R) = \{u : u\alpha(u) \in Z(R)\}$ modulo the units inducing the grade involution, $\{u : c_u = \alpha\}$, so the correspondence is a bijection with the carrying units when $\alpha$ is not inner and a bijection with the cosets of the central units when $\alpha$ is inner; the assignment is continuous for the pointwise topology and a homeomorphism onto its image up to the kernel.

The correspondence fails in the degenerate cases. When the grade involution is inner, $\alpha = c_z$, every reflection is the inner automorphism $c_{uz}$ and the kernel is the coset of the central units, so injectivity is lost on the level of the units; when the ring is commutative every unit gives the same reflection $\alpha$ and the reflection group is $\{\mathrm{id}, \alpha\}$, the maximal degeneration. When $\alpha$ is not inner and the ring is noncommutative the correspondence is injective but not onto the involutive automorphisms, since only the signed conjugations are reflections in this sense; the adjoints of the reflections and the anti-automorphic involution are the neighbouring articles.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\alpha$ | The continuous grade involution, an involutive automorphism |
| $\rho_u(x) = u\alpha(x)u^{-1}$ | The reflection carried by the unit $u$ |
| $I_\alpha(R) = \{u \in R^\times : u\alpha(u) \in Z(R)\}$ | The carrying units |
| $\rho_u^2 = c_{u\alpha(u)}$ | The square of a reflection, the identity on the carrying units |
| $R^{\rho_u} = \{x : \alpha(x) = u^{-1}xu\}$ | The closed fixed subring of the reflection |
| $\rho_u = c_u\alpha = \alpha c_{\alpha(u)}$ | The reflection as the grade involution with an inner automorphism |
| $\{u : c_u = \alpha\}$ | The kernel of the correspondence $u \mapsto \rho_u$ |
| $\alpha = c_z$ | The degenerate inner grade involution |
| $\{\mathrm{id}, \alpha\}$ | The reflection group of a commutative ring |
| $\sigma$ | The anti-automorphic involution of the `- * Theory` group, a different operator |

## Further Reading

- Nicolas Bourbaki, *Algebra I, Chapters 1–3* (Springer, 1998), for inner automorphisms and the structure of the automorphism group.
- Claude Chevalley, *The Algebraic Theory of Spinors and Clifford Algebras* (Springer, 1997; collected works), for the reflections of a quadratic space and their realisation in the Clifford algebra.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for involutions, their fixed subrings and the correspondence with elements.
- Tsi-Yuen Lam, *A First Course in Noncommutative Rings*, Graduate Texts in Mathematics 131 (Springer, 2nd ed. 2001), for when an automorphism is inner and the role of the centre.
- Seth Warner, *Topological Fields* (North-Holland, 1989), for the continuity of the automorphisms of a topological ring and the topology of pointwise convergence.
