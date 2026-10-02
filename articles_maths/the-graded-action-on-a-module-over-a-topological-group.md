
# __The Graded Action on a Module over a Topological Group__

## Introduction

A group with a grade involution acts on its modules with a sign, and the sign is the whole content of the word *graded*. The grade involution of the group extends linearly to an automorphism of the group algebra, whose eigenspaces make that algebra a $\mathbb{Z}/2$-graded algebra; a **graded module** is a module on which the graded algebra acts homogeneously, and the homogeneity is the sign rule: even elements of the group algebra preserve the grading of the module, odd elements reverse it, and the odd part of a group element is exactly what the sign can see. This article develops the graded action for a graded **topological** group, proves the equivalence of the two descriptions of a graded module, extracts the sign rule, and states the continuity hypothesis that the topology places on the action.

The article assumes the topological group and the continuity of the action by translation from *Topological Groups* and *Operators on a Topological Group*; the continuous involutive automorphism, the fixed subgroup and the dictionary of the fixed and inverted sets from *Involutive Topological Groups*; the group algebra and its linearisation of the translations from *Group Algebras*; and the graded algebra, its homogeneous components and the grading involution from *The Grading of an Algebra*. The graded action on an abstract group is *The Graded Action on a Module over a Group*; the adjoint action of the graded module is *The Graded Adjoint Action on a Module over a Topological Group*. A topological module over a topological ring, with continuous addition and scalar action, is *Topology on Linear Spaces*, later in this part; this article keeps the module on the discrete topology and names that theory once, at the boundary.

Throughout, $G$ is a topological group with identity $e$, $k$ is a field of characteristic different from two, $k[G]$ is the group algebra, $\alpha$ is a continuous involutive automorphism of $G$ — its grade involution — and $\sigma = \iota\alpha$ is the associated topological involution. A **graded $k$-module** is a $k$-module $M$ with a direct sum decomposition $M = M_{\bar0}\oplus M_{\bar1}$, whose elements are called **even** and **odd**.

## The Graded Group Algebra

**Definition.** The **grade involution of the group algebra** is the linear extension of $\alpha$ to a map $\bar\alpha : k[G]\to k[G]$, $\bar\alpha\bigl(\sum_g u_g g\bigr) = \sum_g u_g\,\alpha(g)$. The $\pm1$-eigenspaces of $\bar\alpha$ are

$$
k[G]_{\bar0} = \{u : \bar\alpha(u) = u\}, \qquad k[G]_{\bar1} = \{u : \bar\alpha(u) = -u\},
$$

the **even** and the **odd** parts of the group algebra.

**Theorem.** $\bar\alpha$ is an algebra automorphism of $k[G]$ with $\bar\alpha^2 = \mathrm{id}$, and $k[G] = k[G]_{\bar0}\oplus k[G]_{\bar1}$ with

$$
k[G]_i \cdot k[G]_j \subseteq k[G]_{\overline{i+j}} \qquad (i, j \in \{\bar0,\bar1\}),
$$

so that $k[G]$ is a $\mathbb{Z}/2$-graded algebra. The even part is a subalgebra, the odd part is a bimodule over it, the product of two odd elements is even, and $1 \in k[G]_{\bar0}$.

**Proof.** $\bar\alpha$ is linear and multiplicative because $\alpha$ is a group automorphism, and $\bar\alpha^2$ is the linear extension of $\alpha^2 = \mathrm{id}$, hence the identity. Since $2$ is invertible, every $u$ is $\tfrac12(u + \bar\alpha(u)) + \tfrac12(u - \bar\alpha(u))$, a sum of an even and an odd element, and the two eigenspaces meet only at $0$. For the multiplicativity of the grading, if $\bar\alpha(u) = \epsilon u$ and $\bar\alpha(v) = \eta v$ with $\epsilon, \eta \in \{\pm1\}$ then $\bar\alpha(uv) = \bar\alpha(u)\bar\alpha(v) = \epsilon\eta\,uv$, so the product has the sign $\epsilon\eta$; a group element $g \in G \subseteq k[G]$ has $g = \tfrac12(g + \alpha(g)) + \tfrac12(g - \alpha(g))$, an even part and an odd part that coincide with $g$ and $0$ exactly when $\alpha(g) = g$.

**Corollary (which elements are homogeneous).** A group element $g$ is homogeneous of even degree exactly when $\alpha(g) = g$, and it has no odd component exactly in that case; for $\alpha(g)\neq g$ the element $g$ is neither even nor odd, but the antisymmetric combination $g - \alpha(g)$ is odd and the symmetric combination $g + \alpha(g)$ is even.

**Proof.** By the displayed decomposition of $g$; the odd part $\tfrac12(g-\alpha(g))$ vanishes exactly when $g$ is fixed by $\alpha$.

The grading of $k[G]$ is the operator form of the parity that the graded algebras of Part I carry: it is the grading induced by a grade involution, and it is stated for the group algebra in *The Grading of an Algebra*; the article uses it and does not repeat the general theory.

## Graded Modules and the Sign Rule

**Definition.** A **graded module** over $(G,\alpha)$ is a graded $k$-module $M$ with a left action of the group algebra,

$$
k[G] \times M \longrightarrow M, \qquad (u, m) \mapsto u\cdot m ,
$$

that is $k$-linear in $u$ for fixed $m$, additive in $m$ for fixed $u$, and satisfies $u\cdot(v\cdot m) = (uv)\cdot m$ and $1\cdot m = m$; the action is **homogeneous** when

$$
k[G]_i \cdot M_j \subseteq M_{\overline{i+j}} \qquad (i, j \in \{\bar0,\bar1\}).
$$

A **graded action** of $G$ on $M$ is the restriction of a homogeneous action to the group elements, $g\cdot m = \delta_g\cdot m$.

**Theorem (the two descriptions of homogeneity).** A module action of $k[G]$ on a graded module $M = M_{\bar0}\oplus M_{\bar1}$ is homogeneous if and only if there is a $k$-linear involution $\varepsilon$ of $M$ with $\varepsilon|_{M_{\bar0}} = \mathrm{id}$ and $\varepsilon|_{M_{\bar1}} = -\mathrm{id}$, the **grading involution**, such that

$$
\varepsilon\,(g\cdot \varepsilon\, m) = \alpha(g)\cdot m \qquad \text{for all } g \in G,\ m \in M ,
$$

equivalently $\varepsilon \circ g \circ \varepsilon = \alpha(g)$ as operators on $M$. When this holds the assignment $g\cdot_\alpha m := \varepsilon(g \cdot \varepsilon m)$ defines an action of $G$ on $M$, the **$\alpha$-twisted action**, and $g \cdot_\alpha m = \alpha(g)\cdot m$.

**Proof.** Suppose the action is homogeneous. The grading involution is the map $+1$ on $M_{\bar0}$ and $-1$ on $M_{\bar1}$; it is $k$-linear and an involution. For $u = \sum_g u_g g$ put $u_\pm = \tfrac12(u \pm \bar\alpha(u))$, so that $u = u_+ + u_-$ with $u_\pm \in k[G]_{\bar0}, k[G]_{\bar1}$; homogeneity gives $u_+\cdot M_j \subseteq M_j$ and $u_-\cdot M_j \subseteq M_{\overline{j+1}}$. Hence for $m \in M_j$ one has $u\cdot m = u_+\cdot m + u_-\cdot m$ with the two terms of degrees $j$ and $\overline{j+1}$, so

$$
\varepsilon(u\cdot m) = (-1)^j\,u_+\cdot m + (-1)^{j+1}\,u_-\cdot m = (-1)^j\,(u_+ - u_-)\cdot m ,
$$

and therefore $\varepsilon(u\cdot\varepsilon m) = \varepsilon\bigl(u\cdot(-1)^j m\bigr) = (-1)^j\varepsilon(u\cdot m) = (u_+ - u_-)\cdot m = \bar\alpha(u)\cdot m$. Taking $u = g$ gives $\varepsilon g \varepsilon = \alpha(g)$. Conversely, if $\varepsilon u\varepsilon = \bar\alpha(u)$ as operators, then for homogeneous $u$ of parity $i$ one has $\varepsilon u\varepsilon = (-1)^i u$; applying this to $m \in M_j$ and using $\varepsilon u\varepsilon m = (-1)^j\varepsilon(u m)$ gives $(-1)^j\varepsilon(um) = (-1)^i u m$, that is $\varepsilon(um) = (-1)^{i+j}um$, so $um$ lies in the $(-1)^{i+j}$-eigenspace of $\varepsilon$, namely $M_{\overline{i+j}}$.

**Corollary (the sign rule).** Conjugation by the grading involution implements the grade involution on the group algebra: for every $u \in k[G]$,

$$
\varepsilon\, u\, \varepsilon = \bar\alpha(u) , \qquad\text{so}\qquad \varepsilon\,g\,\varepsilon = \alpha(g) \quad (g \in G).
$$

For a homogeneous $u$ of parity $i$ this reads $\varepsilon u\varepsilon = (-1)^i u$: an even element of the group algebra commutes with the grading involution and an odd one anticommutes with it. Hence the odd part $k[G]_{\bar1}$ acts by reversing the grading, $k[G]_{\bar1}\cdot M_j \subseteq M_{\overline{j+1}}$, and the two actions of a group element differ exactly by its odd part,

$$
g\cdot m - \alpha(g)\cdot m = 2\,g_-\cdot m \in M_{\overline{j+1}} \qquad (m \in M_j).
$$

This is the **sign rule** of the graded action: the sign is read off the grading of the module, an odd operator carries it, and the grade involution of the group is what converts the action of $g$ into the action of $\alpha(g)$.


**Example (the regular graded module).** Take $M = k[G]$ with its grading by $\bar\alpha$ and with the action of $k[G]$ on itself by left multiplication. The grading involution is $\bar\alpha$, and the identity $\bar\alpha(u v) = \bar\alpha(u)\bar\alpha(v)$ is the homogeneity; the sign rule reads $\bar\alpha(g\,v) = \alpha(g)\,\bar\alpha(v)$, which is the multiplicativity of $\bar\alpha$.

**Example (a module with a fixed even part).** Let $M = V_{\bar0}\oplus V_{\bar1}$ be a graded vector space on which $G$ acts through the grading-preserving maps of a $\mathbb{Z}/2$-graded algebra, with a group element $g$ acting by an even map when $\alpha(g) = g$. Then the action is homogeneous with $\varepsilon$ the grading of $V$, and the twisted action is by $\alpha(g)$, so the module is graded exactly when the representation is the composite of the given one with $\alpha$.

## The Action and its Compatibility

**Proposition (the action of a group element).** Let $M$ be a graded module with a graded action. For every $g \in G$ and homogeneous $m \in M_j$,

$$
g\cdot M_j \subseteq M_j \iff \alpha(g)\cdot M_j \subseteq M_j ,
$$

and the map $m \mapsto g\cdot m + \alpha(g)\cdot m$ is even while $m \mapsto g\cdot m - \alpha(g)\cdot m$ is odd; both are $k$-linear and are the two homogeneous parts of the operator $m \mapsto 2g\cdot m$.

**Proof.** Write $g = g_+ + g_-$ with $g_\pm$ the even and the odd part of $g$. Then $g\cdot m = g_+\cdot m + g_-\cdot m$ and $\alpha(g)\cdot m = g_+\cdot m - g_-\cdot m$, by the sign rule; the first summand lies in $M_j$ and the second in $M_{\overline{j+1}}$ in both expressions. Hence each of the two inclusions holds exactly when $g_-\cdot m = 0$, and the two are equivalent. The even and odd operators are $\tfrac12(g\cdot + \alpha(g)\cdot\,)$ and $\tfrac12(g\cdot - \alpha(g)\cdot\,)$, the projections of $g\cdot$ onto the two homogeneous parts of $\operatorname{End}_k(M)$.

**Corollary (the fixed module).** The fixed elements $M^G = \{m : g\cdot m = m \text{ for all } g\}$ form a graded submodule, as do the elements on which the two actions agree,

$$
M^{G,\alpha} = \{m : g\cdot m = \alpha(g)\cdot m \text{ for all } g \in G\} = \{m : u\cdot m = 0 \text{ for every odd } u \in k[G]_{\bar1}\},
$$

which is the annihilator of the odd part of the group algebra.

**Proof.** The fixed set is closed under addition and under the action because the action is an action, and it is graded because it is stable under the grading involution. For the second set, the difference $g\cdot m - \alpha(g)\cdot m = 2g_-\cdot m$ vanishes for every $g$ exactly when $u\cdot m = 0$ for every $u$ in the span of the odd parts $g_-$, which is $k[G]_{\bar1}$.

## Continuity

The module carries the discrete topology, which is the only topology available in this category; a topological module in the sense of a topological vector space is *Topology on Linear Spaces*, later in this part, and is named only.

**Theorem (continuity of the action).** Let $M$ carry the discrete topology and let the action $G\times M\to M$ be continuous. Then the action is continuous if and only if every stabiliser

$$
G_m = \{g \in G : g\cdot m = m\}, \qquad m \in M,
$$

is open in $G$; equivalently the action factors through a discrete quotient of $G$. When it is continuous, the orbits are discrete and the orbit map $g \mapsto g\cdot m$ is locally constant for each $m$.

**Proof.** The space $M$ is discrete, so a map $G \to M$ is continuous exactly when it is locally constant, that is when every point has a neighbourhood on which it is constant; the orbit map $g\mapsto g\cdot m$ being locally constant is exactly the openness of its stabiliser $G_m$. The action is continuous at $(g_0, m_0)$ exactly when there is a neighbourhood $U$ of $g_0$ with $g\cdot m_0 = g_0\cdot m_0$ for $g \in U$, which is the openness of $G_{m_0}$ after translating by $g_0^{-1}$. The factorisation statement is the definition of the quotient by the open normal subgroup $\bigcap_m G_m$.

**Theorem (the grading involution is continuous).** The grading involution $\varepsilon$ of a graded module with the discrete topology is a homeomorphism of order two, its two eigenspaces $M_{\bar0}$, $M_{\bar1}$ are closed and open, and the homogeneous components are preserved by every continuous linear operator commuting with $\varepsilon$.

**Proof.** On a discrete space every map is continuous, so $\varepsilon$ is a homeomorphism and its eigenspaces, being the images of the two projection maps $\tfrac12(\mathrm{id}\pm\varepsilon)$, are open and closed. A continuous operator $T$ with $T\varepsilon = \varepsilon T$ satisfies $T M_j \subseteq M_j$, because the eigenspaces are the kernels of $\mathrm{id}\mp\varepsilon$.

**Corollary (the topological form of the sign rule).** For a continuous graded action the element map $g \mapsto g\cdot m$ has image in the orbit and the sign rule $g\cdot_\alpha m = \alpha(g)\cdot m$ holds for every $m$; since $\alpha$ is a homeomorphism of $G$, the twisted action is continuous whenever the original one is, and the twisted module is graded with the same grading involution.

**Proof.** The sign rule is the corollary of the two-descriptions theorem, and the continuity of the twisted action is the continuity of $g \mapsto \alpha(g)\cdot m$, a composite of $\alpha$ with the continuous orbit map.

## Summary

A group with a grade involution has a group algebra graded by the $\pm1$-eigenspaces of the linear extension $\bar\alpha$ of the involution, with $k[G]_ik[G]_j \subseteq k[G]_{\overline{i+j}}$; a group element is homogeneous exactly when it is fixed by the involution, and $g - \alpha(g)$ is the odd combination attached to a general $g$. A **graded module** is a graded $k[G]$-module on which the action is homogeneous, equivalently a graded module carrying a grading involution $\varepsilon$ that intertwines the action with its twist: $\varepsilon g\varepsilon = \alpha(g)$. The equivalence is the content of the sign rule: conjugation by the grading involution implements the grade involution, $\varepsilon u\varepsilon = \bar\alpha(u)$, so an odd element of the group algebra anticommutes with $\varepsilon$ and acts by reversing the grading, and the two actions of a group element differ by its odd part, $g\cdot m - \alpha(g)\cdot m = 2g_-\cdot m$. A homogeneous action is therefore the same datum as an action that is compatible with the grading up to the grade involution. The action of a group element preserves the homogeneous components when the difference between the two actions vanishes on them, the fixed module is graded, and the elements on which the two actions agree are the annihilator of the odd part $k[G]_{\bar1}$. With the discrete topology on the module, continuity of the action is equivalent to the openness of the stabilisers, the grading involution is a homeomorphism whose eigenspaces are open and closed, and the twisted action is continuous whenever the original action is; the topological module in the sense of a topological vector space is *Topology on Linear Spaces*, later in this part, and is not used here.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\alpha$ | the grade involution, a continuous involutive automorphism of $G$ |
| $\bar\alpha$ | its linear extension to the group algebra |
| $k[G]_{\bar0}$, $k[G]_{\bar1}$ | the even and odd parts of the group algebra |
| $k[G]_ik[G]_j \subseteq k[G]_{\overline{i+j}}$ | the grading of the group algebra |
| $M = M_{\bar0}\oplus M_{\bar1}$ | a graded $k$-module, its even and odd parts |
| $\varepsilon$ | the grading involution, $+1$ on $M_{\bar0}$ and $-1$ on $M_{\bar1}$ |
| $\varepsilon g \varepsilon = \alpha(g)$ | compatibility of the action with the grading |
| $g\cdot_\alpha m = \varepsilon(g\cdot\varepsilon m)$ | the $\alpha$-twisted action, equal to $\alpha(g)\cdot m$ |
| $k[G]_i\cdot M_j \subseteq M_{\overline{i+j}}$ | homogeneity of the graded action |
| $G_m$ | the stabiliser of $m$; the action is continuous iff every $G_m$ is open |
| $M^G$ | the fixed submodule, graded |

## Further Reading

- Nicolas Bourbaki, *Algebra I*, Chapters 1–3 (Springer, 1998), for graded algebras, the grading an involution of order two defines and the homogeneous components.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for involutive automorphisms and the modules graded by them.
- Charles W. Curtis and Irving Reiner, *Representation Theory of Finite Groups and Associative Algebras* (Wiley, 1962), for the action of a group algebra and its homogeneous parts.
- Lev S. Pontryagin, *Topological Groups* (Gordon and Breach, second edition, 1966), for the continuity of a group action and the openness of the stabilisers.
- Alexander Arhangel'skii and Mikhail Tkachenko, *Topological Groups and Related Structures* (Atlantis Press, 2008), for the action of a topological group on a discrete set and the associated quotient topologies.
