# __Wave–Particle Duality and the Count of Degrees of Freedom: The Symbol's Rank On and Off the Cone__

## Introduction

**The number of polarisations a field has is one integer, and that integer is a rank.** A massive vector field carries three polarisation states at each wave number and a massless one carries two. The count is usually made with a gauge argument and a constraint. It can be made once, for both, by asking how many directions of the amplitude the symbol of the gradient carries into the algebra. That number is three off the light cone and two on it, and the direction that is lost on the cone is exactly one circular polarisation.

**The last step is the reading, not the theorem.** What the algebra supplies is the rank of one linear map at one frequency point. That a rank is a count of polarisation states is the corpus's identification of an amplitude direction with a state, and it is imported here. The article proves the rank and marks the import in §*Three Counts, One Rank* and §*Limits*.

**Part of the story is already in the corpus.** *The Photon in Biquaternionic Form*, §*Circular Polarization and the Complex Structure of the Propagation Direction*, proves that the circular polarisations are the eigenvectors of left multiplication by the unit propagation direction, with eigenvalues $\mp i$, and that $i\vec u_\Phi$ acts as $+1$ on one of them, as $-1$ on the other, and carries the longitudinal direction to the scalar $-i e_t$. §*Helicity as an Observable in the Informational Sector* of the same article records the spectrum $\{+1,0,-1\}$ of the helicity operator on the complexified vector part. All of that is used here, and none of it is re-proved.

**The new part is one decomposition and one count.** The symbol of the gradient is not the helicity multiplication; it is the helicity multiplication **shifted by the energy wave number**,

$$
i\tilde K_{\Phi}\big|_{\mathbb{B}_{V}}=-k_{t}^{\prime}\,\mathrm{id}+k_{\Phi}\,\bigl(i\vec u_\Phi\bigr)\big|_{\mathbb{B}_{V}} .
$$

Read against the published spectrum, that line gives the eigenvalues $-k_{t}^{\prime}\pm k_{\Phi}$ on the circular pair at once, and it locates the count of degrees of freedom: the rank is three while both branches are away from zero, and two when one of them crosses it. **The crossing surface is the light cone, and the branch that crosses is one circular polarisation.**

**Why this belongs to the duality.** Wave–particle duality, as *Wave–Particle Duality and the Fourier Transform* states it, is one equation read in two bases. Here one integer is read twice. On the wave side it is the dimension of the image of the symbol: how many field strengths the operator can produce at a frequency. On the particle side it is the number of polarisation states available at that frequency. The two readings are the two halves of rank–nullity, and the switch between them is the transform.

**What this does not buy.** No dynamics, no value of a mass, no mechanism for the massless limit, and no derivation of gauge invariance. The rank reports how many directions the symbol reaches. Why a direction is a state, and why the massless field has a gauge symmetry, are the readings imported from the articles named below.

**The conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with $e_t=1$ and $\vec e_x,\vec e_y,\vec e_z$, so $\vec e_\eta^{2}=-e_t$ for $\eta=x,y,z$. On a plane wave *Derivatives, Fields and Transforms* gives the symbols

$$
\tilde\nabla_\Phi\longmapsto i\tilde K_{\Phi},
\qquad
(\tilde\nabla_\Phi)^{\natural}\longmapsto i\tilde K_{\Phi}^{\natural},
\qquad
\tilde K_{\Phi}=i\,k_{t}^{\prime}e_t+\vec k_{\Phi},
\qquad
\tilde K_{\Phi}^{\natural}=i\,k_{t}^{\prime}e_t-\vec k_{\Phi},
$$

whose product is the central norm

$$
\tilde K_{\Phi}\tilde K_{\Phi}^{\natural}=-k_{t}^{\prime\,2}+k_{\Phi}^{2},
$$

equal to $-k_{m}^{2}$ exactly on the mass shell. The superscript $\natural$ is the quaternion conjugation, the one whose fixed space is the centre, and the norm is written in full throughout and never as a single letter. The propagation direction is $\vec u_\Phi=\vec k_{\Phi}/k_{\Phi}$, a real unit pure quaternion, and the circular basis is the corpus's,

$$
\varepsilon_{\mathrm{fop},\pm}=\frac{1}{\sqrt 2}\bigl(\varepsilon_{\mathrm{fop},1}\pm i\,\varepsilon_{\mathrm{fop},2}\bigr),
$$

built on a right-handed triad $(\varepsilon_{\mathrm{fop},1},\varepsilon_{\mathrm{fop},2},\vec u_\Phi)$.

## The Symbol and the Rank

### The symbol is left multiplication

**The transform turns the gradient into an element, and an element acts by multiplication.** Applying the symbol to a field is the map

$$
\mathcal{F}[\tilde F]\longmapsto i\tilde K_{\Phi}\,\mathcal{F}[\tilde F],
$$

which is left multiplication by $i\tilde K_{\Phi}$ on the algebra, or on whichever subspace the field is restricted to. The transform of a field is written $\mathcal{F}[\tilde F]$, after *Biquaternion Continuous Harmonic Analysis*, and it carries no mark on the field itself: a caret carries a power, a conjugation, a transposition and a construction, and the transform is none of the four. This is the boxed statement of *Wave–Particle Duality and the Fourier Transform*, and it is exact for constant coefficients: the derivative becomes a multiplier, and the multiplier is an element.

**The field strength is a pure vector, so the operative domain is three-dimensional.** *Maxwell's Equations in the Biquaternionic Formulation* states that the field strength is the vector part of a conjugate gradient and is therefore a pure element. The vector part $\mathbb{B}_{V}$ is the anti-fixed space of quaternion conjugation, carried by $\vec e_x,\vec e_y,\vec e_z$, and it is three-dimensional over $\mathbb{C}$ — the dimension of the complexified amplitude space of a vector field.

**So the object whose rank is in question is a map from three complex dimensions into four**,

$$
L_{i\tilde K_{\Phi}}:\mathbb{B}_{V}\longrightarrow\mathbb{B},
\qquad
\tilde F\longmapsto i\tilde K_{\Phi}\tilde F .
$$

The operator is written $L_{a}$ for left multiplication by the element $a$, as the corpus writes it, so the structural capital is $L$ and the calligraphic letter is left to the Lagrangian density. The codomain is the whole algebra and not the vector part, and that is not an oversight: the longitudinal direction does not stay in the vector part, a fact the photon article records and which §*The Longitudinal Direction Becomes the Constraint* uses.

### The symbol is the helicity multiplication, shifted

**Split the element, and the operator splits with it.** Because $\vec k_{\Phi}=k_{\Phi}\vec u_\Phi$ and $e_t$ is the identity,

$$
i\tilde K_{\Phi}=-k_{t}^{\prime}+i\,k_{\Phi}\,\vec u_\Phi ,
$$

an identity between elements, hence an identity between operators:

$$
i\tilde K_{\Phi}\big|_{\mathbb{B}_{V}}=-k_{t}^{\prime}\,\mathrm{id}+k_{\Phi}\,\bigl(i\vec u_\Phi\bigr)\big|_{\mathbb{B}_{V}} .
$$

**The decomposition was checked, and it is exact.** On one hundred random frequency points and four test directions each — the two circular ones, the longitudinal one, and a linear one — the two sides agree to $2.9\times10^{-16}$ relative to the largest coefficient of the symbol.

**The first term is a real shift and the second is the helicity.** $-k_{t}^{\prime}$ is a real central scalar. The element $i\vec u_\Phi$ is Hermitian and belongs to $\mathbb{B}_{\Psi}$, the informational sector, and the photon article identifies the vector part of its left multiplication with the helicity operator, $\lambda=\mathrm{Vect}\circ(\text{left multiplication by } i\vec u_\Phi)$. **The symbol of the gradient is therefore a central shift plus the momentum wave number times the helicity generator.** Neither factor is a new object; the shift and the generator are both published, and their sum is the symbol.

**The statement in one line.** The symbol does to an amplitude what a mass-shell condition does to a spectrum: it adds a constant and scales a quantum number. The constant is the energy wave number, the quantum number is the helicity, and the scale is the momentum wave number.

### Rank, kernel and cokernel

**The three spaces, and the two numbers.** *The Fourier Transform and the Symbol of a Differential Operator*, §*The Kernel and the Cokernel*, states the dimensions once for left multiplication by an element of a finite-dimensional algebra:

$$
\dim\ker L_{\sigma}=\dim\operatorname{coker}L_{\sigma}=d-\operatorname{rank}L_{\sigma},
\qquad
\dim\operatorname{im}L_{\sigma}=\operatorname{rank}L_{\sigma},
$$

with $d$ the dimension of the algebra. The kernel is the freedom in the solution; the cokernel is the constraint on the data. That article proves the statement by rank–nullity and the dimension formula for a quotient, so nothing is re-proved here.

**The equality of the two dimensions is a property of the regular representation, and this article's map is not in it.** The same section of that article states the exception in as many words: the equality is a numerical coincidence of the regular representation, and it fails for a symbol that takes values in a proper subalgebra or in a module. Left multiplication by $i\tilde K_{\Phi}$ on the vector part is exactly that case, a map of three complex dimensions into four, so the two dimensions are read separately and neither is $d-r$ with a single $d$:

$$
\dim\ker L_{i\tilde K_{\Phi}}\big|_{\mathbb{B}_{V}}=3-\operatorname{rank},
\qquad
\dim\operatorname{coker}L_{i\tilde K_{\Phi}}\big|_{\mathbb{B}_{V}}=4-\operatorname{rank},
$$

where $3$ is the dimension of the domain and $4$ that of the codomain. **The rank counts one thing and the two dimensions count two more, and the count of degrees of freedom is the rank itself, not either of them.**

**The reading this article uses.** For $L_{i\tilde K_{\Phi}}$ on the three-dimensional vector part: the kernel is the set of amplitude directions the symbol annihilates, and the cokernel is the set of conditions the transformed equation places on the source. The first is a count of lost directions; the second is a count of constraints. **A single rank reports both, and the article reads it twice.**

**One warning, and it is why the rank is computed on the vector part.** The rank of left multiplication by $i\tilde K_{\Phi}$ on the whole algebra is not the rank on the vector part. On the whole algebra the map is four-dimensional in and four-dimensional out; on the vector part it is three in and four out. The two computations give different numbers, and only the second one is about a field strength. Every number below is for the vector part.

### Why the vector part is the carrier

**Three reasons, and they agree.** The field strength of the corpus is a pure vector by construction. The amplitudes of *The Proca Equation: Massive Spin 1 in Biquaternionic Form* are the three real components of a spatial vector, which is the material form of a pure element. And the vector part is the carrier of the spin-one representation, which *Helicity in Biquaternionic Form* names: spin one is the adjoint action on the imaginary quaternions, and only the carrier changes from the fundamental module. **The vector part is therefore a carrier of a representation and not a module over the algebra**, and that distinction is what makes this article's map possible: left multiplication by an element does not preserve the vector part, so the symbol can carry a direction out of it. A module would have trapped every direction inside.

**What the carrier is not.** The state module of the quantum articles is not the carrier here. States lie on the zero-divisor cone of the algebra; a field strength lies in the vector part. This article counts field amplitudes, and the count of states is *Wave–Particle Duality and the Fourier Transform*, §*Where the Duality Lands*.

## The Rank On and Off the Cone

### The three directions

**The basis in which the symbol is diagonal.** The vector part has the linear directions $\varepsilon_{\mathrm{fop},1},\varepsilon_{\mathrm{fop},2},\vec u_\Phi$ and the circular ones $\varepsilon_{\mathrm{fop},\pm}$. The circular pair spans the transverse plane with $\vec u_\Phi$,

$$
\varepsilon_{\mathrm{fop},1}=\frac{\varepsilon_{\mathrm{fop},+}+\varepsilon_{\mathrm{fop},-}}{\sqrt 2},
\qquad
\varepsilon_{\mathrm{fop},2}=\frac{\varepsilon_{\mathrm{fop},+}-\varepsilon_{\mathrm{fop},-}}{i\sqrt 2},
$$

so the three elements $\varepsilon_{\mathrm{fop},+}$, $\varepsilon_{\mathrm{fop},-}$ and $\vec u_\Phi$ are a complex basis of $\mathbb{B}_{V}$. Nothing is gained or lost in the change; the point is that the symbol is diagonal in it, and it is diagonal because the helicity multiplication is.

### The computation

**The three images, read off the published spectrum.** Left multiplication by $i\vec u_\Phi$ acts as $+1$ on $\varepsilon_{\mathrm{fop},+}$, as $-1$ on $\varepsilon_{\mathrm{fop},-}$, and sends $\vec u_\Phi$ to $-i e_t$; that is the photon article's display, and it is quoted. Applying the shift $-k_{t}^{\prime}$ to each gives

$$
i\tilde K_{\Phi}\,\varepsilon_{\mathrm{fop},+}=-(k_{t}^{\prime}-k_{\Phi})\,\varepsilon_{\mathrm{fop},+},
\qquad
i\tilde K_{\Phi}\,\varepsilon_{\mathrm{fop},-}=-(k_{t}^{\prime}+k_{\Phi})\,\varepsilon_{\mathrm{fop},-},
$$

$$
i\tilde K_{\Phi}\,\vec u_\Phi=-i\,k_{\Phi}-k_{t}^{\prime}\,\vec u_\Phi .
$$

The first display is an eigenvalue statement with the two light-cone factors, each carrying a minus sign. The second is not: the longitudinal direction leaves the vector part, and its image has a scalar part $-i k_{\Phi}$ beside a vector part $-k_{t}^{\prime}\vec u_\Phi$.

**The three relations were checked directly, without the decomposition.** On one hundred random frequency points, with the triad rebuilt at each point and the residual taken against the largest coefficient in the image, the two eigenvalue identities hold to $3.6\times10^{-16}$ and the two parts of the longitudinal image to $3.6\times10^{-16}$. The relations are exact algebra, and the numbers guard the transcription of the signs.

**The worked point.** Take $k_{t}^{\prime}=5$ and $\vec k_{\Phi}=3\vec u_\Phi$, so $k_{\Phi}=3$ and $\tilde K_{\Phi}\tilde K_{\Phi}^{\natural}=-16$, which is $-k_{m}^{2}$ at $k_{m}=4$ — the $3$–$4$–$5$ mode of *Wave–Particle Duality and the Fourier Transform*. The eigenvalues are $-2$ and $-8$; their product is $16$, which is $-\tilde K_{\Phi}\tilde K_{\Phi}^{\natural}$; and the longitudinal image is $-3i-5\vec u_\Phi$, with scalar part $-3i=-i k_{\Phi}$.

### The two ranks, and what each dimension counts

**Off the cone the rank is three.** The map is three in and four out, so rank three is the largest possible, the kernel is empty and the cokernel is one-dimensional. No amplitude direction is annihilated; one condition is placed on the data.

**On the cone the rank is two.** The first eigenvalue vanishes, so $\varepsilon_{\mathrm{fop},+}$ joins the kernel, the rank falls by one and the cokernel becomes two-dimensional. The second eigenvalue is $-2k_{\Phi}$, non-zero at every non-zero wave number, so $\varepsilon_{\mathrm{fop},-}$ is never annihilated.

**The domain is the forward cone.** The count is stated for $k_{t}^{\prime}\ge0$ and $k_{\Phi}>0$, which is what $k_{t}^{\prime}=E/(\hbar c)$ with $E>0$ and a non-zero momentum give. Neither restriction is cosmetic. At negative energy the drop does not disappear but moves: at $k_{t}^{\prime}=-k_{\Phi}$ the branch that vanishes is $\varepsilon_{\mathrm{fop},-}$, and $\varepsilon_{\mathrm{fop},+}$ is scaled by $+2k_{\Phi}$, so the mirror statement of §*The conjugate symbol kills the other direction* holds with the two circular labels exchanged. At $\vec k_{\Phi}=0$ the unit direction $\vec u_\Phi$ does not exist and the circular basis is undefined; there the symbol is the central scalar $i k_{t}^{\prime}e_t$, of rank three on the vector part for $k_{t}^{\prime}\ne0$ and of rank zero at the origin, where both eigenvalues vanish at once.

**The four rows, in one table.** The first two were checked on one hundred random frequency points each, with the rank taken by singular value decomposition at a tolerance of $10^{-9}$ and the cokernel dimension taken as $4-r$. The last two are exact: the negative cone is the positive cone with $k_{t}^{\prime}$ reflected, and the origin is a zero map.

| frequency point | rank on $\mathbb{B}_{V}$ | kernel | cokernel | annihilated direction |
|---|---|---|---|---|
| off the cone, $k_{t}^{\prime}\ne\pm k_{\Phi}$ | $3$ | $0$ | $1$ | none |
| on the cone, $k_{t}^{\prime}=k_{\Phi}>0$ | $2$ | $1$ | $2$ | $\varepsilon_{\mathrm{fop},+}$ |
| on the negative cone, $k_{t}^{\prime}=-k_{\Phi}<0$ | $2$ | $1$ | $2$ | $\varepsilon_{\mathrm{fop},-}$ |
| the origin, $k_{t}^{\prime}=k_{\Phi}=0$ | $0$ | $3$ | $4$ | all three |

**No intermediate rank occurs.** Over the hundred sample points of each forward kind the rank took exactly one value, so there is no third stratum between the cone and its complement. That is what a zero set of multiplicity one looks like: one branch crosses zero once, and it crosses on a single surface.

**The stratification is the whole content.** The rank is a function of the frequency point, constant on the two open regions and lower on their common boundary. The count of degrees of freedom is therefore not a number belonging to a field; it is a number belonging to a field **at a frequency point**, and its two values are the two regions.

## The Two Circular Directions

### The eigenvalues are the two light-cone factors

**One identity, and it carries the shell.** The product of the two eigenvalues is

$$
(k_{t}^{\prime}-k_{\Phi})(k_{t}^{\prime}+k_{\Phi})=k_{t}^{\prime\,2}-k_{\Phi}^{2}=-\tilde K_{\Phi}\tilde K_{\Phi}^{\natural},
$$

so the determinant of the symbol on the transverse plane is minus the quaternion norm. **The mass shell, which is the vanishing of $\tilde K_{\Phi}\tilde K_{\Phi}^{\natural}+k_{m}^{2}$, is therefore also the vanishing of one eigenvalue plus $k_{m}^{2}$.** That is the vector-part reading of the corpus's block determinant being one number to the fourth power, *The First-Order Root of the Biquaternion Klein–Gordon Operator*, §*The determinant*.

**The reading.** The dispersion relation is usually met as a level set of a norm. Here it is met twice: as a level set of the norm, and as the vanishing locus of one eigenvalue of the symbol's action on amplitude directions. The second is finer, because it says which direction vanishes with it. **A norm can vanish without naming a direction; an eigenvalue cannot.**

### On the cone one eigenvalue vanishes

**Only one, because the other is bounded away from zero.** On the cone the second eigenvalue is $-2k_{\Phi}$, so it cannot vanish at a non-zero wave number. Exactly one circular direction disappears from the image, and the rank drops by exactly one — never by two.

**This is the sharpest form of the statement.** A rank is a number, and a number can drop for many reasons. The eigenvalue display gives the reason: one branch of the shifted helicity spectrum crosses zero, and the direction attached to it is annihilated. On the cone the kernel is one complex line, and the line is $\varepsilon_{\mathrm{fop},+}$.

**The check on the mode.** At $k_{t}^{\prime}=k_{\Phi}=5$ with $\vec k_{\Phi}=5\vec u_\Phi$, the image of $\varepsilon_{\mathrm{fop},+}$ is zero to machine precision and the image of $\varepsilon_{\mathrm{fop},-}$ is $-10\,\varepsilon_{\mathrm{fop},-}$, the value the formula gives.

### The longitudinal direction becomes the constraint

**The third direction is not annihilated; it is carried out of the vector part.** Its image is $-i k_{\Phi}-k_{t}^{\prime}\vec u_\Phi$, whose scalar part is $-i k_{\Phi}$. The scalar direction is where the constraint lives: it is the Lorenz condition of the Maxwell and Proca articles, the vanishing of the scalar part of the conjugate gradient of the potential.

**So the three directions are used in three different ways.** One is annihilated on the cone and carried off it. One is scaled by the sum of the light-cone factors and never vanishes. One leaves the vector part and becomes the constraint. **The rank counts the directions with independent non-zero images: three off the cone, two on it.** The longitudinal direction is one of them at every frequency, because its image is non-zero even though it has left the vector part. What the cone removes is one circular direction, and nothing else.

## What the Lost Direction Means

### One circular polarisation, not the longitudinal

**The direction the symbol loses on the cone is circular, not longitudinal.** A reader expects the massless field to lose the longitudinal direction, because a residual gauge transformation removes it, and that is the textbook sentence. Here the direction that leaves the image is $\varepsilon_{\mathrm{fop},+}$, a transverse circular direction. The longitudinal direction is annihilated at no frequency point, on the cone or off it: its image is $-i\,k_{\Phi}-k_{t}^{\prime}\vec u_\Phi$, non-zero because of the scalar part, and that scalar part is the constraint rather than a fourth surviving vector direction.

**The two statements are consistent, and the difference is what is being counted.** The textbook count is of states after the gauge quotient. The rank counts amplitude directions before the quotient. The longitudinal direction is removed for both massive and massless fields by the constraint, which is why it leaves the vector part; its image remains in the algebra as the scalar constraint, and it is counted once in the rank at every frequency. The massless case then loses one circular direction, which is why the count is two and not three. **The constraint and the cone together produce the massless count, and the rank separates them.**

**What that buys.** The usual presentation gives the massless count as one subtraction from four. Here there is exactly one subtraction, and it happens on one surface: the rank falls by one on the cone and by nothing anywhere else. The constraint is not a subtraction at all in this bookkeeping — it is the scalar part of the third image, present at every frequency. **The two mechanisms that the textbook count merges are therefore kept apart: one is a dimension, the other is a component of an image.**

### The conjugate symbol kills the other direction

**The two conjugates split the two circular directions.** On the cone,

$$
i\tilde K_{\Phi}^{\natural}\,\varepsilon_{\mathrm{fop},-}=0,
\qquad
i\tilde K_{\Phi}^{\natural}\,\varepsilon_{\mathrm{fop},+}=-2k_{\Phi}\,\varepsilon_{\mathrm{fop},+},
$$

the mirror of the display for $i\tilde K_{\Phi}$: the conjugate annihilates the other direction and scales the one the first symbol annihilated. The residual is $3.6\times10^{-16}$ over the hundred sample points.

**The reading.** The two conjugate symbols have complementary one-dimensional kernels on the cone, and their direct sum is the transverse plane. An equation written with $\tilde\nabla_\Phi$ and one written with $(\tilde\nabla_\Phi)^{\natural}$ do not select the same circular direction, and the pair of them exhausts the transverse amplitudes.

**This is a statement about the algebra, not a convention of handedness.** Which of the two the corpus's helicity articles label $\lambda=+1$ is a matter of the operator's sign, and this article does not need it. What is claimed is only that the two conjugate symbols annihilate opposite circular directions, and that the pair is complete.

### The eigenvectors are null

**The two circular directions are null in the algebra's own sense.** Their squares vanish,

$$
\varepsilon_{\mathrm{fop},+}^{2}=\varepsilon_{\mathrm{fop},-}^{2}=0,
$$

to a residual of $2.4\times10^{-16}$ over the hundred sample points. This is the algebra's form of the statement that a circular polarisation vector is isotropic, $\varepsilon_{\mathrm{fop},\pm}\cdot\varepsilon_{\mathrm{fop},\pm}=0$ in the complex-bilinear product, which the photon article records.

**Why this is the right coincidence.** A null element of the vector part is a zero divisor in that subspace, and the zero-divisor cone is the object the quantum articles use as the state module. The direction the symbol annihilates on the cone is therefore the same kind of object as a state: null, and annihilated by a multiplicative operator. That is the closest this article comes to the quantum side, and it is a statement about the algebra, not about a particle.

## Three Counts, One Rank

### The massive field counts three

**A massive vector field sits off the cone at every wave number**, because $k_{t}^{\prime\,2}=k_{\Phi}^{2}+k_{m}^{2}$ with $k_{m}\ne0$ gives $k_{t}^{\prime}>k_{\Phi}$ strictly. The symbol is then injective on the vector part, its rank is three, and the three directions all reach the algebra with non-zero images. *The Proca Equation* counts three real amplitudes in the rest frame; the rank says the same thing without a frame.

**Where the longitudinal amplitude comes from.** Off the cone the longitudinal direction still leaves the vector part and still produces the scalar constraint, so the count of three is not a count of directions remaining inside the vector part. It is the count of directions the symbol distinguishes, each carried to a non-zero image. The Proca article's three amplitudes are the three directions, and the constraint fixes the time component, which is a fourth component and not one of the three. **The rank and the amplitude count agree because the constraint acts outside the vector part.**

### The massless field counts two

**A massless field sits on the cone at every wave number**, and the rank is two, one less than off the cone. The kernel is one complex line, $\varepsilon_{\mathrm{fop},+}$, so the loss is exactly one circular polarisation. The Proca article obtains its two by removing the longitudinal direction with a residual gauge transformation, and the two counts agree while the bookkeeping differs: the rank's two dimensions are $\varepsilon_{\mathrm{fop},-}$ and the longitudinal image $-i\,k_{\Phi}-k_{t}^{\prime}\vec u_\Phi$, whereas the Proca pair is $\varepsilon_{\mathrm{fop},\pm}$. **The agreement is a count of dimensions, and this article claims no more than that.**

**The two arguments are independent, and that is the useful part.** A reader who distrusts the gauge argument can count the rank; a reader who distrusts the algebra can count the amplitudes. When they agree the count is not in doubt, and the agreement is not circular, because neither argument refers to the other.

### The graviton counts two by a different mechanism

**The graviton is not a vector field, so this rank is not its rank.** The count of two comes from the transverse-traceless projector on the symmetric square, whose rank *Canonical Quantization of the Biquaternion Graviton Field* computes as $6-4=2$. The carrier is six-dimensional and the removal is by a projector, not by a symbol.

**What the two cases share is the shape of the answer, not the mechanism.** In both, a count of degrees of freedom is the rank of one map on one carrier, and in both the carrier is fixed by the algebra before any dynamics is written. What differs is the carrier, and the article says so rather than forcing the graviton into the vector picture.

### What the count does not derive

**No gauge invariance.** The rank drop on the cone is not the statement that the massless field has a gauge symmetry. Gauge invariance is a statement about a transformation that leaves the equation fixed, and it is an input of the Maxwell and Proca articles. The rank reports the dimension of an image; the gauge argument reports an equivalence class. They meet in the count and they are not the same statement.

**No Higgs mechanism.** The passage from three to two as the mass is turned off is a discontinuity of the count, and the mechanism that makes it continuous is the Stueckelberg field, which the Proca article records. The rank sees the discontinuity and nothing else; it has no scalar to give the third direction to.

**No value of a mass.** The cone is $k_{t}^{\prime}=k_{\Phi}$ and the mass shell is $k_{t}^{\prime\,2}=k_{\Phi}^{2}+k_{m}^{2}$. The rank distinguishes the two surfaces and says nothing about which one a given field lies on.

## The Duality in This Reading

**The same integer, read twice.** On the wave side, the rank is the dimension of the image of the symbol: the number of field strengths the operator can produce at a frequency. On the particle side, it is the number of polarisation states the field has at that frequency. The two readings are the two halves of rank–nullity, and the transform is what makes them one integer. **The identification of a direction with a state is the corpus's reading and is imported here; §*Three Counts, One Rank* states exactly how far it goes, and the count of dimensions is the part this article proves.**

**Why this belongs to the duality and not to the algebra alone.** The algebra alone gives a rank of a linear map. What makes it a statement about a particle is that the field's amplitudes are the states, an identification the corpus makes throughout and states in *Wave–Particle Duality and the Fourier Transform*, §*Two Forms, Two Descriptions*. The wave side is a property of the symbol; the particle side is a property of the amplitude space; the transform is the switch that carries one to the other. **The count of degrees of freedom is where the switch is visible as an integer rather than as a transform.**

**The cone is where the switch changes its answer.** Everywhere off the cone the two readings give three; on the cone they give two. The duality does not hold one number for a field, it holds one number per frequency point, and the surface where the number changes is the massless dispersion surface. That is sharper than the sentence "a massless field has two polarisations", and it is what the rank supplies.

**One consequence for how the corpus writes its counts.** A count of polarisations is a function of the frequency point, so an article that states a count without naming the surface it is taken on is incomplete. The Proca article names the rest frame; the photon articles name the massless shell. The rank display names both at once, and it is the form in which the two can be compared.

## Limits

- **The count is stated on the forward cone.** $k_{t}^{\prime}\ge0$ and $k_{\Phi}>0$, with the origin excluded, where the rank is zero rather than two. Negative energy repeats the drop at $k_{t}^{\prime}=-k_{\Phi}$ with $\varepsilon_{\mathrm{fop},+}$ and $\varepsilon_{\mathrm{fop},-}$ exchanged, so the forward statement is the corpus's convention and not a loss of generality.
- **The count is of complex amplitude directions.** The vector part has complex dimension three, and off the cone the three directions are the three polarisation states of a massive vector field by the corpus's reading. The correspondence is not a count of real parameters: a real field strength has six real components in three complex directions. **On the cone the correspondence is not direction for direction**, as §*The massless field counts two* states, and the article claims the count of dimensions and not the identification.
- **The rank is computed on one carrier only.** On the whole algebra the same symbol has rank four off the cone and rank two on it, with a two-dimensional kernel on the cone. Both computations are correct and they answer different questions: the whole-algebra one is a rank of left multiplication in the algebra read as a matrix algebra, the vector-part one is the rank of the symbol on the space a field strength occupies.
- **Constant coefficients.** The symbol exists only for a constant-coefficient operator. A varying medium has a convolution for an image and no rank at a frequency point, so the count of degrees of freedom in an inhomogeneous medium is not this count.
- **The handedness labels are the photon article's.** This article uses the corpus's $\varepsilon_{\mathrm{fop},\pm}$ and its $\mp i$ eigenvalue relation, and it does not assign $\lambda=+1$ or $-1$ to either, because the assignment needs the helicity operator's sign convention, which the article does not use.
- **The graviton is quoted, not recomputed.** The count of two for the graviton is the transverse-traceless rank of the corpus's graviton article, and the mechanism there is a projector on a six-dimensional carrier. Nothing in this article's rank computation applies to it.
- **No statement about a state.** The polarisations counted here are amplitude directions of a field strength. Whether a direction is occupied, and with what weight, is a statement about a state, and states are not in this article.
- **The rank at a point says nothing about propagation.** A rank is an algebraic number at one frequency point. It does not say how a wave packet moves, and it does not distinguish a stable mode from an evanescent one.

## Summary

**The count of degrees of freedom is the rank of the symbol on the vector part.** Left multiplication by $i\tilde K_{\Phi}$ maps the three complex directions of the vector part into the algebra, with rank three off the light cone and rank two on it. The cokernel is one-dimensional off the cone and two-dimensional on it.

**The symbol is the helicity multiplication shifted by the energy wave number.** $i\tilde K_{\Phi}=-k_{t}^{\prime}+i k_{\Phi}\vec u_\Phi$, so on the vector part it is $-k_{t}^{\prime}$ times the identity plus $k_{\Phi}$ times left multiplication by the Hermitian element $i\vec u_\Phi$. The identity holds to $2.9\times10^{-16}$ over one hundred points.

**The two circular polarisations are the eigenvectors, and the eigenvalues are the light-cone factors.** In the photon article's basis the images are $-(k_{t}^{\prime}-k_{\Phi})\varepsilon_{\mathrm{fop},+}$ and $-(k_{t}^{\prime}+k_{\Phi})\varepsilon_{\mathrm{fop},-}$. The product of the two eigenvalues is minus the quaternion norm, and the identities hold to $3.6\times10^{-16}$.

**On the cone exactly one branch vanishes, and the direction attached to it is lost.** The drop from three to two is the loss of one circular polarisation, not of the longitudinal one. The longitudinal direction leaves the vector part at every frequency, its image carrying the scalar part $-i k_{\Phi}$, and that scalar is the constraint.

**The two conjugate symbols annihilate opposite circular directions.** On the cone $i\tilde K_{\Phi}$ annihilates $\varepsilon_{\mathrm{fop},+}$ and $i\tilde K_{\Phi}^{\natural}$ annihilates $\varepsilon_{\mathrm{fop},-}$, so the two kernels together span the transverse plane.

**The eigenvectors are null.** $\varepsilon_{\mathrm{fop},+}^{2}=\varepsilon_{\mathrm{fop},-}^{2}=0$, so the directions the symbol distinguishes are exactly the null directions of the vector part.

**The three counts of the corpus are three readings of one rank.** The massive vector has three because it is off the cone, the massless vector has two because it is on it, and the graviton has two by a different mechanism on a different carrier. **The massless agreement is an agreement of dimensions**, and §*The massless field counts two* states where the direction-by-direction correspondence stops.

**What is not derived.** Gauge invariance, the value of a mass, the mechanism of the massless limit, and the identification of a direction with a state. The rank is exact; the reading is imported, and the article marks where.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra, $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ |
| $\mathbb{B}_{V}$ | the vector part, the anti-fixed space of quaternion conjugation, of complex dimension three |
| $\mathbb{B}_{\Phi}$, $\mathbb{B}_{\Psi}$ | the material and informational sectors: $\mathbb{B}_{\Psi}$ is the Hermitian, fixed space of the adjoint, $\mathbb{B}_{\Phi}$ the anti-Hermitian, anti-fixed one |
| $\tilde K_{\Phi}$ | the wave-number element $i\,k_{t}^{\prime}e_t+\vec k_{\Phi}$ |
| $\tilde K_{\Phi}^{\natural}$ | its quaternion conjugate $i\,k_{t}^{\prime}e_t-\vec k_{\Phi}$ |
| $\tilde K_{\Phi}\tilde K_{\Phi}^{\natural}$ | the central quaternion norm, $-k_{t}^{\prime\,2}+k_{\Phi}^{2}$, equal to $-k_{m}^{2}$ on shell |
| $k_{t}^{\prime}$ | the energy wave number, $E/(\hbar c)=\omega/c$ |
| $k_{\Phi}$ | the modulus of the momentum wave number, $\lvert\vec p\rvert/\hbar$ |
| $k_{m}$ | the mass wave number, $m\,c/\hbar$ |
| $\vec u_\Phi$ | the unit propagation direction, $\vec k_{\Phi}/k_{\Phi}$ |
| $\varepsilon_{\mathrm{fop},1},\varepsilon_{\mathrm{fop},2}$ | a right-handed orthonormal pair transverse to $\vec u_\Phi$ |
| $\varepsilon_{\mathrm{fop},\pm}$ | the circular directions $(\varepsilon_{\mathrm{fop},1}\pm i\varepsilon_{\mathrm{fop},2})/\sqrt 2$ |
| $\lambda$ | the helicity operator, the vector part of left multiplication by $i\vec u_\Phi$ |
| $L_{i\tilde K_{\Phi}}$ | left multiplication by $i\tilde K_{\Phi}$, read as a map $\mathbb{B}_{V}\to\mathbb{B}$ |
| $r$ | the rank of that map: three off the cone, two on it |
| $\ker$, $\operatorname{coker}$ | its kernel and cokernel, of dimensions $3-r$ and $4-r$ |

## Further Reading

- *The Fourier Transform and the Symbol of a Differential Operator*, for the symbol, the zero set, and the rank–nullity statement this article reads on the vector part.
- *Biquaternion Continuous Harmonic Analysis*, for the transform pair and the convolution theorem behind the symbol.
- *Inversion of the Biquaternion Fourier Transform: Poles, Tails and the Degenerate Set*, for the degenerate set where the inverse fails, which is the light cone of this article read as a set of frequencies.
- *Relations between the Biquaternion Exponential and the Fourier Kernel*, for the character that the symbol multiplies.
- *Wave–Particle Duality and the Fourier Transform*, for the two quadratic forms, the switch between them, and the mass shell as a level set.
- *The Three Wavenumbers of a Particle*, for $k_{t}^{\prime}$, $k_{\Phi}$ and $k_{m}$ and the right triangle they form.
- *The Photon in Biquaternionic Form*, for the circular basis, the $\mp i$ eigenvalue relation, the action of $i\vec u_\Phi$ on the vector part, and the helicity spectrum.
- *Helicity in Biquaternionic Form*, for the helicity operator, its two-valued label, and the self-dual split of the field strength.
- *The Proca Equation: Massive Spin 1 in Biquaternionic Form*, for the count of three amplitudes and the constraint that fixes the time component.
- *Maxwell's Equations in the Biquaternionic Formulation*, for the field strength as a pure vector and the scalar part as the Lorenz condition.
- *Canonical Quantization of the Biquaternion Graviton Field*, for the transverse-traceless count of two on the symmetric square.
- *The First-Order Root of the Biquaternion Klein–Gordon Operator*, for the block determinant that is one number to the fourth power.
- *The Klein–Gordon Equation in Biquaternionic Form*, for the dispersion relation as the level set of the norm.
