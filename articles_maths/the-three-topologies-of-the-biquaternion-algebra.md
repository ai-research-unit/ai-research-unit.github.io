# __The Three Topologies of the Biquaternion Algebra__

## Introduction

The topology region of the biquaternion category is divided into three sub-categories — *Topology Induced by the Bilinear Form*, *Topology Induced by the Hermitian Form* and *Topology Induced by the Krein Form* — and each name invites the reading that the algebra carries three inequivalent topologies, one per form. This article examines the distance each form supplies and settles the question: the algebra carries **one** topology, and the three names denote three structures read inside it, not three point-set topologies on one set of points.

The examination corrects a first guess. Since only the Hermitian diagonal is positive definite, one is tempted to conclude that the other two forms give no norm and no distance at all. That conclusion is false. A non-degenerate form always yields a distance, through a **symmetry** rather than through its diagonal: the symmetrised expression $\mathrm{Re}\,\Phi(J\tilde{P},\tilde{Q})$ is an inner product, and every non-degenerate form has such a symmetry, by Sylvester. The diagonal route, positive definite or nothing, is one route among two, and it is the weaker one.

The argument therefore has three parts. Each form gives a distance, by the symmetry route. The three distances coincide, because the symmetries of the three forms are the complex conjugation and the natural conjugation and each of them returns the Hermitian form. And no second topology is possible in any case, because all norms on a finite-dimensional real space are equivalent. What the three layers do single out, and what the three names are legitimately true of, is three **unit level sets** and three **isometry groups**, and these are genuinely distinct topological objects.

The article is the companion of *Introduction to Topology on the Biquaternions*, which presents the three layers and compares them; that article states the verdict, and this one gives its reasons. It quotes the three forms from *The Three Pairings of the Biquaternion Algebra*, the Euclidean structure from *The Euclidean Topology of the Biquaternion Algebra*, the level sets and homotopy of the bilinear layer from *Biquaternion Topology* and *The Biquaternion Unit Group as a Topological Group*, those of the Krein layer from *The Krein Level Sets and the Hyperbolic Structure*, the symmetry from *The Fundamental Symmetry of the Biquaternion Algebra*, and the three isometry groups from *The Three Pairings of the Biquaternion Algebra*. No physics is invoked.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with units $e_0=1,e_1,e_2,e_3$, $e_k^{2}=-e_0$, central scalar imaginary $i$, and a general element $\tilde{Q}=\sum_{\mu=0}^{3}Q_\mu e_\mu$ with $Q_\mu=q_\mu+iq'_\mu\in\mathbb{C}$. The three forms are

$$
B(\tilde{P},\tilde{Q})=\sum_\mu P_\mu Q_\mu,\qquad
\langle\tilde{P},\tilde{Q}\rangle=\sum_\mu\overline{P_\mu}Q_\mu,\qquad
[\tilde{P},\tilde{Q}]=\sum_\mu\varepsilon_\mu\overline{P_\mu}Q_\mu,
$$

with $\varepsilon=(1,-1,-1,-1)$. The biquaternion norm is $N(\tilde{Q})=\sum_\mu Q_\mu^{2}$, the Euclidean norm is $\lVert\tilde{Q}\rVert_E=\bigl(\sum_\mu\lvert Q_\mu\rvert^{2}\bigr)^{1/2}$, $J={}^{\natural}$ is the natural conjugation, and $c=\bar{\cdot}$ is the complex conjugation.

## The Name and the Question

A **topology on $\mathbb{B}$**, in the sense at issue, is a Hausdorff topology making the vector-space operations continuous — the topology of a metric, not an arbitrary point-set topology on the underlying set. The question is whether the three forms define one such topology or three.

Two routes lead from a form to a distance, and they must be kept apart.

- the **diagonal route**, which reads the length of $\tilde{Q}$ from the value $\Phi(\tilde{Q},\tilde{Q})$ alone; and
- the **symmetry route**, which composes the form with an involution $J$ of the space before taking the length.

The diagonal route is the obvious one and it is the weaker one. The article takes it first, to see exactly what it gives and where it stops, and then takes the symmetry route, which is the one that decides the question.

## The Three Diagonals

The three diagonals, written in the real coordinates $q_\mu,q'_\mu$, are collected here with the range of values each takes.

| layer | diagonal $\Phi(\tilde{Q},\tilde{Q})$ | in real coordinates | values taken |
|---|---|---|---|
| bilinear | $\sum_\mu Q_\mu^{2}$ | $\sum_\mu\bigl(q_\mu^{2}-q'_\mu{}^{2}\bigr)$ | complex; both signs and $0$ |
| Hermitian | $\sum_\mu\lvert Q_\mu\rvert^{2}$ | $\sum_\mu\bigl(q_\mu^{2}+q'_\mu{}^{2}\bigr)$ | real, $\geq0$, vanishes only at $0$ |
| Krein | $\sum_\mu\varepsilon_\mu\lvert Q_\mu\rvert^{2}$ | $q_0^{2}+q'_{0}{}^{2}-\sum_{k}\bigl(q_k^{2}+q'_k{}^{2}\bigr)$ | real, both signs and $0$ |

Only the second is non-negative, and only it vanishes at the origin alone. The other two take the value zero away from the origin, and the two witnesses are the ones the corpus uses throughout:

$$
N(e_1+ie_2)=1+i^{2}=0,\qquad
[e_0+e_1,e_0+e_1]=1-1=0,\qquad
[e_1,e_1]=-1 .
$$

The first is a non-zero element of *complex length zero*; the second is a non-zero element of *real length zero*; the third is a non-zero element whose square is negative. The table is the data the diagonal route has to work with.

## The Diagonal Route and Its Limit

**Definition (norm).** A **norm** on a real vector space $V$ is a map $\lVert\cdot\rVert:V\to\mathbb{R}$ with (i) $\lVert v\rVert\geq0$ and $\lVert v\rVert=0\iff v=0$; (ii) $\lVert\lambda v\rVert=\lvert\lambda\rvert\lVert v\rVert$ for real $\lambda$; and (iii) $\lVert v+w\rVert\leq\lVert v\rVert+\lVert w\rVert$.

**Theorem (the diagonal route gives a norm exactly when the form is positive definite).** Let $\Phi$ be a real-valued form on a real vector space $V$ whose diagonal is non-negative. Then $v\mapsto\bigl(\Phi(v,v)\bigr)^{1/2}$ is a norm on $V$ if and only if $\Phi$ is positive definite. A form whose diagonal takes a negative value has no real square root at all.

**Proof.** If $\Phi$ is positive definite, its polar form satisfies the Cauchy–Schwarz inequality $\Phi(v,w)^{2}\leq\Phi(v,v)\Phi(w,w)$, whence

$$
\Phi(v+w,v+w)=\Phi(v,v)+2\Phi(v,w)+\Phi(w,w)\leq\Bigl(\bigl(\Phi(v,v)\bigr)^{1/2}+\bigl(\Phi(w,w)\bigr)^{1/2}\Bigr)^{2},
$$

which is (iii); (i) and (ii) are immediate. Conversely, if $\Phi(v_0,v_0)=0$ at some $v_0\neq0$ then the map vanishes at a non-zero point and (i) fails; if $\Phi(v_0,v_0)<0$ the value is not real; and an indefinite form has both a negative value and a non-zero isotropic vector. $\square$

**Corollary (only one diagonal is positive definite).** Of the three diagonals of §*The Three Diagonals* only the Hermitian one is positive definite. Therefore the diagonal route gives a norm for the Hermitian form and for neither of the other two.

**Remark (an indefinite diagonal fails the triangle inequality too, not only separation).** Even on the part of an indefinite form where the diagonal is real and positive, the square root can fail axiom (iii). On the centre $\mathbb{C}_{\mathbb{B}}$ the bilinear diagonal is $q_0^{2}-q'_{0}{}^{2}$, and on the elements $u=2e_0+ie_0$, $v=2e_0-ie_0$, $u+v=4e_0$ one has

$$
\bigl(N(u)\bigr)^{1/2}=\bigl(N(v)\bigr)^{1/2}=\sqrt3,\qquad
\bigl(N(u+v)\bigr)^{1/2}=4>2\sqrt3 ,
$$

so axiom (iii) fails on the very part of the centre where the square root is defined. The failure is not only the vanishment on the lightlike elements.

**Remark (what this rules out).** The corollary rules out the **diagonal route** for the bilinear and the Krein form. It does not rule out a distance from those forms, because the diagonal route is not the only route. The next section takes the other one.

## The Symmetry Route

The route that always works composes the form with an involution before taking the length. The involution is a symmetry of the form in the following sense.

**Definition (symmetry).** Let $\Phi$ be a symmetric or Hermitian form on a space $V$ over $\mathbb{R}$ or $\mathbb{C}$. A **symmetry** of $\Phi$ is a linear involution $J$ with

$$
J^{2}=\mathrm{id},\qquad \Phi(Jv,Jw)=\Phi(v,w)\ \text{for all }v,w,\qquad \Phi(Jv,v)>0\ \text{for }v\neq0 .
$$

The second condition says $J$ is an isometry of the form; the third is its definiteness witness. Since $J^{2}=\mathrm{id}$ and $J$ preserves $\Phi$, the two conditions make $J$ self-adjoint for $\Phi$: $\Phi(Jv,w)=\Phi(Jv,J^{2}w)=\Phi(v,Jw)$.

**Theorem (every non-degenerate form has a symmetry).** Let $\Phi$ be a non-degenerate symmetric or Hermitian form on a finite-dimensional space $V$ over $\mathbb{R}$ or $\mathbb{C}$. Then $V$ has a direct sum decomposition $V=V_{+}\oplus V_{-}$ into mutually orthogonal subspaces on which $\Phi$ is positive definite and negative definite respectively, and $J=\mathrm{id}$ on $V_{+}$, $J=-\mathrm{id}$ on $V_{-}$ is a symmetry of $\Phi$.

**Proof.** Sylvester's law of inertia gives the decomposition, and non-degeneracy ensures that the two parts span: a vector orthogonal to the whole space would be zero, so no radical is left over. On a vector $v=v_{+}+v_{-}$ the three conditions are immediate, $\Phi(Jv,v)=\Phi(v_{+},v_{+})-\Phi(v_{-},v_{-})$ being a sum of two positive definite terms off zero. $\square$

**Theorem (the symmetry route always gives an inner product, hence a distance).** Let $J$ be a symmetry of $\Phi$. Then

$$
(v,w)_{J}=\Phi(Jv,w)
$$

is an inner product on $V$; the associated $\lVert v\rVert_{J}=\bigl(\Phi(Jv,v)\bigr)^{1/2}$ is a norm; $d_{J}(v,w)=\lVert v-w\rVert_{J}$ is a distance; and it induces a metric topology on $V$.

**Proof.** The map is linear in the second argument and conjugate-symmetric, since $(w,v)_{J}=\Phi(Jw,v)=\Phi(v,Jw)=\overline{\Phi(Jv,w)}$ by the self-adjointness; it is positive definite because $(v,v)_{J}=\Phi(Jv,v)>0$ off zero. An inner product gives a norm by Cauchy–Schwarz, and a norm gives a distance. $\square$

**Corollary (all three forms of the algebra give a distance).** The bilinear, the Hermitian and the Krein form are non-degenerate and of finite dimension, so each has a symmetry and each gives a distance. **The bilinear and the Krein form are therefore not without a norm; they are without a norm from their diagonals.**

**Remark (why the symmetry is needed, and not an absolute value).** The tempting repair of the diagonal route is to take $\lvert\Phi(\tilde{Q},\tilde{Q})\rvert^{1/2}$, and it fails. On the Krein form put $v=e_0+e_1$ and $w=e_0-e_1$; then $[v,v]=[w,w]=0$ while $[v+w,v+w]=[2e_0,2e_0]=4$. The repaired expression gives distance $0$ from $0$ to the non-zero $v$, so axiom (i) fails, and it gives $2\leq0+0$ for the triangle inequality, so axiom (iii) fails. Both failures come from the sign, not from the size, and only an involution that converts the sign into a positive contribution removes them. The symmetry does exactly that: $[v^{\natural},v]=2$, $[w^{\natural},w]=2$, $[(v+w)^{\natural},v+w]=4$, and the three now satisfy both axioms.

**Remark (non-degeneracy is what is needed).** The theorem uses non-degeneracy to leave no radical, and all three forms of the algebra are non-degenerate. A degenerate form would have a symmetry on its non-degenerate part only, and its radical would be invisible to the form; the question does not arise here.

## The Three Symmetries and the Coincidence of the Distances

The three symmetries are involutions already at hand in the Algebra layer, and each is named in the corpus. They are collected in the table, with the form each symmetrises and the identity it satisfies.

| form $\Phi$ | symmetry $J$ | the symmetrised form $(v,w)_{J}=\Phi(Jv,w)$ | value at $v=w=\tilde{Q}$ |
|---|---|---|---|
| bilinear $B$ | complex conjugation $c=\bar{\cdot}$ | $B(\bar{\tilde{P}},\tilde{Q})=\langle\tilde{P},\tilde{Q}\rangle$ | $\lVert\tilde{Q}\rVert_E^{2}$ |
| Hermitian $\langle\cdot,\cdot\rangle$ | identity | $\langle\tilde{P},\tilde{Q}\rangle$ | $\lVert\tilde{Q}\rVert_E^{2}$ |
| Krein $[\cdot,\cdot]$ | natural conjugation ${}^{\natural}$ | $[\tilde{P}^{\natural},\tilde{Q}]=\langle\tilde{P},\tilde{Q}\rangle$ | $\lVert\tilde{Q}\rVert_E^{2}$ |

**Theorem (the three distances coincide).** The three symmetrised forms of the table are equal, all three being the Hermitian form $\langle\cdot,\cdot\rangle$. Consequently the three distances are equal, all three being the Euclidean distance of $\lVert\cdot\rVert_E$, and the three metric topologies are one topology.

**Proof.** For the bilinear row, $B(\bar{\tilde{P}},\tilde{Q})=\sum_\mu\overline{P_\mu}Q_\mu=\langle\tilde{P},\tilde{Q}\rangle$ by the definitions of $B$ and of the complex conjugation. For the Hermitian row there is nothing to do, the symmetry being the identity. For the Krein row, $(\tilde{P}^{\natural})_\mu=\varepsilon_\mu P_\mu$ and $\varepsilon_\mu^{2}=1$, so $[\tilde{P}^{\natural},\tilde{Q}]=\sum_\mu\varepsilon_\mu\overline{\varepsilon_\mu P_\mu}Q_\mu=\sum_\mu\overline{P_\mu}Q_\mu=\langle\tilde{P},\tilde{Q}\rangle$; this is the bridge identity of *The Fundamental Symmetry of the Biquaternion Algebra*, §*The Natural Conjugation as a Fundamental Symmetry*. The three are equal to the Hermitian form, whose associated norm is $\lVert\cdot\rVert_E$ by definition. $\square$

**Remark (the first guess is inverted).** The Hermitian form is not the one form that gives a distance while the others give none; it is the one form that gives the distance with no symmetry required. The three forms give the **same** distance, and the coincidence is exact, not up to equivalence.

**Remark (other symmetries give other but equivalent distances).** The symmetry of an indefinite form is not unique: the fundamental symmetries of the Krein form are parametrised by the open unit ball of the vector subspace (*The Fundamental Symmetry of the Biquaternion Algebra*, §*Non-Uniqueness and the Angular Operator*), and each choice gives its own inner product and its own distance. Those distances are not equal to one another in general, but they are all norms on the finite-dimensional space, so by the next section they all induce the same topology. The coincidence above is exact for the canonical symmetries, and the uniqueness of the topology does not depend on it.

## The Uniqueness of the Topology

**Theorem (finite-dimensional norms are equivalent).** On a finite-dimensional real vector space all norms are equivalent: for any two norms there are constants $c,C>0$ with $c\lVert v\rVert_{1}\leq\lVert v\rVert_{2}\leq C\lVert v\rVert_{1}$. Consequently all such norms induce the same topology, indeed the unique Hausdorff vector-space topology on the space.

**Proof.** Standard; it reduces to the compactness of the unit sphere of $\mathbb{R}^{n}$ and the continuity of the other norm there (see *Further Reading*). $\square$

**Corollary (at most one topology, whichever symmetry is chosen).** Every norm obtainable from any of the three forms, on $\mathbb{B}$ or on any of its subspaces, with any choice of symmetry, induces the same topology, namely the Euclidean one. The three layers cannot induce three topologies: they induce one topology, and the only freedom left within it is the choice of an equivalent distance.

**Remark (two reasons for one topology, one of them stronger).** There are two independent reasons the algebra carries one topology. The weaker is the equivalence of the norms, which holds for any choice of symmetries and any forms. The stronger is the coincidence of §*The Three Symmetries and the Coincidence of the Distances*, which holds for the three canonical symmetries. The first would suffice on its own; the second is stated because it is exact.

## What the Three Names Are True Of

Two readings survive the argument, and they are the ones the articles of the region actually use.

### The three unit level sets

Each form singles out a level set, and each level set is a different topological space. They are collected in the table; the homotopy types are those of the owning articles.

| layer | level set | topology | a group? |
|---|---|---|---|
| bilinear | $N(\tilde{Q})=1$ | non-compact real $6$-manifold, homotopy equivalent to $S^{3}$ | yes, the norm-one group $\mathbb{B}^\times_1$ |
| Hermitian | $\lVert\tilde{Q}\rVert_E=1$ | the sphere $S^{7}$, compact | no; contains zero divisors |
| Krein | $[\tilde{Q},\tilde{Q}]=1$ | $\cong S^{1}\times\mathbb{R}^{6}$, non-compact, homotopy equivalent to $S^{1}$ | no |

The first is a group, the other two are not; the first and the third are non-compact, the second is compact; the second is a sphere and the other two are not. Three forms, three level sets, three distinct spaces — this is a sense in which the algebra carries three topologies, and it is a statement about subsets, not about the algebra.

The same holds of the further subsets each layer owns: the null cone of the bilinear form with its link, the null set of the Krein form and its isotropic planes, the Euclidean sphere with its link and the unitary group. Each is read in the one topology of §*The Uniqueness of the Topology*, by taking the subspace topology; none requires a second topology on the algebra.

### The three isometry groups

Each form singles out the group of linear maps that preserve it, and each such group is a closed subgroup of $GL_{8}(\mathbb{R})$, hence a topological group in the subspace topology.

| layer | form | isometry group | real dimension | compact? |
|---|---|---|---|---|
| bilinear | $B(\tilde{P},\tilde{Q})=\sum_\mu P_\mu Q_\mu$ | $O_4(\mathbb{C})$ | $12$ | no |
| Hermitian | $\langle\tilde{P},\tilde{Q}\rangle=\sum_\mu\overline{P_\mu}Q_\mu$ | $U(4)$ | $16$ | yes |
| Krein | $[\tilde{P},\tilde{Q}]=\sum_\mu\varepsilon_\mu\overline{P_\mu}Q_\mu$ | $U(1,3)$ | $16$ | no |

The three groups are pairwise non-isomorphic as topological groups: the first has dimension $12$ while the other two have dimension $16$, and of the two of dimension $16$ one is compact and the other is not. **A form induces the topological group of its isometries, and the three forms here induce three distinct such groups: this is a reading under which the phrase *topology induced by the form* is exactly true.** The dimensions are those of *The Three Pairings of the Biquaternion Algebra*, §*The Adjoints and the Three Isometry Groups*, and of *The Krein Isometry Group and Its $J$-Contractions*, §*The Group of Krein Isometries*.

## The Verdict

Every one of the three forms of the biquaternion algebra gives a distance, and the three distances are the same, the Euclidean one. The bilinear and the Krein form fail the **diagonal route** — their diagonals vanish on the non-zero $e_1+ie_2$ and $e_0+e_1$, and the square root of an indefinite diagonal fails the triangle inequality even where it is real — but they do not fail to give a distance: the symmetry route supplies one for every non-degenerate form, by Sylvester, and for these two the symmetries are the complex conjugation and the natural conjugation, each of which returns the Hermitian form. The algebra $\mathbb{B}$ therefore carries one topology: the three distances coincide, and independently all norms on a finite-dimensional real space are equivalent. **The three sub-categories are named for the structure each form induces beyond the common distance — its diagonal and signature, its null set and level sets, its isometry group — and the three names are true of those structures, not of three inequivalent topologies on the algebra.** The units are decided by the bilinear norm and their topology by the Hermitian form, which is the same statement in the language of the group (*The Biquaternion Unit Group as a Topological Group*, §*The Topology of the Group*).

**Remark (the caveat belongs to the reader).** The three names are the author's, and the corpus keeps them; this article exists so that the caveat is stated once and can be cited rather than repeated. Any later article that writes of a statement *read in the topology induced by the Krein form* means the structure the Krein form induces, read in the one Euclidean topology.

## Summary

A non-degenerate form reaches a distance by one of two routes. The diagonal route, reading the length from $\Phi(\tilde{Q},\tilde{Q})$ alone, gives a norm exactly when the form is positive definite, and of the three diagonals only the Hermitian one is: the bilinear diagonal vanishes on the non-zero $e_1+ie_2$, the Krein diagonal on the non-zero $e_0+e_1$, and the square root of an indefinite diagonal fails the triangle inequality even where it is real, as on the centre where $\sqrt3+\sqrt3<4$. The symmetry route, reading the length from $\mathrm{Re}\,\Phi(J\tilde{P},\tilde{Q})$ for a symmetry $J$, gives an inner product and a distance for **every** non-degenerate form, by Sylvester, and it is the route that decides the question: the bilinear and the Krein form are not without a norm, they are without a norm from their diagonals. The symmetries of the three forms are the complex conjugation, the identity and the natural conjugation, and each returns the Hermitian form, so the three distances coincide exactly with the Euclidean distance; independently, all norms on a finite-dimensional real space are equivalent, so one topology is all the algebra can carry. What the three layers do own is three unit level sets — the norm-one group, homotopy equivalent to $S^{3}$; the sphere $S^{7}$; the hyperboloid $S^{1}\times\mathbb{R}^{6}$ — and three isometry groups — $O_4(\mathbb{C})$ of dimension $12$, $U(4)$ of dimension $16$ and compact, $U(1,3)$ of dimension $16$ and non-compact — which are pairwise distinct topological objects. The three names are true of those structures, not of three topologies on the algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\lVert\cdot\rVert$, axioms (i)–(iii) | the norm of a real vector space |
| $\Phi$ positive definite $\iff$ $\bigl(\Phi(\cdot,\cdot)\bigr)^{1/2}$ is a norm | the diagonal route |
| $N(e_1+ie_2)=0$, $[e_0+e_1,e_0+e_1]=0$, $[e_1,e_1]=-1$ | the witnesses that stop the diagonal route |
| $J^{2}=\mathrm{id}$, $\Phi(Jv,Jw)=\Phi(v,w)$, $\Phi(Jv,v)>0$ | a symmetry of the form |
| $(v,w)_{J}=\Phi(Jv,w)$ | the inner product the symmetry produces |
| Sylvester decomposition $V=V_{+}\oplus V_{-}$ | every non-degenerate form has a symmetry, hence a distance |
| $B(\bar{\tilde{P}},\tilde{Q})=\langle\tilde{P},\tilde{Q}\rangle$ | the symmetry of the bilinear form is $c=\bar{\cdot}$ |
| $[\tilde{P}^{\natural},\tilde{Q}]=\langle\tilde{P},\tilde{Q}\rangle$ | the symmetry of the Krein form is $J={}^{\natural}$ |
| the three symmetrised forms are equal | the three distances coincide |
| all norms equivalent, dimension finite | one topology, whatever the symmetry |
| $\mathbb{B}^\times_1$, $S^{7}_{E}$, $\{[\tilde{Q},\tilde{Q}]=1\}$ | the three unit level sets |
| $S^{3}$, $S^{7}$, $S^{1}\times\mathbb{R}^{6}$ | their homotopy types |
| $O_4(\mathbb{C})$, $U(4)$, $U(1,3)$ | the three isometry groups; dimensions $12$, $16$, $16$; compactness no, yes, no |

## Further Reading

- *Introduction to Topology on the Biquaternions* (`articles_maths/introduction-to-topology-on-the-biquaternions.md`), the companion that presents the three layers and the comparison table
- *The Three Pairings of the Biquaternion Algebra* (`articles_maths/the-three-pairings-of-the-biquaternion-algebra.md`), for the three forms, their Gram matrices, their signatures, their mutual determination and their isometry groups
- *The Fundamental Symmetry of the Biquaternion Algebra* (`articles_maths/the-fundamental-symmetry-of-the-biquaternion-algebra.md`), for the symmetry $J={}^{\natural}$, the bridge identity and the non-uniqueness of the symmetry
- *The Euclidean Topology of the Biquaternion Algebra* (`articles_maths/the-euclidean-topology-of-the-biquaternion-algebra.md`), for the topology the Hermitian form induces and for the sphere $S^{7}_{E}$
- *The Krein Level Sets and the Hyperbolic Structure* (`articles_maths/the-krein-level-sets-and-the-hyperbolic-structure.md`), for the level sets $S^{1}\times\mathbb{R}^{6}$ and $S^{5}\times\mathbb{R}^{2}$
- *The Krein Isometry Group and Its $J$-Contractions* (`articles_maths/the-krein-isometry-group-and-its-j-contractions.md`), for the group $U(1,3)$, its dimension and its maximal compact subgroup
- *The Biquaternion Unit Group as a Topological Group* (`articles_maths/the-biquaternion-unit-group-as-a-topological-group.md`), for the sentence that the norm defines the group but not its topology, and for $\mathbb{B}^\times_1\simeq S^{3}$
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the real forms, their signatures and the audit of the norm axioms
- Walter Rudin, *Functional Analysis*, 2nd ed. (McGraw-Hill, 1991), Theorem 1.21, for the equivalence of the norms on a finite-dimensional space and the uniqueness of its Hausdorff vector-space topology
