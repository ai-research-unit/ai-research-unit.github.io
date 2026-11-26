# __The Instanton Monad, the Euclidean Route, and the Passages Moved Here__

## Introduction

**This article holds the twistor material that the rest of the physics corpus carried, moved here verbatim and left whole.** Two of the corpus's articles developed a subject through twistor space rather than through the algebra: *The ADHM Construction and Biquaternion Instanton Data*, whose monad description of the instanton is the Penrose–Ward correspondence, and *The SO(4) Route to the Euclidean Frame*, whose external programme is Woit's Euclidean unification and is stated on projective twistor space. **Both passages are reproduced below without alteration**, so that the corpus keeps the content and loses only the scattering.

**Why a separate home is the right one.** A twistor is a point of a space that is not spacetime, and a construction written on that space is not a statement about a metric, a frame or a field in the algebra. **It is a statement in a different theory.** Filing such passages beside the articles they came from made the corpus look as though the framework contained them; **filed here, they are marked for what they are: neighbouring programmes, recorded and not adopted.**

**The three units below stand in their original order of dependence**: the monad, which is a geometric restatement of the ADHM data; the Euclidean route, which needs projective twistor space to make its internal groups; and the recomputation of one generation, which is the part of that route that can be checked.

## The Instanton Monad and the Quaternionic Geometry

The ADHM equations are the algebraic shadow of a holomorphic-geometric statement, and the statement is quaternionic. The twistor space of the compactified four-space $S^4$ is the complex projective three-space $\mathbb{CP}^3$, which fibres over $S^4$,

$$
\mathbb{CP}^1\;\hookrightarrow\;\mathbb{CP}^3\;\longrightarrow\;S^4 ,
$$

with fibre $\mathbb{CP}^1\cong S^2$ over each point. The fibre is the space of complex structures compatible with the quaternionic structure of $\mathbb H_{\mathbb B}$: a point of $S^4$ is a quaternionic line, and the complex structures of that line are a $\mathbb{CP}^1$. This is the geometric form of the statement that $\mathbb H_{\mathbb B}$ admits a sphere of complex structures, and it is why the self-duality condition can be a holomorphic condition.

The Penrose–Ward correspondence states that a self-dual connection on $S^4$ is equivalent to a holomorphic rank-two vector bundle $E$ on $\mathbb{CP}^3$, trivial on each real line, and that the instanton number is the second Chern number of $E$. The ADHM data are the algebraic description of $E$ as a **monad**, a three-term exact sequence of holomorphic bundles,

$$
0\;\longrightarrow\;\mathcal O(-1)^{\oplus k}\;\xrightarrow{\ \alpha\ }\;\mathcal O^{\oplus(2k+N)}\;\xrightarrow{\ \beta\ }\;\mathcal O(1)^{\oplus k}\;\longrightarrow\;0 ,
$$

with $\alpha$ linear in the twistor coordinate and $\beta$ linear in it as well. The composite $\beta\alpha=0$ is exactly the pair of ADHM equations, and the $\mathrm{U}(k)$ quotient is the freedom in choosing the monad; the bundle $E=\ker\beta/\mathrm{im}\,\alpha$ is the physical object, and the instanton at a point of $\mathbb R^4$ is recovered by restricting $E$ to the corresponding twistor line. Thus the quotient of this article and the holomorphic bundle are two descriptions of the same self-dual connection.

Two features make the construction *native* to the framework's algebra. First, the fibre $\mathbb{CP}^1$ is the complex projectivisation of the quaternionic line, and the quaternionic line is precisely the defining module $S\cong\mathbb C^2$ of $\mathbb B\cong M_2(\mathbb C)$; the twistor fibration is therefore the projectivisation of the algebra's own module, not an auxiliary space. Second, the ADHM quotient is a **hyperkähler quotient**: the flat space of the data $B_1,B_2,I,J$ carries the three complex structures of the quaternions, the moment map is $(\mu_{\mathbb R},\mu_{\mathbb C})$, and the quotient by the level set at zero is again hyperkähler. Hyperkähler geometry is the differential geometry of the quaternionic structure, and the algebra's three imaginary units are the three complex structures. The moduli space of instantons is therefore a hyperkähler manifold whose complex structures are the algebra's, which is the deepest sense in which the ADHM construction is the framework's own. The construction and the correspondence are standard; the algebra's role is that its module and its imaginary units are the objects being projectivised and varied.

## The Euclidean Route: An External Construction

The programme is P. Woit, "Euclidean Twistor Unification" (arXiv:2104.05099). It is recorded here as an external construction, in the manner of *An External Construction of Space*: nothing in it is derived by the framework, and nothing in the framework is evidence for it.

**The choice of case.** The Euclidean case is taken as fundamental. The reason given is the state space: a Euclidean quantum field theory determines its Hilbert space only after an imaginary time direction is chosen, which is the direction used for the Osterwalder–Schrader reflection. If the Euclidean case is the physics, that direction is a degree of freedom of the theory and not a calculational choice.

**The two factors, made local differently.** On $\mathbb{R}^4$ the rotation group is $\mathrm{Spin}(4)=\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$. The programme fixing conditions them into two different things:

- the $\mathrm{SU}(2)_R$ connection is the **chiral spin connection**, with the vierbein as a $\mathbb{R}^4$-valued one-form, and Einstein's equations are written on that pair;
- the $\mathrm{SU}(2)_L$ connection is the **weak interaction**;
- the field that picks the imaginary time direction is the imaginary-time component of the canonical $\mathbb{R}^4$-valued one-form $\theta$ — that is, one of the four components of the vierbein — and it is identified with the **Higgs**.

**Why twistor space is needed, in the source's own account.** The step above does not work as it stands, and the source says why. There are two problems. First, the electroweak group has an extra $\mathrm{U}(1)$, not just $\mathrm{SU}(2)_L$. Second, and worse, "as a 1-form, the Higgs field transforms non-trivially under both $\mathrm{SU}(2)_L$ and $\mathrm{SU}(2)_R$, but we want it to be invariant under $\mathrm{SU}(2)_R$". A component of $\theta$ cannot be a Higgs doublet while $\mathrm{SU}(2)_R$ is a local symmetry, because it is charged under $\mathrm{SU}(2)_R$ by construction.

The resolution is to lift to projective twistor space, where the two problems solve each other. A point of $\mathbb{PT}$ is a complex line $l\in\mathbb{C}^4$ together with the complex structure it defines; the unit vectors in $l$ give a $\mathrm{U}(1)$ bundle over $\mathbb{PT}$, which is the missing abelian factor; and tangent vectors to $S^4$ lifted to $\mathbb{PT}$ lie in $\mathrm{Hom}_{\mathbb{C}}(l,S_L)$, on which only that $\mathrm{U}(1)$ and $\mathrm{SU}(2)_L$ act. A lifted imaginary-time vector therefore transforms as a Higgs doublet and is $\mathrm{SU}(2)_R$-invariant, which is exactly what a component of $\theta$ could not be.

**The unbroken group is again a stabiliser.** The source's account of the electroweak breaking is this: "the Higgs picks out a specific $\mathrm{U}(1)$ subgroup of the $\mathrm{U}(2)$ group, the subgroup that leaves the field vector invariant", and the connection theory of that $\mathrm{U}(1)$ is electromagnetism. So both steps of the programme are the same move. The complex structure is a chosen object, and $\mathrm{U}(2)$ is its stabiliser in $\mathrm{SO}(4)$; the imaginary-time vector is a chosen object, and the electromagnetic $\mathrm{U}(1)$ is its stabiliser in that $\mathrm{U}(2)$. Two nested choices of a direction, each leaving a group behind. The corpus makes the first choice once and globally by the coordinate $Q_t=i q'_t$ and never makes the second, which is why the corpus has a $\mathrm{U}(2)$ and no electromagnetism.

This is the division the corpus declines to make. The corpus writes the same two factors, with the diagonal as the symmetry group and the axial combination as a chirality rotation; the programme writes the same two factors with each one local, one of them as gravity.

**Projective twistor space, and the internal groups.** Four-dimensional Euclidean space compactifies to $S^4=\mathbb{HP}^1$, and projective twistor space fibres over it,

$$
S^2=\mathbb{CP}^1\;\hookrightarrow\;\mathbb{PT}=\mathbb{CP}^3\;\longrightarrow\;S^4=\mathbb{HP}^1 ,
$$

with fibre the space of complex structures at the point — which is the sphere of the preceding section. A point of $\mathbb{PT}$ is a complex line $l\subset\mathbb{C}^4$, and because

$$
\mathbb{PT}=\frac{\mathrm{SU}(4)}{\mathrm{U}(1)\times\mathrm{SU}(3)} ,
$$

each point carries those two internal groups. The $\mathrm{SU}(3)$ acts on the quotient $l^\perp$ and is the strong group; the $\mathrm{U}(1)$ is the one the resolution above has just used. Because the fibre is the sphere of complex structures, the sphere of the preceding section is the internal space of the lift, and the point of $\mathbb{PT}$ is exactly a choice of $J$.

**The generation.** One generation of fermions is the space of linear maps

$$
\mathrm{Hom}\bigl(l\oplus l^\perp,\ S_R\oplus S_L\bigr)
=\bigl(l\oplus l^\perp\bigr)^{*}\otimes\bigl(S_L\oplus S_R\bigr) ,
$$

with $S_L=\mathbb{C}^2_0$ a doublet of $\mathrm{SU}(2)_L$ of weight $0$, and $S_R=\mathbb{C}_{-1}\oplus\mathbb{C}_{+1}$ the two singlets of $\mathrm{SU}(2)_L$ carrying the internal $\mathrm{U}(1)$ weights shown. The point of the construction is that no large group is used: there is no $\mathrm{SU}(5)$, no $\mathrm{SO}(10)$, and no separate weak factors; the internal groups are read off the geometry of a point of $\mathbb{PT}$.

**What the programme does not do, in its own words.** No full theory on $\mathbb{PT}$ is constructed. The dynamics are the Standard Model's own: the source writes that the fields "can be given exactly the dynamics of the Standard Model, using the usual Yang–Mills action and the standard Higgs field kinetic term and potential", so the Higgs potential is taken over, not derived. The origin of the **number** of generations is not addressed — the source says "it is unclear what the origin of generations might be", the construction gives one, and the three of the world are unexplained. The candidate extension that might supply them, a theory on $S^7$, is offered as speculation. And the state space construction, through cohomology on the upper half of $\mathbb{PT}$, is stated as a direction rather than a result.

**The hypercharge, and the arrangement the corpus already uses.** The corpus's scalar sector has written down the same electroweak assignment: *Custodial Symmetry and the Rho Parameter* records that "the left action is the full $\mathrm{SU}(2)_L$ and the right action is an $\mathrm{SU}(2)_R$ whose $T_3^R$ is the hypercharge". That is the programme's $\mathrm{U}(1)\subset\mathrm{SU}(2)_R$, named there in the corpus's own terms. What differs is what fixes it. The corpus's $T_3^R$ is the same element everywhere; in the programme the $\mathrm{U}(1)$ is a function of the point of $\mathbb{PT}$, so that choosing the hypercharge direction, the complex structure and the imaginary time direction are one and the same choice. The corpus has the right arrangement with the choice already made and frozen; the programme makes the choice dynamical. That is the difference the translation has to handle.

## The Generation, Recomputed

The dimension count is the part of the programme that can be checked without its dynamics, and it is the sharpest evidence that the geometric reading is not empty.

The two factors have complex dimensions $4$ and $4$, so

$$
\dim_{\mathbb{C}}\Bigl[\bigl(l\oplus l^\perp\bigr)^{*}\otimes\bigl(S_L\oplus S_R\bigr)\Bigr]=4\times 4=16 ,
$$

which is the number of Weyl components of one Standard-Model generation with a right-handed neutrino: $2$ for the lepton doublet, $1$ for the charged singlet, $1$ for the sterile singlet, $6$ for the quark doublet, and $3+3$ for the two quark singlets, totalling $16$. The programme's expansion reproduces exactly this list, with the multiplets read off the tensor product.

The $\mathrm{U}(1)$ weights follow from the two line-bundle weights. With $\mathrm{U}(1)\subset\mathrm{S}(\mathrm{U}(1)\times\mathrm{U}(3))\subset\mathrm{U}(4)$ traceless, the weight on $l$ and the weight on $l^\perp$ are in the ratio $-3:1$; taking $l$ at weight $+1$ and $l^\perp$ at weight $-\tfrac13$, the six terms carry the weights below, and the electric charge follows from $Q=T_3+\tfrac12Y$ in the usual normalisation. The overall sign is a convention — the other choice gives every $Y$ below with the opposite sign — and it is fixed here by the lepton doublet, which carries $Y=-1$.

| term | multiplet | $Y$ | $Q$ | particle |
|---|---|---|---|---|
| $l^{*}\otimes S_L$ | $\mathbb{C}^2$ | $-1$ | $0,-1$ | $(\xi_{\mathrm{neu},e},e)_L$ |
| $l^{*}\otimes\mathbb{C}_{-1}$ | $\mathbb{C}$ | $-2$ | $-1$ | $e_R$ |
| $l^{*}\otimes\mathbb{C}_{+1}$ | $\mathbb{C}$ | $0$ | $0$ | $\xi_{\mathrm{neu},R}$ |
| $(l^\perp)^{*}\otimes S_L$ | $\mathbb{C}^3\otimes\mathbb{C}^2$ | $\tfrac13$ | $\tfrac23,-\tfrac13$ | $(u,d)_L$ |
| $(l^\perp)^{*}\otimes\mathbb{C}_{-1}$ | $\mathbb{C}^3$ | $-\tfrac23$ | $-\tfrac13$ | $d_R$ |
| $(l^\perp)^{*}\otimes\mathbb{C}_{+1}$ | $\mathbb{C}^3$ | $\tfrac43$ | $\tfrac23$ | $u_R$ |

Recomputed: the six dimensions sum to $16$, and the eight charges above are exactly the eight of one generation. One discrepancy in the source is worth recording rather than passing over. The source prints the two triplet singlets with the weights $\tfrac23$ and $-\tfrac43$; they are the negatives of the pair that follows from its own lepton weights, since with the lepton doublet fixed at $Y=-1$ and the traceless condition fixing the ratio, the singlets must be $\tfrac43$ and $-\tfrac23$. The two printed values are consistent with each other and with nothing else on the line, so a sign has slipped between them and the leptons. With the sign fixed once, at the leptons, $Q=T_3+\tfrac12Y$ gives $u_R$ at $\tfrac23$ and $d_R$ at $-\tfrac13$. The content is unaffected — the two are the two members of one $S_R$ doublet either way — and the correction is recorded because the corpus's rule is to show the arithmetic, not to reproduce it.

Two limits belong beside the table. The construction gives **one** generation and has no mechanism for three: the count is a dimension of a tensor product, and no integer in the geometry selects $3$. And it gives no mass and no mixing angle, because the masses come from Yukawa couplings, which the construction does not contain. What it does give is the **pattern** — that the fermions of one generation are the linear maps between two bundles at a point — and the pattern is exact.

## What Moved, and From Where

| passage | source article | why it moved |
| --- | --- | --- |
| the monad and the Penrose–Ward correspondence | *The ADHM Construction and Biquaternion Instanton Data* | written on $\mathbb{CP}^3$, not on $\mathbb{B}$ |
| the Euclidean unification, in outline | *The SO(4) Route to the Euclidean Frame* | its arena is projective twistor space |
| the generation recomputed | *The SO(4) Route to the Euclidean Frame* | a check of that arena's construction |

**Nothing in the moved passages was edited except the headings**, which are now sections of this article. **The source articles keep their own results**: the ADHM equations, the moduli-space dimension and the BPST datum in the one; the real group, the sphere of complex structures and the translation table in the other.

## Summary

**The corpus now states its twistor material in one section and nowhere else.** What is collected here is geometry on a complex projective three-space: the monad whose cohomology is the instanton bundle, the lift that makes the two $\mathrm{SU}(2)$ factors local without an extra $\mathrm{U}(1)$, and the sixteen-component generation that the lift produces.

**The framework's relation to all of it is unchanged and is negative.** The algebra hosts the quaternionic line whose projectivisation is the fibre, and hosts $\mathrm{sym}^{4}S$, the carrier of the Weyl spinor; **it does not generate the bundle, the deformation, or the generation count.** The moved passages are recorded, checked where they can be checked, and adopted nowhere.

## Three Passages Removed from the Corpus

**Three paragraphs of the physics corpus were built on the contrast between the algebra and the arena, and they are kept here rather than lost.** The first is a realization of the conformal group on a new module; the second is a motivation for complexification drawn from the arena; the third is a comparison of two roles for the same generating object. **Each is reproduced as it stood, with its source named.**

### The Conformal Group on the New Module

*From Conformal Group in Biquaternionic Form.*

**Twistors.** A third realization uses the same vector space as the algebra but a different structure. The double cover $SU(2,2)$ of the conformal group acts linearly on twistor space $T=S\oplus\bar{S}\cong\mathbb{C}^4$. As complex vector spaces, $T$ and $\mathbb{B}$ are both $\mathbb{C}^4$; but the form that $SU(2,2)$ preserves is a **Hermitian** form of inertia $(2,2)$, whereas the biquaternion norm $\langle\cdot\rangle_{\natural}$ is a complex **symmetric bilinear** form. The spaces agree; the forms do not. This is the precise sense in which the conformal group, when it acts on the same four-dimensional vector space, enters as the **$*$-unitary** group of a form and not as the group of norm-one elements — a different kind of group from the one the framework uses. The companion article on twistors develops this in full, with the incidence relation and the Klein correspondence; the point here is only that the twistor realization does not place the conformal group inside $\mathbb{B}$, it places it on $\mathbb{B}$ read as a new module with a new form.

### Complexification as the Arena

*From Why Complexify Spacetime.*

**Twistor theory.** Penrose's twistor theory is built on complexified Minkowski space. Twistors are elements of $\mathbb{C}^4$, and Minkowski space is a real slice. The complex structure is not an add-on; it is the fundamental arena. Twistor theory has produced deep results — the nonlinear graviton construction, the Penrose transform, the twistor-string correspondence — even though it has not replaced standard physics. If twistor theory complexifies spinor space, and the $i r'_t$ convention complexifies time, it is natural to ask whether the two complexifications are related. This article explores whether they are: both could be projections of a single complexified spacetime.

### The Shared Generating Object

*From The Differentiable Field: One Primary Equation and the Linear Sector.*

**The same twistor.** The general solution of the primary equation is generated, on the programme's account, by an arbitrary function of three components of a twistor, with the coordinate resolved from the incidence relation. *Twistor Theory and Biquaternions* writes that relation for a different purpose, the representation of massless fields. The object is shared; only its role differs.

## Further Reading

- P. Woit, "Euclidean Twistor Unification", arXiv:2104.05099 [hep-th] (2021), the source of the Euclidean route above.
- M. F. Atiyah, N. J. Hitchin and I. M. Singer, "Self-duality in four-dimensional Riemannian geometry", *Proceedings of the Royal Society A* **362** (1978) 425–461, for the self-dual connection and the moduli-space dimension.
- R. S. Ward, "On self-dual gauge fields," *Physics Letters A* **61** (1977) 81–82, for the correspondence between self-dual connections and holomorphic bundles.
- L. A. Alexeyeva, "Differential algebra of biquaternions. 4. Twistors and twistor fields", *Mathematical Journal* **13** (2013), arXiv:1406.5347 [math-ph], for the vector-coefficient biwave system, its four families of unit-norm solutions and their generating potentials.
- V. V. Kassandrov, "The Algebrodynamics: Primordial Light, Particles-Caustics and the Flow of Time", *Hypercomplex Numbers in Geometry and Physics* **1** (2004) 84, arXiv:hep-th/0312278, for the congruence field of the shear-free complex null congruence.
- R. Penrose and W. Rindler, *Spinors and Space-Time*, Vol. 2 (Cambridge, 1986), for the conformal compactification of Minkowski space and its relation to null geometry.
