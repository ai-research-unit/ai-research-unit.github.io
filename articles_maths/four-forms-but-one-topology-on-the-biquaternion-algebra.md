# __Four Forms but One Topology on the Biquaternion Algebra__

## Introduction

The topology region of the biquaternion category is divided into the sub-categories *Topology Induced by the Bilinear Form*, *Topology Induced by the Hermitian Form* and *Topology Induced by the Krein Form*, and each name invites the reading that the algebra carries three inequivalent topologies, one per form. The algebra in fact carries four distinguished forms — the complex bilinear, the quaternion bilinear, the complex sesquilinear and the quaternion sesquilinear form — and this article examines the distance each of the four supplies and settles the question: the algebra carries **one** topology, and the four names denote four structures read inside it, not four point-set topologies on one set of points.

The examination corrects a first guess. Since only the complex sesquilinear diagonal is positive definite, one is tempted to conclude that the other three forms give no norm and no distance at all. That conclusion is false. A non-degenerate form always yields a distance, through a **symmetry** rather than through its diagonal: the symmetrised expression is an inner product, and every non-degenerate form has such a symmetry, by Sylvester. The diagonal route, positive definite or nothing, is one route among two, and it is the weaker one.

The argument therefore has three parts. Each form gives a distance, by the symmetry route. The four distances coincide, because the symmetries of the four forms are the four involutions $\mathrm{id},{}^{\natural},\bar{\cdot},{}^{*}$ and each of them returns the complex sesquilinear form. And no second topology is possible in any case, because all norms on a finite-dimensional real space are equivalent. What the layers do single out, and what the four names are legitimately true of, is four **level sets** and the **isometry groups**, and these are genuinely distinct topological objects.

The article is the companion of *Introduction to Topology on the Biquaternions*, which presents the four layers and compares them; that article states the verdict, and this one gives its reasons. It quotes the four forms from *The Four Biquaternion Complex Products* and *The Four Pairings of the Biquaternion Algebra*, the Euclidean structure from *The Euclidean Topology of the Biquaternion Algebra*, the level sets and homotopy of the quaternion bilinear layer from *Biquaternion Topology* and *The Biquaternion Unit Group as a Topological Group*, those of the quaternion sesquilinear layer from *The Krein Level Sets and the Hyperbolic Structure*, the symmetry from *The Fundamental Symmetry of the Biquaternion Algebra*, and the isometry groups from *The Four Pairings of the Biquaternion Algebra*. No physics is invoked.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with units $e_0=1,e_1,e_2,e_3$, $e_k^{2}=-e_0$, central scalar imaginary $i$, and a general element $\tilde{Q}=\sum_{\mu=0}^{3}Q_\mu e_\mu$ with $Q_\mu=q_\mu+iq'_\mu\in\mathbb{C}$. The four forms are written with the one bracket of the region, whose subscript records the conjugation entering each argument — the natural conjugation ${}^{\natural}$ in the first, the complex conjugation $\bar{\cdot}$ in the second,

$$
\langle\tilde{P},\tilde{Q}\rangle=\mathrm{Sc}(\tilde{P}\tilde{Q}),\qquad
\langle\tilde{P},\tilde{Q}\rangle_{\natural}=\mathrm{Sc}(\tilde{P}^{\natural}\tilde{Q}),\qquad
\langle\tilde{P},\tilde{Q}\rangle_{*}=\mathrm{Sc}(\tilde{P}\tilde{Q}^{*}),\qquad
\langle\tilde{P},\tilde{Q}\rangle_{\natural*}=\mathrm{Sc}(\tilde{P}^{\natural}\tilde{Q}^{*}),
$$

that is, in coordinates with $\varepsilon=(1,-1,-1,-1)$,

$$
\langle\tilde{P},\tilde{Q}\rangle=\sum_\mu\varepsilon_\mu P_\mu Q_\mu,\qquad
\langle\tilde{P},\tilde{Q}\rangle_{\natural}=\sum_\mu P_\mu Q_\mu,\qquad
\langle\tilde{P},\tilde{Q}\rangle_{*}=\sum_\mu P_\mu\overline{Q_\mu},\qquad
\langle\tilde{P},\tilde{Q}\rangle_{\natural*}=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}.
$$

The quaternion bilinear form has diagonal $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=\sum_\mu Q_\mu^{2}$, the Euclidean norm is $\lVert\tilde{Q}\rVert_E=\bigl(\sum_\mu\lvert Q_\mu\rvert^{2}\bigr)^{1/2}$, the natural conjugation is $J={}^{\natural}$, and the complex conjugation is $c=\bar{\cdot}$.

## The Name and the Question

A **topology on $\mathbb{B}$**, in the sense at issue, is a Hausdorff topology making the vector-space operations continuous — the topology of a metric, not an arbitrary point-set topology on the underlying set. The question is whether the four forms define one such topology or four.

Two routes lead from a form to a distance, and they must be kept apart.

- the **diagonal route**, which reads the length of $\tilde{Q}$ from the value $\Phi(\tilde{Q},\tilde{Q})$ alone; and
- the **symmetry route**, which composes the form with an involution $J$ of the space before taking the length.

The diagonal route is the obvious one and it is the weaker one. The article takes it first, to see exactly what it gives and where it stops, and then takes the symmetry route, which is the one that decides the question.

## The Four Diagonals

The four diagonals, written in the real coordinates $q_\mu,q'_\mu$, are collected here with the range of values each takes.

| form | diagonal $\Phi(\tilde{Q},\tilde{Q})$ | in real coordinates | values taken |
|---|---|---|---|
| complex bilinear | $\sum_\mu\varepsilon_\mu Q_\mu^{2}$ | $\sum_\mu\varepsilon_\mu\bigl(q_\mu^{2}-q'_\mu{}^{2}\bigr)$ | complex; both signs and $0$ |
| quaternion bilinear | $\sum_\mu Q_\mu^{2}$ | $\sum_\mu\bigl(q_\mu^{2}-q'_\mu{}^{2}\bigr)$ | complex; both signs and $0$ |
| complex sesquilinear | $\sum_\mu\lvert Q_\mu\rvert^{2}$ | $\sum_\mu\bigl(q_\mu^{2}+q'_\mu{}^{2}\bigr)$ | real, $\geq0$, vanishes only at $0$ |
| quaternion sesquilinear | $\sum_\mu\varepsilon_\mu\lvert Q_\mu\rvert^{2}$ | $q_0^{2}+q'_{0}{}^{2}-\sum_{k}\bigl(q_k^{2}+q'_k{}^{2}\bigr)$ | real, both signs and $0$ |

Only the third is non-negative, and only it vanishes at the origin alone. The other three take the value zero away from the origin, and the witnesses are the ones the corpus uses throughout:

$$
\langle e_0+e_1,e_0+e_1\rangle=1-1=0,\qquad
\langle e_1+ie_2,e_1+ie_2\rangle_{\natural}=1+i^{2}=0,\qquad
\langle e_0+e_1,e_0+e_1\rangle_{\natural*}=1-1=0,\qquad
\langle e_1,e_1\rangle_{\natural*}=-1 .
$$

The first is a non-zero element whose complex bilinear length is zero; the second is a non-zero element of *quaternion length zero*, the zero divisor; the third is a non-zero element of *real length zero* in the quaternion sesquilinear form; and the fourth is a non-zero element whose quaternion sesquilinear square is negative. The table is the data the diagonal route has to work with.

## The Diagonal Route and Its Limit

**Definition (norm).** A **norm** on a real vector space $V$ is a map $\lVert\cdot\rVert:V\to\mathbb{R}$ with (i) $\lVert v\rVert\geq0$ and $\lVert v\rVert=0\iff v=0$; (ii) $\lVert\lambda v\rVert=\lvert\lambda\rvert\lVert v\rVert$ for real $\lambda$; and (iii) $\lVert v+w\rVert\leq\lVert v\rVert+\lVert w\rVert$.

**Theorem (the diagonal route gives a norm exactly when the form is positive definite).** Let $\Phi$ be a real-valued form on a real vector space $V$ whose diagonal is non-negative. Then $v\mapsto\bigl(\Phi(v,v)\bigr)^{1/2}$ is a norm on $V$ if and only if $\Phi$ is positive definite. A form whose diagonal takes a negative value has no real square root at all.

**Proof.** If $\Phi$ is positive definite, its polar form satisfies the Cauchy–Schwarz inequality $\Phi(v,w)^{2}\leq\Phi(v,v)\Phi(w,w)$, whence

$$
\Phi(v+w,v+w)=\Phi(v,v)+2\Phi(v,w)+\Phi(w,w)\leq\Bigl(\bigl(\Phi(v,v)\bigr)^{1/2}+\bigl(\Phi(w,w)\bigr)^{1/2}\Bigr)^{2},
$$

which is (iii); (i) and (ii) are immediate. Conversely, if $\Phi(v_0,v_0)=0$ at some $v_0\neq0$ then the map vanishes at a non-zero point and (i) fails; if $\Phi(v_0,v_0)<0$ the value is not real; and an indefinite form has both a negative value and a non-zero isotropic vector. $\square$

**Corollary (only one diagonal is positive definite).** Of the four diagonals of §*The Four Diagonals* only the complex sesquilinear one is positive definite. Therefore the diagonal route gives a norm for the complex sesquilinear form and for none of the other three.

**Remark (an indefinite diagonal fails the triangle inequality too, not only separation).** Even on the part of an indefinite form where the diagonal is real and positive, the square root can fail axiom (iii). On the centre $\mathbb{C}_{\mathbb{B}}$ both bilinear diagonals read $\sum_\mu\varepsilon_\mu Q_\mu^{2}$ and $\sum_\mu Q_\mu^{2}$, whose real part there is $q_0^{2}-q'_{0}{}^{2}$, and on the elements $u=2e_0+ie_0$, $v=2e_0-ie_0$, $u+v=4e_0$ one has

$$
\bigl(\langle u,u\rangle_{\natural}\bigr)^{1/2}=\bigl(\langle v,v\rangle_{\natural}\bigr)^{1/2}=\sqrt3,\qquad
\bigl(\langle u+v,u+v\rangle_{\natural}\bigr)^{1/2}=4>2\sqrt3 ,
$$

so axiom (iii) fails on the very part of the centre where the square root is defined. The failure is not only the vanishment on the lightlike elements.

**Remark (what this rules out).** The corollary rules out the **diagonal route** for the three indefinite forms. It does not rule out a distance from those forms, because the diagonal route is not the only route. The next section takes the other one.

## The Symmetry Route

The route that always works composes the form with an involution before taking the length. Since the four forms are complex-valued, each is read through its real part $\mathrm{Re}\,\Phi$, a real symmetric bilinear form on $\mathbb{B}\cong\mathbb{R}^{8}$; nothing in the argument needs the complex values. The involution is a symmetry of the real form in the following sense.

**Definition (symmetry).** Let $\Phi$ be a real symmetric bilinear form on a real vector space $V$. A **symmetry** of $\Phi$ is a linear involution $J$ with

$$
J^{2}=\mathrm{id},\qquad \Phi(Jv,Jw)=\Phi(v,w)\ \text{for all }v,w,\qquad \Phi(v,Jv)>0\ \text{for }v\neq0 .
$$

The second condition says $J$ is an isometry of the form; the third is its definiteness witness. Since $J^{2}=\mathrm{id}$ and $J$ preserves $\Phi$, the two conditions make $J$ self-adjoint for $\Phi$: $\Phi(Jv,w)=\Phi(Jv,J^{2}w)=\Phi(v,Jw)$.

**Theorem (every non-degenerate form has a symmetry).** Let $\Phi$ be a non-degenerate real symmetric bilinear form on a finite-dimensional real space $V$. Then $V$ has a direct sum decomposition $V=V_{+}\oplus V_{-}$ into mutually orthogonal subspaces on which $\Phi$ is positive definite and negative definite respectively, and $J=\mathrm{id}$ on $V_{+}$, $J=-\mathrm{id}$ on $V_{-}$ is a symmetry of $\Phi$.

**Proof.** Sylvester's law of inertia gives the decomposition, and non-degeneracy ensures that the two parts span: a vector orthogonal to the whole space would be zero, so no radical is left over. On a vector $v=v_{+}+v_{-}$ the three conditions are immediate, $\Phi(v,Jv)=\Phi(v_{+},v_{+})-\Phi(v_{-},v_{-})$ being a sum of two positive definite terms off zero. $\square$

**Theorem (the symmetry route always gives an inner product, hence a distance).** Let $J$ be a symmetry of $\Phi$. Then

$$
(v,w)_{J}=\Phi(v,Jw)
$$

is an inner product on $V$; the associated $\lVert v\rVert_{J}=\bigl(\Phi(v,Jv)\bigr)^{1/2}$ is a norm; $d_{J}(v,w)=\lVert v-w\rVert_{J}$ is a distance; and it induces a metric topology on $V$.

**Proof.** The map is linear in the first argument and, because $J$ is self-adjoint for the symmetric $\Phi$, linear in the second as well; it is symmetric, $(w,v)_{J}=\Phi(w,Jv)=\Phi(Jw,v)=\Phi(v,Jw)=(v,w)_{J})$; and it is positive definite because $(v,v)_{J}=\Phi(v,Jv)>0$ off zero. An inner product gives a norm by Cauchy–Schwarz, and a norm gives a distance. $\square$

**Corollary (all four forms of the algebra give a distance).** The complex bilinear, the quaternion bilinear, the complex sesquilinear and the quaternion sesquilinear form are non-degenerate and of finite dimension, so each has a symmetry and each gives a distance. **The three indefinite forms are therefore not without a norm; they are without a norm from their diagonals.**

**Remark (why the symmetry is needed, and not an absolute value).** The tempting repair of the diagonal route is to take $\lvert\Phi(\tilde{Q},\tilde{Q})\rvert^{1/2}$, and it fails. On the quaternion sesquilinear form put $v=e_0+e_1$ and $w=e_0-e_1$; then $\langle v,v\rangle_{\natural*}=\langle w,w\rangle_{\natural*}=0$ while $\langle v+w,v+w\rangle_{\natural*}=\langle 2e_0,2e_0\rangle_{\natural*}=4$. The repaired expression gives distance $0$ from $0$ to the non-zero $v$, so axiom (i) fails, and it gives $2\leq0+0$ for the triangle inequality, so axiom (iii) fails. Both failures come from the sign, not from the size, and only an involution that converts the sign into a positive contribution removes them. The symmetry does exactly that: $\langle v,\natural v\rangle_{\natural*}=2$, $\langle w,\natural w\rangle_{\natural*}=2$, $\langle v+w,\natural(v+w)\rangle_{\natural*}=4$, and the three now satisfy both axioms.

**Remark (non-degeneracy is what is needed).** The theorem uses non-degeneracy to leave no radical, and all four forms of the algebra are non-degenerate. A degenerate form would have a symmetry on its non-degenerate part only, and its radical would be invisible to the form; the question does not arise here.

## The Four Symmetries and the Coincidence of the Distances

The four symmetries are involutions already at hand in the Algebra layer, and each is named in the corpus. They are collected in the table, with the form each realifies and the identity it satisfies.

| complex form | symmetry $J$ | the symmetrised complex form $\Phi(\tilde{P},J\tilde{Q})$ | value at $\tilde{P}=\tilde{Q}$ |
|---|---|---|---|
| complex bilinear $\langle\cdot,\cdot\rangle$ | Hermitian conjugation ${}^{*}$ | $\langle\tilde{P},\tilde{Q}^{*}\rangle=\langle\tilde{P},\tilde{Q}\rangle_{*}$ | $\lVert\tilde{Q}\rVert_E^{2}$ |
| quaternion bilinear $\langle\cdot,\cdot\rangle_{\natural}$ | complex conjugation $c=\bar{\cdot}$ | $\langle\tilde{P},\bar{\tilde{Q}}\rangle_{\natural}=\langle\tilde{P},\tilde{Q}\rangle_{*}$ | $\lVert\tilde{Q}\rVert_E^{2}$ |
| complex sesquilinear $\langle\cdot,\cdot\rangle_{*}$ | identity | $\langle\tilde{P},\tilde{Q}\rangle_{*}$ | $\lVert\tilde{Q}\rVert_E^{2}$ |
| quaternion sesquilinear $\langle\cdot,\cdot\rangle_{\natural*}$ | natural conjugation ${}^{\natural}$ | $\langle\tilde{P},\natural\tilde{Q}\rangle_{\natural*}=\langle\tilde{P},\tilde{Q}\rangle_{*}$ | $\lVert\tilde{Q}\rVert_E^{2}$ |

**Remark (the symmetry preserves the realification).** When the form is bilinear and its symmetry is conjugate-linear — the first two rows — the involution $J$ preserves $\mathrm{Re}\,\Phi$ rather than the complex form $\Phi$; for example $\Phi(c\tilde{P},c\tilde{Q})=\overline{\Phi(\tilde{P},\tilde{Q})}$, whose real part is the value at $(\tilde{P},\tilde{Q})$. It is the real form that carries the distance, and the complex identities of the table are the shadow of the four equalities $\mathrm{Re}\,\Phi(\tilde{P},J\tilde{Q})=\mathrm{Re}\langle\tilde{P},\tilde{Q}\rangle_{*}$.

**Theorem (the four distances coincide).** The four symmetrised complex forms of the table are equal, all four being the complex sesquilinear form $\langle\cdot,\cdot\rangle_{*}$. Their real parts, which are the four inner products of §*The Symmetry Route*, are therefore equal as well; consequently the four distances are equal, all four being the Euclidean distance of $\lVert\cdot\rVert_E$, and the four metric topologies are one topology.

**Proof.** The four identities are read from the coordinate rules of §*Conventions*. For the complex bilinear row, $\langle\tilde{P},\tilde{Q}^{*}\rangle=\sum_\mu\varepsilon_\mu P_\mu\varepsilon_\mu\overline{Q_\mu}=\sum_\mu P_\mu\overline{Q_\mu}=\langle\tilde{P},\tilde{Q}\rangle_{*}$, since $\varepsilon_\mu^{2}=1$. For the quaternion bilinear row, $\langle\tilde{P},\bar{\tilde{Q}}\rangle_{\natural}=\sum_\mu P_\mu\overline{Q_\mu}=\langle\tilde{P},\tilde{Q}\rangle_{*}$. For the complex sesquilinear row there is nothing to do, the symmetry being the identity. For the quaternion sesquilinear row, $\langle\tilde{P},\natural\tilde{Q}\rangle_{\natural*}=\sum_\mu\varepsilon_\mu P_\mu\overline{\varepsilon_\mu Q_\mu}=\sum_\mu\varepsilon_\mu^{2}P_\mu\overline{Q_\mu}=\langle\tilde{P},\tilde{Q}\rangle_{*}$; this is the bridge identity of *The Fundamental Symmetry of the Biquaternion Algebra*, §*The Natural Conjugation as a Fundamental Symmetry*. All four are equal to the complex sesquilinear form, whose associated real inner product is $\mathrm{Re}\langle\cdot,\cdot\rangle_{*}$ and whose associated norm is $\lVert\cdot\rVert_E$ by definition. $\square$

**Remark (the first guess is inverted).** The complex sesquilinear form is not the one form that gives a distance while the others give none; it is the one form that gives the distance with no symmetry required. The four forms give the **same** distance, and the coincidence is exact, not up to equivalence.

**Remark (other symmetries give other but equivalent distances).** The symmetry of an indefinite form is not unique: the fundamental symmetries of the quaternion sesquilinear form are parametrised by the open unit ball of the vector subspace (*The Fundamental Symmetry of the Biquaternion Algebra*, §*Non-Uniqueness and the Angular Operator*), and each choice gives its own inner product and its own distance. Those distances are not equal to one another in general, but they are all norms on the finite-dimensional space, so by the next section they all induce the same topology. The coincidence above is exact for the canonical symmetries, and the uniqueness of the topology does not depend on it.

## The Uniqueness of the Topology

**Theorem (finite-dimensional norms are equivalent).** On a finite-dimensional real vector space all norms are equivalent: for any two norms there are constants $c,C>0$ with $c\lVert v\rVert_{1}\leq\lVert v\rVert_{2}\leq C\lVert v\rVert_{1}$. Consequently all such norms induce the same topology, indeed the unique Hausdorff vector-space topology on the space.

**Proof.** Standard; it reduces to the compactness of the unit sphere of $\mathbb{R}^{n}$ and the continuity of the other norm there (see *Further Reading*). $\square$

**Corollary (at most one topology, whichever symmetry is chosen).** Every norm obtainable from any of the four forms, on $\mathbb{B}$ or on any of its subspaces, with any choice of symmetry, induces the same topology, namely the Euclidean one. The layers cannot induce four topologies: they induce one topology, and the only freedom left within it is the choice of an equivalent distance.

**Remark (two reasons for one topology, one of them stronger).** There are two independent reasons the algebra carries one topology. The weaker is the equivalence of the norms, which holds for any choice of symmetries and any forms. The stronger is the coincidence of §*The Four Symmetries and the Coincidence of the Distances*, which holds for the four canonical symmetries. The first would suffice on its own; the second is stated because it is exact.

## What the Four Names Are True Of

Two readings survive the argument, and they are the ones the articles of the region actually use.

### The four level sets

Each form singles out a level set, and each level set is a different topological space. They are collected in the table; the homotopy types are those of the owning articles.

| form | level set | topology | a group? |
|---|---|---|---|
| complex bilinear | $\sum_\mu\varepsilon_\mu Q_\mu^{2}=1$ | a non-compact complex quadric, real dimension $6$ | no |
| quaternion bilinear | $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=1$ | non-compact real $6$-manifold, homotopy equivalent to $S^{3}$ | yes, the norm-one group $\mathbb{B}^\times_1$ |
| complex sesquilinear | $\lVert\tilde{Q}\rVert_E=1$ | the sphere $S^{7}$, compact | no; contains zero divisors |
| quaternion sesquilinear | $\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=1$ | $\cong S^{1}\times\mathbb{R}^{6}$, non-compact, homotopy equivalent to $S^{1}$ | no |

Only the quaternion bilinear level set is a group, and only the complex sesquilinear one is compact; the four are four distinct spaces. This is a sense in which the algebra carries four topologies, and it is a statement about subsets, not about the algebra.

The same holds of the further subsets each layer owns: the null cone of the quaternion bilinear form with its link, the null set of the quaternion sesquilinear form and its isotropic planes, the Euclidean sphere with its link and the unitary group, and the complex cone of the complex bilinear form. Each is read in the one topology of §*The Uniqueness of the Topology*, by taking the subspace topology; none requires a second topology on the algebra.

### The three isometry groups

Each form singles out the group of complex-linear maps that preserve it, and each such group is a closed subgroup of $GL_{8}(\mathbb{R})$, hence a topological group in the subspace topology.

| form | isometry group | real dimension | compact? |
|---|---|---|---|
| complex bilinear $\langle\tilde{P},\tilde{Q}\rangle=\sum_\mu\varepsilon_\mu P_\mu Q_\mu$ | $O_4(\mathbb{C})$ | $12$ | no |
| quaternion bilinear $\langle\tilde{P},\tilde{Q}\rangle_{\natural}=\sum_\mu P_\mu Q_\mu$ | $O_4(\mathbb{C})$ | $12$ | no |
| complex sesquilinear $\langle\tilde{P},\tilde{Q}\rangle_{*}=\sum_\mu P_\mu\overline{Q_\mu}$ | $U(4)$ | $16$ | yes |
| quaternion sesquilinear $\langle\tilde{P},\tilde{Q}\rangle_{\natural*}=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$ | $U(1,3)$ | $16$ | no |

The four forms induce three distinct topological groups: the two bilinear forms share $O_4(\mathbb{C})$, the two forms of dimension $16$ are separated by compactness, and no two of the three are isomorphic as topological groups. **A form induces the topological group of its isometries, and the four forms here induce three distinct such groups: this is a reading under which the phrase *topology induced by the form* is exactly true.** The dimensions are those of *The Four Pairings of the Biquaternion Algebra*, §*The Adjoints and the Three Isometry Groups*, and of *The Krein Isometry Group and Its $J$-Contractions*, §*The Group of Krein Isometries*.

## The Verdict

Every one of the four forms of the biquaternion algebra gives a distance, and the four distances are the same, the Euclidean one. The three indefinite forms fail the **diagonal route** — their diagonals vanish on the non-zero $e_0+e_1$, $e_1+ie_2$ and $e_0+e_1$, and the square root of an indefinite diagonal fails the triangle inequality even where it is real — but they do not fail to give a distance: the symmetry route supplies one for every non-degenerate form, by Sylvester, and for these three the symmetries are the Hermitian conjugation, the complex conjugation and the natural conjugation, each of which returns the complex sesquilinear form. The algebra $\mathbb{B}$ therefore carries one topology: the four distances coincide, and independently all norms on a finite-dimensional real space are equivalent. **The sub-categories are named for the structure each form induces beyond the common distance — its diagonal and signature, its null set and level sets, its isometry group — and the names are true of those structures, not of inequivalent topologies on the algebra.** The units are decided by the quaternion bilinear norm and their topology by the complex sesquilinear form, which is the same statement in the language of the group (*The Biquaternion Unit Group as a Topological Group*, §*The Topology of the Group*).

**Remark (the caveat belongs to the reader).** The names are the author's, and the corpus keeps them; this article exists so that the caveat is stated once and can be cited rather than repeated. Any later article that writes of a statement *read in the topology induced by the quaternion sesquilinear form* means the structure the quaternion sesquilinear form induces, read in the one Euclidean topology.

## Summary

A non-degenerate form reaches a distance by one of two routes. The diagonal route, reading the length from $\Phi(\tilde{Q},\tilde{Q})$ alone, gives a norm exactly when the form is positive definite, and of the four diagonals only the complex sesquilinear one is: the complex bilinear diagonal vanishes on the non-zero $e_0+e_1$, the quaternion bilinear diagonal on the non-zero $e_1+ie_2$, the quaternion sesquilinear diagonal on the non-zero $e_0+e_1$, and the square root of an indefinite diagonal fails the triangle inequality even where it is real, as on the centre where $\sqrt3+\sqrt3<4$. The symmetry route, reading the length from $\Phi(v,Jv)$ for a symmetry $J$, gives an inner product and a distance for **every** non-degenerate form, by Sylvester, and it is the route that decides the question: the three indefinite forms are not without a norm, they are without a norm from their diagonals. The symmetries of the four forms are the Hermitian conjugation, the complex conjugation, the identity and the natural conjugation, and each returns the complex sesquilinear form, so the four distances coincide exactly with the Euclidean distance; independently, all norms on a finite-dimensional real space are equivalent, so one topology is all the algebra can carry. What the layers do own is four level sets — the complex quadric; the norm-one group, homotopy equivalent to $S^{3}$; the sphere $S^{7}$; the hyperboloid $S^{1}\times\mathbb{R}^{6}$ — and three isometry groups — $O_4(\mathbb{C})$ of dimension $12$, shared by the two bilinear forms, $U(4)$ of dimension $16$ and compact, and $U(1,3)$ of dimension $16$ and non-compact — which are distinct topological objects. The names are true of those structures, not of four topologies on the algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\lVert\cdot\rVert$, axioms (i)–(iii) | the norm of a real vector space |
| $\Phi$ positive definite $\iff$ $\bigl(\Phi(\cdot,\cdot)\bigr)^{1/2}$ is a norm | the diagonal route |
| $\langle e_0+e_1,e_0+e_1\rangle=0$, $\langle e_1+ie_2,e_1+ie_2\rangle_{\natural}=0$, $\langle e_1,e_1\rangle_{\natural*}=-1$ | the witnesses that stop the diagonal route |
| $J^{2}=\mathrm{id}$, $\Phi(Jv,Jw)=\Phi(v,w)$, $\Phi(v,Jv)>0$ | a symmetry of the form |
| $(v,w)_{J}=\Phi(v,Jw)$ | the inner product the symmetry produces |
| Sylvester decomposition $V=V_{+}\oplus V_{-}$ | every non-degenerate form has a symmetry, hence a distance |
| $\langle\tilde{P},\tilde{Q}^{*}\rangle=\langle\tilde{P},\tilde{Q}\rangle_{*}$ | the symmetry of the complex bilinear form is ${}^{*}$ |
| $\langle\tilde{P},\bar{\tilde{Q}}\rangle_{\natural}=\langle\tilde{P},\tilde{Q}\rangle_{*}$ | the symmetry of the quaternion bilinear form is $c=\bar{\cdot}$ |
| $\langle\tilde{P},\natural\tilde{Q}\rangle_{\natural*}=\langle\tilde{P},\tilde{Q}\rangle_{*}$ | the symmetry of the quaternion sesquilinear form is $J={}^{\natural}$ |
| the four symmetrised forms are equal | the four distances coincide |
| all norms equivalent, dimension finite | one topology, whatever the symmetry |
| $\mathbb{B}^\times_1$, $S^{7}_{E}$, $\{\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=1\}$, $\{\sum_\mu\varepsilon_\mu Q_\mu^{2}=1\}$ | the four level sets |
| $S^{3}$, $S^{7}$, $S^{1}\times\mathbb{R}^{6}$ | their homotopy types |
| $O_4(\mathbb{C})$ (twice), $U(4)$, $U(1,3)$ | the isometry groups; dimensions $12$, $16$, $16$; compactness no, yes, no |

## Further Reading

- *Introduction to Topology on the Biquaternions* (`articles_maths/introduction-to-topology-on-the-biquaternions.md`), the companion that presents the four layers and the comparison table
- *The Four Biquaternion Complex Products* (`articles_maths/the-four-biquaternion-complex-products.md`), for the four products whose scalar parts are the four forms
- *The Four Pairings of the Biquaternion Algebra* (`articles_maths/the-four-pairings-of-the-biquaternion-algebra.md`), for three of the forms, their Gram matrices, their signatures, their mutual determination and their isometry groups
- *The Fundamental Symmetry of the Biquaternion Algebra* (`articles_maths/the-fundamental-symmetry-of-the-biquaternion-algebra.md`), for the symmetry $J={}^{\natural}$, the bridge identity and the non-uniqueness of the symmetry
- *The Euclidean Topology of the Biquaternion Algebra* (`articles_maths/the-euclidean-topology-of-the-biquaternion-algebra.md`), for the topology the complex sesquilinear form induces and for the sphere $S^{7}_{E}$
- *The Krein Level Sets and the Hyperbolic Structure* (`articles_maths/the-krein-level-sets-and-the-hyperbolic-structure.md`), for the level sets $S^{1}\times\mathbb{R}^{6}$ and $S^{5}\times\mathbb{R}^{2}$
- *The Krein Isometry Group and Its $J$-Contractions* (`articles_maths/the-krein-isometry-group-and-its-j-contractions.md`), for the group $U(1,3)$, its dimension and its maximal compact subgroup
- *The Biquaternion Unit Group as a Topological Group* (`articles_maths/the-biquaternion-unit-group-as-a-topological-group.md`), for the sentence that the norm defines the group but not its topology, and for $\mathbb{B}^\times_1\simeq S^{3}$
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the real forms, their signatures and the audit of the norm axioms
- Walter Rudin, *Functional Analysis*, 2nd ed. (McGraw-Hill, 1991), Theorem 1.21, for the equivalence of the norms on a finite-dimensional space and the uniqueness of its Hausdorff vector-space topology
