# __Changes Linked to the Biquaternion Formalism Instead of the Gamma Matrices__

## Scope

This file is a **review of one migration**, not an article and not an entry of a menu. It reads the physics corpus after the withdrawal of the gamma frame from the bodies, states what the withdrawal changed, and lists the physics that the cell form makes visible and the gamma form did not. The counts are read off the files, the algebra was recomputed, and every number below is checked.

One article was modified in the course of the review: *Thomson and Compton Scattering: the Biquaternion Polarization Algebra*, whose body was the last one written in column notation. Section 1 records the change.

The corpus rewrote its spinors and its Dirac operators as actions on the algebra, $\psi\mapsto a\psi b$, and moved the five gammas to one closing appendix per article. The published argument for doing so is *Why the Biquaternion Formalism Instead of Gamma Matrices*. That article answers *may we*. This note answers a different question: *what did it buy*.

The answer is not "a cleaner notation". Three objects that the gamma notation wrote with one symbol are now three symbols, and one equation that the gamma notation wrote once is now a pair. Both changes are forced by the algebra, not chosen. They also expose two ceilings and one ambiguity that the old notation could keep out of sight.

## Review of the Earlier Draft

Two reviews, both recorded, because the second corrected an error the first revision introduced.

| round | the point raised | verdict |
|---|---|---|
| 1 | the rank set $\{0,1,2,4\}$ did not say which rank it meant | accepted: the two ranks are now named, kept apart, and shown independent in both directions |
| 1 | the gauge ceiling read as a no-go result for physics | accepted: restricted to the programme that asks the gauge group to come out of the algebra |
| 1 | the rank-two limitation was overstated | accepted: a limitation of the primitive, not of the algebra |
| 1 | the $\mathbb{Z}/2$ item carried more weight than it earns | accepted: a fact about the Fock representation, not the bare algebra |
| 1 | the $4\times4$ rank lies in $\{0,2,4\}$, not $\{0,1,2,4\}$ | **refused**, with a computation |
| 2 | the revision said the two ranks "are the same number" for a cell | accepted: an error introduced by the fix |

**The refusal.** The objection computes the rank of a single left factor, $\operatorname{rank}L_Q=2\operatorname{rank}\mathsf M_2(Q)$, and applies it to the cell. A cell multiplies both sides, $T_{Q,P}=\mathsf M_2(P)^{\mathrm T}\otimes\mathsf M_2(Q)$, and the rank of a Kronecker product is the product of the ranks, so $\operatorname{rank}T_{Q,P}=\operatorname{rank}\mathsf M_2(Q)\cdot\operatorname{rank}\mathsf M_2(P)$. The nine rank pairs give exactly $\{0,1,2,4\}$; the value one occurs whenever both factors have rank one. The set $\{0,2,4\}$ is right for $L_Q$ and wrong for the cell. Item 2 of §5 now carries the computation and names the confusion as the trap, because it is the mistake a reader will make.

**The second round.** The revision that answered the first review then wrote that the coefficient rank and the matrix rank "are the same number" for a cell. That is false, and item 1 of the same section was the counterexample: $T_{e_t,e_t}$ has length one and matrix rank four. The sentence came from attaching a computation of the matrix rank to a claim about the coefficient rank. Both directions of the independence are now exhibited, and §7 carries the rows.

The two claims the reviews singled out as the payoff, §4.2 and §4.4, were rechecked and left unaltered.

## 1. The state of the withdrawal

The physics corpus holds 404 articles. Ninety-one of them carry the closing appendix `## Appendix — The Gamma Formulation`. The other 313 never wrote a gamma generator in the first place — most of them are classical, thermodynamic or algebraic — so the absence of an appendix there is not an unfinished migration.

Two bodies name a gamma on purpose:

- *Why the Biquaternion Formalism Instead of Gamma Matrices*, whose subject is the comparison, and which therefore displays the five cells next to the five gammas.
- *Conventions of the Frames*, which names the frames $\gamma_\mu[\mathbb{B}]$ and $\gamma_\mu[\mathbb{M}_-]$ because a frame is its subject. It carries no appendix, and it should not: it is the one article where the frame is the datum.

One stray stood outside this design, and it has since been repaired. In *Thomson and Compton Scattering: the Biquaternion Polarization Algebra*, the body wrote the spin sum of the Dirac trace as $\sum_s \xi_s\bar{\xi}_s = \gamma_\mu p_\mu + m$, in a file with no appendix. The gamma there was neither an exception nor a coordinate; it was a leftover, and it was the only body in the corpus still in column language. The article was rewritten to the corpus form: the sum is now the cell $D(p)=\mathsf C_\mu p_\mu+m\,T_{e_t,e_t}$, the spin-resolved sum is $D_s(p)=\tfrac12 D(p)(1+\mathsf C_5\mathsf C_\mu s_\mu)$, and the article carries the standard closing appendix. The old citation was also wrong — the spin sums live in *Solutions and the Non-Relativistic Limit*, not in *The Dirac Equation in Biquaternionic Form* — and the object was called a projector without the normalisation that makes it one.

The remaining bodies that carry the letter write another quantity. In *Dirac Matter: Graphene, Dirac Cones and Topological Insulators* the $\gamma_0\approx2.8$ eV is the nearest-neighbour hopping; in *Causality and the Light Cone*, *Velocity Space as Hyperbolic Geometry*, *Paravectors and the Geometry of Spacetime* and *Noether's Theorem* the $\gamma_1,\gamma_2,\gamma_{\mathrm{rel}}$ are Lorentz factors; in *SU(3) Representations and the Gell-Mann–Okubo Mass Formula* the $\gamma_2$ is a mass-formula coefficient. These are homonyms of the generator, not uses of it, and no appendix is owed for them.

The vocabulary the rewrite spread is the measure of its reach: 43 articles now state the chiral pair explicitly, 87 speak of a two-sided operator, 169 of chirality, 86 of the central sign $\chi$, and 70 of the Peirce decomposition. The rewrite did not touch only the Dirac articles; it spread a distinction into every article that touches a spinor.

## 2. The dictionary, stated once

The five generators are cells, $T_{a,b}=L_aR_b$:

| generator | cell | left multiplier | right multiplier |
|---|---|---|---|
| $\mathsf C_0$ | $iT_{e_t,e_x}$ | $i e_t$ (central) | $e_x$ |
| $\mathsf C_1$ | $iT_{e_x,e_y}$ | $e_x$ | $e_y$ |
| $\mathsf C_2$ | $iT_{e_y,e_y}$ | $e_y$ | $e_y$ |
| $\mathsf C_3$ | $iT_{e_z,e_y}$ | $e_z$ | $e_y$ |
| $\mathsf C_5$ | $-iT_{e_t,e_z}$ | $-i e_t$ (central) | $e_z$ |

Two rows of the table — the timelike generator and the chirality — have a central left multiplier, and that is the source of the first two results below. The list also misses an object: the identity is the cell $T_{e_t,e_t}$, and the mass multiplies it.

## 3. Five things that became visible

### 3.1 Chirality is a right multiplication

$$
\Gamma=-iT_{e_t,e_z}=-i\,R_{e_z},\qquad \Gamma^2=e_t,\qquad \{\Gamma,\mathsf C_\mu\}=0 .
$$

Written as a cell, chirality acts only after the field. It has no left multiplier. Verified: the residual of $\Gamma+iR_{e_z}$ is $0$, and $\Gamma$ anticommutes with all four generators to residual $0$.

The sharper statement is a negative one. No element $a\in\mathbb{B}$ has $L_a=\Gamma$. Fitting $\Gamma$ against the four-dimensional space $\{L_a\}$ leaves a residue of $1$ in one entry, so $\Gamma$ is not a left multiplication at all. Chirality is therefore not something the algebra does to a field from the left; it is something done to the field from the right. In gamma notation the distinction has no name, because $\gamma_5$ acts on a column, and a column has one side only.

### 3.2 Time and chirality act on one side, space acts on both

This is the observation the corpus does not state in one place, and it is exact.

| object | cell | side used |
|---|---|---|
| mass | $mT_{e_t,e_t}=m\,\mathbf{1}$ | neither (the centre) |
| timelike generator $\mathsf C_0$ | $iT_{e_t,e_x}=R_{i e_x}$ | right only |
| chirality $\Gamma=\mathsf C_5$ | $-iT_{e_t,e_z}=-iR_{e_z}$ | right only |
| spatial generators $\mathsf C_k$ | $iT_{e_k,e_y}$ | both |

The reason is structural and not a feature of the reference frame. A cell whose left multiplier is central is a multiple of a right multiplication: $T_{\lambda e_t,b}=\lambda R_b$. The timelike generator and the chirality both have $e_t$ on the left, up to the central $i$, so both are one-sided in every frame. The spatial generators have $\vec e_k$ on the left, which is not central, so they are genuinely two-sided, and the anticommutator $\{\mathsf C_0,\mathsf C_k\}=0$ comes entirely from the right factors, $R_{e_y}R_{e_x}=-R_{e_x}R_{e_y}$.

The one-sidedness of $\mathsf C_0$ and $\gamma_5$ was checked in three frame pairs, $(\beta,\delta)=(\vec e_y,\vec e_x)$, $(\vec e_x,\vec e_y)$, $(\vec e_z,\vec e_x)$, with residual $0$ in each, together with the Clifford relations, also residual $0$ in each. The spatial generators fail the same test with residual $2$, as they must.

Read as physics, the table says that time and chirality are properties of the *second* side, space is a property of the *pair* of sides, and the mass is central. This is the same content as the corpus's statement that the fourth Clifford direction *is* the second side, seen from the other end: the fourth direction is one-sided for the same reason the chirality is.

### 3.3 The mass is the identity cell, and the gamma list cannot name it

$$
m\,T_{e_t,e_t}\psi=m\,e_t\psi e_t=m\psi .
$$

The gamma list names five of the sixteen basis elements and leaves the scalar unnamed. The mass is exactly the unnamed one. In the gamma display the same term is $m\psi=m\gamma_0^2$, which is a product of two gammas, not a sixth gamma, and the reader is left with the impression that the mass is the absence of an operator.

The cell list names it, and the naming has a consequence. The mass is central, so it commutes with every generator; a scalar mass therefore cannot appear as a single root of the d'Alembertian, and this is the origin of the duplication in §4.

### 3.4 Hodge duality is the central imaginary

$$
\star\tilde F=-i\tilde F .
$$

Self-duality is an eigenvalue of left multiplication by $i$, and the duality rotation $\exp(-i\theta)$ is a $\mathrm{U}(1)$ of the centre: internal, exact for the sourced equations, Lorentz-trivial, of order four. In gamma notation the Hodge dual is $\gamma_5$ dressed with an epsilon symbol, and the rotation is a transformation of the field strength; in the cell form the rotation *is* a phase of the algebra, and the epsilon symbol disappears.

The self-dual and anti-self-dual halves then come out as the projectors $\tfrac12(1\pm i\star)$ on the vector part, and the two helicities of the massless field are the two eigenspaces. The corpus states this without ever writing a gamma.

### 3.5 The EDM insertion is minus a material vector

The electric-dipole insertion is anti-Hermitian and its magnetic partner is Hermitian:

$$
\sigma_{0k}\mathsf C_5\ \text{anti-Hermitian},\qquad \sigma_{ij}\ \text{Hermitian},
$$

both to residual $0$ over all pairs. The identity behind the placement is exact:

$$
\sigma_{0k}\mathsf C_5=i\,\mathbf{1}\otimes\sigma_k=-\mathsf M_2(\vec e_k),
$$

on the spinor slot, for $k=1,2,3$, residual $0$. So the CP-odd insertion *is* a vector of the material sector, with a minus sign, and the explicit $i$ that makes the Lagrangian Hermitian is the marker of that sector rather than a convention.

The gain is that "the EDM operator is anti-Hermitian" becomes "the EDM operator is (minus) a spatial direction". The first is a property of a matrix; the second is a property of the algebra.

## 4. The duplication

Chirality, once it is a two-sided notion, duplicates equations. The corpus does this in a specific way, and the reason is algebraic rather than stylistic.

### 4.1 The pair that replaces the equation

The massive Dirac equation is not one equation:

$$
\tilde\nabla\tilde\Psi_R=m\tilde\Psi_L,\qquad \tilde\nabla^{\natural}\tilde\Psi_L=m\tilde\Psi_R .
$$

At $m=0$ the two lines decouple into two independent Weyl equations, one per chiral half. The mass is the only thing that couples them, and it couples them *off the diagonal*, because no element of $\mathbb{B}$ acting on the left can move between the halves.

The duplication is not confined to the free equation. The same split appears in the covariant derivative, in the adjoint equation, in the axial current, and in the plane-wave solutions, and 43 articles now state the pair in this form.

### 4.2 Why the scalar mass forces a pair

This is the strongest single result the rewrite exposed, and it is in *The First-Order Root of the Biquaternion Klein–Gordon Operator*.

A first-order operator $\mathsf D+B$ squares to $\Box-\mu^2$ only if $\{B,\mathsf C_\mu\}=0$ for all $\mu$. The anticommutant of the four generators is one-dimensional, and the only element in it is $\mathsf C_5$:

$$
B=c\,\mathsf C_5,\qquad B^2=c^2=-\mu^2,\qquad c=\pm i\mu .
$$

So a **single** root exists, but the mass it carries is a **pseudoscalar** mass, parity-odd, diagonal in chirality, and not the mass of the Standard Model. The **scalar** mass commutes with the generators instead of anticommuting, so no single operator of the form $\mathsf D+\mu$ squares to the wave operator. What exists is the factorisation

$$
\mathsf D_{\mathrm{sc},-}\mathsf D_{\mathrm{sc},+}=\left(\mathsf D-\mu\right)\left(\mathsf D+\mu\right)=\left(\Box-\mu^2\right)\mathbf{1},
$$

whose two factors carry opposite mass, and the physical equation is one factor. The pair is the price of a scalar mass. It is not an arbitrary choice of basis and not a redundancy of notation.

This is the sharpest instance of what the migration was for, and the gamma notation hides it completely: there, $m$ multiplies the identity and $\gamma_5$ is another matrix, and both look like matrices; here one is central and the other is the volume cell, and the two behave differently under the anticommutator.

### 4.3 What the duplication buys

The duplication is not only a cost.

- **Chirality becomes a real-structure notion.** The two halves are invisible to $\mathbb{B}$ as a complex algebra, where both minimal left ideals are copies of the same module; they appear only through the conjugate module and the complexification. The exercise *Chirality and the Weyl Spinors* states this as its main finding.
- **The Lorentz action separates under boosts and coincides under rotations.** A boost rotor has an imaginary vector part, so the two halves transform by inverse matrices; a rotation rotor is a real quaternion, so they transform alike. In gamma notation the two statements are one statement about $\gamma_5$ commuting with the Lorentz generators.
- **The double cover becomes a kernel statement.** The sign cancels on a four-vector because the four-vector is bilinear, and it does not cancel on a spinor. One factor of $g$ versus two. The duplication is what makes the two actions different in kind.

### 4.4 Three objects that the gamma notation calls $\gamma_5$

| role | gamma | cell or module object | what it is | squares to |
|---|---|---|---|---|
| grading of the Dirac module | $\gamma_5$ | $\chi=i\tilde\Xi_{\mathrm{ad}}$, represented by $-iT_{e_t,e_z}$ | central in $\mathbb{C}\otimes\mathbb{B}$ | $e_t$ |
| chirality cell of the frame | $\gamma_5$ | $\Gamma=-iT_{e_t,e_z}=-iR_{e_z}$ | the cell in the reference frame | $e_t$ |
| copy index of the regular module | $\gamma_5$ | $P=R_{i\vec e_z}$ | inner, non-central, left $\mathbb{B}$-linear | $e_t$ |

On the Dirac module the matrices of $\Gamma$ and of $P$ are $\operatorname{diag}(-1,-1,+1,+1)$ and its negative; the sign is one bit of convention and the corpus fixes it once. What separates the three objects is not the numbers but the module they act on and whether they are central. $\chi$ grades $S$ against $S^{\mathrm c}$, the two halves being inequivalent modules. $P$ labels two copies of the same module $S$. $\Gamma$ is the representative of $\chi$ in the frame, valid only when the frame is named.

The rewrite gives three symbols to three objects. That is the whole gain, and it is the place where the old notation was actively misleading rather than merely inconvenient: a single symbol $\gamma_5$ covered a central grading, a frame cell, and a copy index, and the three agree numerically exactly in the case where the conflation is harmless.

## 5. Surprising and unusual points

Eight items, in decreasing order of how far they are from what the gamma notation suggests.

1. **The identity is a single product of full matrix rank.** $T_{e_t,e_t}$ has length one and matrix rank four. The intuition "one cell, low rank" is wrong in the only case that matters, the mass.

2. **No cell has matrix rank three, and the two ranks are independent quantities.** Three numbers are in play, and they must be kept apart.

    - **Length**, the coefficient rank $\ell(M)=\operatorname{rank}c(M)$ of the element in the sixteen-product basis. It is one for a single product, whatever that product is, and it runs over $\{0,1,2,3,4\}$ in general, because a sum of three products with independent coefficients has length three.
    - **Matrix rank**, the rank of the $4\times4$ matrix of $M$ on the regular module. For a cell, $T_{Q,P}$ acts as $\mathsf M_2(P)^{\mathrm T}\otimes\mathsf M_2(Q)$, and the rank of a Kronecker product is the product of the ranks, so $\operatorname{rank}T_{Q,P}=\operatorname{rank}\mathsf M_2(Q)\cdot\operatorname{rank}\mathsf M_2(P)\in\{0,1,2,4\}$. Three is impossible for the matrix rank of a cell.
    - **The trap**, a single left factor: $\operatorname{rank}L_Q=2\operatorname{rank}\mathsf M_2(Q)$, so the range $\{0,2,4\}$ — correct for $L_Q$ — is wrong for the cell, because the right factor multiplies the rank rather than contributing a second factor of two.

    The two numbers are independent in both directions, and *Why the Biquaternion Formalism Instead of Gamma Matrices* says so in one line with the same example: the chiral projector $P_+=\tfrac12(T_{e_t,e_t}-iT_{e_t,e_z})$ has matrix rank two and length one, and a rank-one matrix can have length four. Both were recomputed. The mass is a second instance of the first direction, $T_{e_t,e_t}$ having length one and matrix rank four. The reverse — matrix rank one, length four — is any rank-one $4\times4$ matrix drawn at random on $\mathbb{C}^4$, which is not a single product in the sixteen-basis. Neither number is a proxy for the other, and a statement about one says nothing about the other.

3. **A dull-looking operator is outside the cone.** $T_{e_t,e_t}+T_{e_x,e_x}$ has length two and matrix rank two, and is not a single product; no decomposable frame change makes it one, since multiplying by single products on both sides leaves the length at two, checked on one hundred such products. A sum of two ordinary cells is a genuinely different object, and the gamma form has no way to say so.

4. **The fourth direction is the second side.** Time is not a fourth quaternion unit; it is a right multiplication. This is why no element of $\mathbb{B}$ anticommutes with all three $\vec e_k$, and why the first-order root lives in $\mathbb{B}\otimes\mathbb{B}^{\mathrm{opp}}$ rather than in $\mathbb{B}$.

5. **Two different $\mathbb{Z}/2$.** Besides the spinor double cover there is the central sign: on the fermionic Fock space $\Gamma(-I)=(-1)^{N}$, so a $2\pi$ rotation *is* the fermionic parity. This is a statement about the Fock representation and not about the bare algebra — it needs the mode operators and their anticommutation to be true — so it is weaker in kind than the statements of §3.1 and §4.2, which hold in the algebra alone. The two signs are the same sign, and the corpus says so in one line.

6. **A gauge ceiling that the algebra states itself.** The ceiling is a statement about one programme, and it must be quoted with that restriction: it governs any construction that asks the **gauge group itself** to come out of the algebra, and says nothing against gauge theory built on an internal fibre. Within that programme the statement is exact. Left multiplication acts on both chiral halves alike, so the framework's non-abelian action is vector-like, and the centre gives at most a locked ratio of left and right charges. The **intrinsic** compact group of $\mathbb{B}$ is $\mathrm{U}(2)$, of real dimension four; $\mathrm{SU}(3)$ needs eight and cannot sit inside it; the smallest carrier that contains it is $M_2(\mathbb{B})$, whose intrinsic group is $\mathrm{U}(4)$, and that is an embedding into a larger group rather than the algebra's own. The corpus states the ceiling in those words and treats it as a result, not a gap.

7. **A rank-two limitation of the norm primitive.** The quadratic invariant $\langle\tilde F\rangle_{\natural}=\tilde F\tilde F^{\natural}$ carries one algebra slot, so it cannot host $\operatorname{Tr}(F\wedge F)$ or the index density. The limitation is in the primitive, not in the algebra: $M_4(\mathbb{C})$ supports $\operatorname{Tr}(MN)$ perfectly well, and the density can be written in components with that trace. What is missing is a second contraction **native to the framework's own bilinear**; the trace has to be imported, and an imported trace is not an object of the biquaternion-norm calculus. The instanton article and the index-theorem article say exactly this, and it is the same statement twice.

8. **The mass shell is written twice, and the two writings differ in degree.** On a four-position the determinant is $s^4$, on a four-momentum $m^4c^4$; the $2\times2$ picture gives the first power. An identity of the $2\times2$ picture holds only to the second power in the regular picture, and the corpus records which is in use.

## 6. Where the rewrite is fragile

Three weak points, stated plainly.

**The central phase has two readings and the corpus has not chosen.** If the biquaternion field is identified with the regular module $S\oplus S$, a central phase acts vector-like, equally on both halves. If it is identified with the Dirac module $S\oplus S^{\mathrm c}$, the same phase acts axially, with $ϙ_R=-ϙ_L$. The passage between the two is the real structure. This "two-$i$" question decides whether the framework's abelian factor is vector-like or axial, and at least three articles record it as open. Through the hypercharge assignment it also decides whether the framework can carry the observed chiral fermion content, so it is the one open item with empirical consequences. It is the one place where the duplication of §4 produces an ambiguity rather than a result.

**The Peirce split is easy to mistake for the chiral split.** $S\oplus S$ and $S\oplus S^{\mathrm c}$ are the same real dimension and different modules, and several articles must say repeatedly that the Peirce idempotents do not project onto chirality. The rewrite made the distinction nameable; it did not make it automatic.

**The real forms are not covered by the dictionary.** Over $\mathbb{C}$ the dictionary is exact. Over $\mathbb{R}$ the generators span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ while the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$. Every appendix states this, and any article that uses a real structure must restate it locally.

And the one bookkeeping item has been closed: the Thomson article was rewritten to the cell form, and the last gamma in a body is gone.

## 7. Verification log

Recomputed with the fixed matrix model $\mathsf M_2(e_t)=I_2$, $\mathsf M_2(\vec e_k)=-i\sigma_k$, $\mathsf M_2(i)=iI_2$, on the four-dimensional regular module.

| claim | residual |
|---|---|
| Clifford relations of the five cells, reference frame | $0$ |
| Clifford relations in the pairs $(\vec e_x,\vec e_y)$ and $(\vec e_z,\vec e_x)$ | $0$ |
| $\mathsf C_5^2=\mathbf 1$ | $0$ |
| $\mathsf C_5$ anticommutes with the four generators | $0$ |
| $\Gamma=\mathsf C_5=-iR_{e_z}$ | $0$ |
| $\Gamma$ is not a left multiplication $L_a$ | best fit off by $1$ |
| $\mathsf C_0$ is a pure right multiplication | $0$ |
| $\gamma_5$ is a pure right multiplication, three frames | $0$ |
| $\mathsf C_k$ is not a pure right multiplication | $2$ |
| Peirce sign $P=R_{i\vec e_z}$ squares to $\mathbf 1$ | $0$ |
| $P$ commutes with every left multiplication | $0$ |
| $\operatorname{rank}(T_{e_t,e_t})=\operatorname{rank}\mathbf 1=4$, length $1$ | exact |
| length of each of the sixteen basis cells | $1$, all sixteen |
| matrix rank of each of the sixteen basis cells | $4$, all sixteen |
| a sum of three products with independent coefficients: length $3$, matrix rank $4$ | exact |
| a sum of four: length $4$, matrix rank $4$ | exact |
| a generic rank-one matrix on $\mathbb{C}^4$: length $4$, matrix rank $1$ | residual $9\times10^{-16}$ |
| the chiral projector $P_+=\tfrac12(T_{e_t,e_t}-iT_{e_t,e_z})$: matrix rank $2$, length $1$ | exact |
| length of $T_{e_t,e_t}+T_{e_x,e_x}$ after $100$ frame products $XMY$ | stays $2$ |
| $T_{e_t,e_t}+T_{e_x,e_x}$: eigenvalues $0,0,2,2$ | matrix rank $2$, length $2$ |
| $T_{Q,P}=\mathsf M_2(P)^{\mathrm T}\otimes\mathsf M_2(Q)$ on the regular module | $0$ |
| $\operatorname{rank}(T_{Q,P})=\operatorname{rank}\mathsf M_2(Q)\cdot\operatorname{rank}\mathsf M_2(P)\in\{0,1,2,4\}$, nine rank pairs | exact |
| $\operatorname{rank}L_Q=2\operatorname{rank}\mathsf M_2(Q)$ (the trap) | exact |
| $\operatorname{rank}(T_{e_t,e_t}+T_{e_x,e_x})=2$ | exact |
| $\operatorname{rank}$ of the minimal Dirac operator $=2$ | exact |
| $\sigma_{0k}\mathsf C_5$ anti-Hermitian, all $k$ | $0$ |
| $\sigma_{ij}\mathsf C_5$ Hermitian, all $i<j$ | $0$ |
| $\sigma_{0k}\mathsf C_5=-\mathsf M_2(\vec e_k)$ on the spinor slot | $0$ |
| $\Gamma$ and $P$ differ | $2$ |
| $D_s^2=2mD_s$, $\operatorname{rank}D_s=1$, $\operatorname{Tr}D_s=2m$ | $0$ |
| the two spin cells are mutually orthogonal | $0$ |
| $D_{+}+D_{-}=D(p)$ and $\tfrac{1}{2m}\bigl(D(p)+m\,T_{e_t,e_t}-\mathsf C_\mu p_\mu\bigr)=1$ | $0$ |

## 8. Open questions

- **Does the vector-like reading survive the axial one?** The two-$i$ question above, and the only open item that gates a programme rather than a paragraph. Deciding which module the field inhabits fixes whether the abelian factor is vector-like or axial, which fixes the hypercharge assignment, which decides whether the framework can reproduce the observed chiral fermion content at all. It is a modelling decision with empirical consequences, so it is left to the author and not settled here by preference.
- **Is the pseudoscalar root physical anywhere?** The single root $\mathsf D\pm i\mu\mathsf C_5$ is parity-odd and is not the Dirac mass. If the framework has a natural home for a pseudoscalar mass, the corpus has not named it.
- **Can the three $\gamma_5$ roles be separated in the appendix too?** The appendices say "$\gamma_5$" once, distinguish the cell from the central grading in one sentence, and never mention the Peirce copy sign $P$. A reader who consults only the appendix sees two objects where there are three.
- **Is the spin-resolved cell used anywhere else?** The Thomson article now states $D_s(p)=\tfrac12 D(p)(1+\mathsf C_5\mathsf C_\mu s_\mu)$, verified as a pair of orthogonal rank-one cells. No other article states it, although Møller, Bhabha and the polarized cross-sections all need it; propagating it is the obvious next step.

## Summary

The withdrawal of the gamma frame changed more than the notation.

**What became visible.** Chirality is a pure right multiplication, and no left multiplication equals it. Time and chirality are one-sided in every frame; space is two-sided; the mass is central. The mass is the identity cell, the one object the five-name gamma list cannot name. Hodge duality is the central imaginary. The EDM insertion is minus a spatial direction of the material sector.

**What became duplicated.** The Dirac equation is a chiral pair, because a scalar mass has no single first-order root: the only single root carries a pseudoscalar mass. At $m=0$ the pair decouples into two Weyl equations. The duplication is the algebraic form of the statement that chirality is a real-structure notion, and it is why the double cover cancels on a four-vector and not on a spinor.

**What became separable.** Three objects that the gamma notation called $\gamma_5$ — the central grading $\chi$, the frame cell $\Gamma$, the Peirce copy sign $P$ — now have three names and three roles.

**What stays fragile.** The central phase has two readings and no decision; the Peirce split is easy to confuse with the chiral split; the dictionary is complex-linear and does not cover the real forms.
