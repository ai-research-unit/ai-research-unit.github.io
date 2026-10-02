
# __Involutive Valued Fields__

## Introduction

A valued field with an involution is a valued field together with an order-two operator that reverses the multiplication; on a commutative field, which is the case of a field, it is simply an order-two automorphism, and it is the conjugation of the model field $\mathbb{C}$ and of the quadratic extensions of $\mathbb{Q}_p$. The involution interacts with the valuation in one of two ways: it preserves the absolute value — it is **isometric** — and then it preserves the valuation ring and the maximal ideal and induces an involution of the residue field, or it does not, and then it does not even preserve the valuation ring. This article treats involutive valued fields: it fixes the compatibility of the involution with the valuation, shows that an isometric involution preserves the entire valuation filtration and induces a residue involution, computes the fixed field and its degree over the base, treats the norm form and its interaction with ramification, and reads the whole structure through the completion, where the isometric involution extends by the general theorem on the involution and the completion.

The article assumes the absolute value, the valuation, the valuation ring $\mathcal{O}$, the maximal ideal $\mathrm{M}$, the residue field $k$, the value group $\Gamma$ and the extension of the valuation to a finite extension from *Absolute Values, Valuations and Completions*; the residue operator and its commutation with the completion from *The Residue Operator of a Valued Field*; the involution, its fixed subring and its skew subgroup from *Involutive Rings*; the continuity and the fixed set of a continuous involution from *Involutive Topological Rings and Fields*; and the extension of a continuous involution to the completion with the same fixed part up to closure from *The Involution and the Completion of a Ring*. The structure of a local field, its ramification index and residue degree, Hensel's lemma and the maximal unramified extension are *Local Fields*, and are named only where they are used. No measure, no norm and no form beyond the valuation occurs.

Throughout, $(F, \lvert \cdot \rvert)$ is a valued field with valuation $v$, value group $\Gamma$, valuation ring $\mathcal{O}$, maximal ideal $\mathrm{M}$ and residue field $k = \mathcal{O}/\mathrm{M}$; $\sigma$ is an **involution** of $F$, that is an order-two map with $\sigma(x + y) = \sigma(x)+\sigma(y)$ and $\sigma(xy) = \sigma(y)\sigma(x)$; the fixed field is $F^\sigma = \{x : \sigma(x) = x\}$; the **norm form** is $N(x) = x\,\sigma(x)$; the completion is $\widehat{F}$.

## The Isometric Involution

**Definition.** An involution $\sigma$ of the valued field $(F, \lvert \cdot \rvert)$ is **isometric** if $\lvert \sigma(x)\rvert = \lvert x\rvert$ for all $x$, equivalently $v(\sigma(x)) = v(x)$. The **associated absolute value** is $\lvert x\rvert_\sigma = \lvert\sigma(x)\rvert$, which is another absolute value on $F$.

**Proposition (isometric is the same as valuation-preserving).** For an involution $\sigma$ the following are equivalent: $\sigma$ is isometric; $\sigma(\mathcal{O}) = \mathcal{O}$; $\sigma(\mathrm{M}) = \mathrm{M}$; $\sigma$ preserves every ideal $\mathrm{M}_\gamma = \{x : v(x)\geq\gamma\}$; and $\sigma$ is continuous for the valuation topology.

**Proof.** Isometry gives $\lvert\sigma(x)\rvert = \lvert x\rvert$, so $\sigma$ preserves the unit ball $\mathcal{O}$ and the open unit ball $\mathrm{M}$; conversely, the sets $\{\lvert x\rvert \leq r\}$ are determined by $\mathcal{O}$ and the scalings, so preserving $\mathcal{O}$ and $\mathrm{M}$ recovers the value on every element: $v(\sigma(x))$ is the supremum of the $\gamma$ with $\sigma(x)\in\mathrm{M}_\gamma$, and $\sigma(\mathrm{M}_\gamma) = \mathrm{M}_\gamma$ by inversion and scaling. Continuity of an additive map is the continuity at $0$, that is the preservation of a neighbourhood of $0$, which is $\mathrm{M}$ being carried into itself.

**Proposition (the involution extends to the completion).** An isometric involution is continuous, hence uniformly continuous for the additive uniformity, and extends uniquely to a continuous involution $\widehat\sigma$ of the completion $\widehat{F}$ with $\widehat\sigma\iota = \iota\sigma$; the extension is isometric for the extended valuation, and $\lvert \cdot \rvert_\sigma$ extends to an absolute value equivalent to $\lvert \cdot \rvert$ on $\widehat{F}$.

**Proof.** Continuity is the previous proposition; the extension is *The Involution and the Completion of a Ring*. The isometry of the extension holds on the dense image and passes to the limit by continuity of the absolute value; the two absolute values $\lvert \cdot \rvert$ and $\lvert \cdot \rvert_\sigma$ agree on $F$ when $\sigma$ is isometric, hence are equivalent, and both extend to the completion.

## The Fixed Field

**Theorem (the fixed field is a subfield of index at most two).** Let $\sigma$ be a nontrivial involution of $F$. Then the fixed set $F^\sigma$ is a subfield of $F$ and $[F : F^\sigma] = 2$; the extension is Galois with group $\{1, \sigma\}$, the norm form $N(x) = x\sigma(x)$ takes values in $F^\sigma$, and $F$ is a quadratic extension of $F^\sigma$ generated by any $x \notin F^\sigma$ satisfying $\sigma(x) = -x$ when such an $x$ exists.

**Proof.** The fixed set of an involution is a subfield, being the equalizer of two field automorphisms. For $x \notin F^\sigma$ the elements $x + \sigma(x)$ and $x\sigma(x) = N(x)$ lie in $F^\sigma$, so $x$ satisfies the quadratic equation $T^2 - (x+\sigma(x))T + N(x) = 0$ over $F^\sigma$; hence $[F : F^\sigma]\leq 2$ and, since $\sigma$ is nontrivial, the degree is exactly $2$. The extension is separable in characteristic other than $2$; in characteristic $2$ the equation reads $T^2 + (x+\sigma(x))T + N(x) = 0$, so the extension is Artin–Schreier, generated by an element $\theta$ with $\theta^2 + \theta = x^2+x\in F^\sigma$ and trace $\theta + \sigma(\theta) = 1$, and the inseparable case cannot occur because an inseparable quadratic extension has no nontrivial automorphism. The norm takes values in $F^\sigma$ because $\sigma(N(x)) = \sigma(x)\sigma^2(x) = N(x)$.

**Corollary (the trace and the norm).** The maps $x\mapsto x + \sigma(x)$ and $x\mapsto x\sigma(x)$ are the trace and the norm of the quadratic extension $F/F^\sigma$; the trace is a surjective $F^\sigma$-linear map and the norm is a surjective homomorphism $F^\times\to (F^\sigma)^\times$ when the extension is separable, and the norm form is multiplicative, $N(xy) = N(x)N(y)$.

**Proof.** They are the standard trace and norm of a Galois extension of group $\{1,\sigma\}$; the multiplicativity of the norm is $\sigma(xy) = \sigma(y)\sigma(x) = \sigma(x)\sigma(y)$ for a commutative field. Surjectivity of the norm is Hilbert's theorem 90 applied to the cyclic extension, or the standard computation.

## The Residue Involution

**Theorem (the residue involution).** An isometric involution $\sigma$ induces a well-defined involution $\bar\sigma$ of the residue field,

$$
\bar\sigma : k\longrightarrow k, \qquad \bar\sigma(x + \mathrm{M}) = \sigma(x) + \mathrm{M} ,
$$

which is again an order-two anti-automorphism (an automorphism when $k$ is commutative, which is the field case); it is the identity exactly when $\sigma$ acts trivially on the residue field, and the residue field of the fixed field embeds in the fixed field of the residue involution.

**Proof.** Because $\sigma(\mathrm{M}) = \mathrm{M}$ the map is well defined on classes; it is additive and reverses products because $\sigma$ does, and $\bar\sigma^2 = \mathrm{id}$ because $\sigma^2 = \mathrm{id}$. It is the identity exactly when $\sigma(x) - x \in \mathrm{M}$ for all $x$, that is when $\sigma$ acts trivially modulo $\mathrm{M}$. The residue field $k_{F^\sigma}$ of the fixed field consists of classes represented by elements of $F^\sigma$, on which $\bar\sigma$ is the identity, so $k_{F^\sigma}\subseteq k^{\bar\sigma}$.

**Corollary (the residue involution and the valuation filtration).** The isometric involution acts on each quotient $\mathrm{M}^n/\mathrm{M}^{n+1}$ as the identity when it acts as the identity on $k$; in general it acts by $\bar\sigma$ on $\mathrm{M}^n/\mathrm{M}^{n+1}\cong k$, so the whole associated graded ring $\bigoplus_n \mathrm{M}^n/\mathrm{M}^{n+1}$ carries the induced involution.

**Proof.** The quotients $\mathrm{M}^n/\mathrm{M}^{n+1}$ are $k$-modules isomorphic to $k$; an isometric involution preserves each $\mathrm{M}^n$ and induces $\bar\sigma$ on each quotient, because the action on classes is $\bar\sigma$ by multiplicativity.

## The Norm Form and Ramification

**Proposition (the norm form and the value).** For $x \in F$ the norm form satisfies $v(N(x)) = 2\,v(x)$; hence $N(x)$ is a unit of $\mathcal{O}$ exactly when $x$ is, and $N(x)\in \mathrm{M}^n$ exactly when $v(x)\geq n/2$. The norm form is isotropic on the skew part and anisotropic on the fixed field; the **unitary group** $U(F,\sigma) = \{x : N(x) = 1\}$ is the group of norm-one elements.

**Proof.** $v(N(x)) = v(x\sigma(x)) = v(x)+v(\sigma(x)) = 2v(x)$ by the isometry; the level statements follow. The norm form vanishes at skew elements because $N(x) = x\sigma(x) = -x^2$ when $\sigma(x) = -x$; on the fixed field it is $x^2$, which vanishes only at $0$. The unitary group is the kernel of the norm on the units.

**Theorem (ramification of the quadratic extension).** Let $\sigma$ be a nontrivial isometric involution of the discretely valued field $F$ with $F^\sigma$ its fixed field and $[F : F^\sigma] = 2$. Then the extension $F/F^\sigma$ has ramification index $e$ and residue degree $f$ with $ef = 2$, so exactly one of the following holds: the extension is **unramified**, $e = 1$, $f = 2$, and the residue involution $\bar\sigma$ is nontrivial; or the extension is **ramified**, $e = 2$, $f = 1$, and the residue involution $\bar\sigma$ is trivial. In the unramified case the residue involution is the nontrivial automorphism of the quadratic residue extension, and in the ramified case it is the identity.

**Proof.** For a quadratic extension $ef = [F : F^\sigma] = 2$, so $(e, f)$ is $(1, 2)$ or $(2, 1)$. The residue field of $F^\sigma$ is a subfield of $k$ of degree $f$ over it, being the residue field of the base; $\bar\sigma$ acts on $k$ and its fixed field is the residue field of the fixed field by the theorem above, so $\bar\sigma$ is nontrivial exactly when $f = 2$, that is in the unramified case, and trivial when $f = 1$, that is in the ramified case. The statements about the residue involution follow.

**Remark (the ramification index and the norm form).** In the ramified case a uniformiser $\pi$ of $F$ has $v(\pi) = \tfrac12 v(\pi_{F^\sigma})$ for a uniformiser $\pi_{F^\sigma}$ of the fixed field, so the norm form of a uniformiser is a uniformiser of the fixed field, $N(\pi) = \pi\sigma(\pi)$ with $\sigma(\pi) = -\pi$ up to a unit, giving $v(N(\pi)) = 2v(\pi) = v(\pi_{F^\sigma})$; in the unramified case the norm of a uniformiser is a unit of the fixed field. This is the arithmetical content of the norm form and belongs with *Involutive Local Fields*, where the local field case is treated.

## The Completion

**Theorem (the involutive valued field and its completion).** An isometric involution $\sigma$ of a valued field $F$ extends to an isometric involution $\widehat\sigma$ of the completion $\widehat{F}$; $\widehat{F}$ is an involutive valued field with the same value group and the same residue field, the fixed field of $\widehat\sigma$ is the completion of the fixed field, $\widehat{F}^{\widehat\sigma} = \widehat{F^\sigma}$, for the restriction of the valuation, and the residue involution of the completion is the residue involution of $F$, $\overline{\widehat\sigma} = \bar\sigma$ under the identification $k_{\widehat{F}} = k$.

**Proof.** The extension is *The Involution and the Completion of a Ring* and the isometry is the continuity of the absolute value; the value group and residue field of the completion are those of the field by *The Residue Operator of a Valued Field* and *The Valuation Operator*; the fixed field of the completion is the closure of the image of the fixed field, which for the restriction of the valuation is the completion of the fixed field because $F^\sigma$ is closed in $F$ and carries the induced valuation, so its completion embeds as the closure. The residue involution is determined on the dense image and is the same map on $k$.

**Corollary (Henselian case).** When $F$ is Henselian the fixed field $F^\sigma$ is Henselian for the restricted valuation, and the residue involution lifts through the Teichmüller section; these are the statements of *Local Fields* and are named, not proved.

**Proof.** The Henselian property of the fixed field is the standard permanence of Hensel's lemma under the fixed field of an isometric involution, quoted.

## Examples

**Example ($\mathbb{C}$ and the conjugation).** On $\mathbb{C}$ with the usual absolute value, the conjugation is an isometric involution with fixed field $\mathbb{R}$ of index two; it is Archimedean, so the residue field is trivial and the residue involution is the identity; it is the model of a nontrivial isometric involution.

**Example ($\mathbb{Q}_p(\sqrt{u})$ unramified).** For $p$ odd and $u$ a unit which is not a square, the extension $\mathbb{Q}_p(\sqrt u)$ is unramified of degree two and the nontrivial automorphism $\sqrt u\mapsto -\sqrt u$ is isometric; the residue involution is the nontrivial involution of $\mathbb{F}_{p^2}$, that is the Frobenius $x\mapsto x^p$; the fixed field is $\mathbb{Q}_p$ and the extension is unramified.

**Example ($\mathbb{Q}_p(\sqrt{p})$ ramified).** The extension is ramified of degree two and the automorphism is isometric; the residue involution is the identity on $\mathbb{F}_p$, and the norm form of the uniformiser $\sqrt p$ is $-p$, a uniformiser of $\mathbb{Q}_p$; the fixed field is $\mathbb{Q}_p$ and the extension is ramified.

**Example ($k((t))$ with $t\mapsto t^{-1}$).** On the local field $k((t))$ the map $t\mapsto t^{-1}$ is an order-two automorphism; it is not isometric for the usual valuation, because $v(t^{-1}) = -v(t)$ changes the sign, and it does not preserve the valuation ring; the fixed field is $k(t + t^{-1})$, and this is the standard example of an involution that fails to be isometric, so that the residue involution is not defined.

## Summary

An involution of a valued field is isometric when it preserves the absolute value, equivalently the valuation ring and the maximal ideal, equivalently the whole valuation filtration, equivalently continuity for the valuation topology; an isometric involution extends to the completion and induces an involution $\bar\sigma$ of the residue field, the **residue involution**. A nontrivial involution has fixed field of index two, $[F : F^\sigma] = 2$, with trace $x + \sigma(x)$ and norm form $N(x) = x\sigma(x)$, the norm being multiplicative and satisfying $v(N(x)) = 2v(x)$; the unitary group is the norm-one group. For a discretely valued field the quadratic extension $F/F^\sigma$ is either unramified, $e = 1$, $f = 2$, with nontrivial residue involution, or ramified, $e = 2$, $f = 1$, with trivial residue involution, and the norm of a uniformiser is a unit in the unramified case and a uniformiser in the ramified case.

Under completion the whole structure is preserved: the value group and the residue field are unchanged, the isometric involution extends isometrically, the fixed field completes to the fixed field of the completion, and the residue involution of the completion is the residue involution of the field; when the field is Henselian the fixed field is Henselian and the residue involution lifts, these being the statements of the local theory. An involution that is not isometric, such as $t\mapsto t^{-1}$ on $k((t))$, does not preserve the valuation ring and has no residue involution, which is the boundary of the theory.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(F, v, \lvert \cdot \rvert)$ | The valued field |
| $\mathcal{O}$, $\mathrm{M}$, $k$, $\Gamma$ | Valuation ring, maximal ideal, residue field, value group |
| $\sigma$ | The involution, order two |
| $\lvert \cdot \rvert_\sigma = \lvert\sigma(\cdot)\rvert$ | The associated absolute value |
| Isometric | $v(\sigma(x)) = v(x)$; $\sigma(\mathcal{O}) = \mathcal{O}$; continuity |
| $F^\sigma$ | The fixed field, $[F : F^\sigma]\leq 2$ |
| $N(x) = x\sigma(x)$, $v(N(x)) = 2v(x)$ | The norm form |
| $\bar\sigma$ | The residue involution of $k$ |
| $U(F,\sigma)$ | The unitary group, $N(x) = 1$ |
| $ef = 2$ | Unramified $(1,2)$ or ramified $(2,1)$ |
| $\widehat{F}^{\widehat\sigma} = \widehat{F^\sigma}$ | The fixed field is preserved by completion |

## Further Reading

- Jean-Pierre Serre, *Local Fields* (Springer, 1979), for quadratic extensions, ramification, the residue field and the norm form.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for involutions of fields and their norm forms.
- Seth Warner, *Topological Fields* (North-Holland, 1989), for isometric involutions and the valuation topology.
- Jürgen Neukirch, *Algebraic Number Theory* (Springer, 1999), for valuations, their extensions and the ramification of quadratic extensions.
- Wim H. Schikhof, *Ultrametric Calculus* (Cambridge University Press, 1984), for the norm form and the structure of a valued field of characteristic zero.
