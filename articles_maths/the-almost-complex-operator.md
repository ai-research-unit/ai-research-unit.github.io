
# __The Almost Complex Operator__

## Introduction

An **almost complex operator** on a smooth manifold $M$ is a field $J$ of endomorphisms of the tangent bundle with $J^2 = -\mathrm{id}$ — the field form of the complex structure of a complex vector space, and an operator on the tangent spaces in its own right. It equips every tangent space with the structure of a complex vector space, and it splits the complexified tangent bundle into the $\pm i$ eigenbundles; the two projections onto those eigenbundles are the operators
$$
\pi^{1,0} = \tfrac12(\mathrm{id} - iJ), \qquad \pi^{0,1} = \tfrac12(\mathrm{id} + iJ),
$$
which are idempotent and conjugate. The operator $J$ alone is not enough to make $M$ a complex manifold: the projections need not be compatible with the Lie bracket, and the obstruction is a tensor, the **Nijenhuis operator** $N_J$, built from $J$ and the bracket. The integrability theorem of Newlander–Nijenhuis states that $N_J$ vanishes exactly when the almost complex structure comes from a holomorphic atlas. When a Hermitian metric $g$ is chosen with $g(JX,JY) = g(X,Y)$, the operator $J$ becomes an isometry of each tangent space, and the pair $(J,g)$ is an almost Hermitian structure whose fundamental form is $\Omega(X,Y) = g(JX,Y)$.

The article has four sections: the almost complex operator and the eigenprojections; the linear model, in which $J$ is always integrable; the Nijenhuis operator and the integrability criterion; and the compatibility with the chosen Hermitian metric. The almost complex structure, its type decomposition, the Nijenhuis tensor with the corpus normalisation, the integrability theorem and the examples are *Hermitian Geometry and Almost Complex Structures*; the article here reads the same structure as an operator, names its eigenprojections and gives the operator form of the integrability criterion. The exterior algebra and the Lie bracket are *Differential Forms* and *The Lie Derivative*; the Hermitian metric, the fundamental form and the Kähler condition are *Kähler Geometry* and *Kähler Manifolds and the Hermitian Form*. The complex structure of a linear space and its linearity are *The Involution on a Complex Vector Space*, later in this category.

Throughout, $M$ is a smooth manifold of even dimension $2n$, $J \in \Gamma(\operatorname{End}(TM))$ is an almost complex structure, $T_{\mathbb C}M = T^{1,0}M\oplus T^{0,1}M$ is the decomposition into the $+i$ and $-i$ eigenbundles of $J$, $\pi^{1,0}$ and $\pi^{0,1}$ are the eigenprojections, $[\,\cdot\,,\,\cdot\,]$ is the Lie bracket of vector fields, and $N_J$ is the Nijenhuis tensor.

## The Almost Complex Operator and the Eigenprojections

**Definition.** An **almost complex structure** on $M$ is a smooth field $J$ of endomorphisms of $TM$ with
$$
J^2 = -\mathrm{id} ;
$$
such a field is also called an **almost complex operator**. A pair $(M,J)$ is an **almost complex manifold**. A map $F : (M,J)\to(N,J')$ is **almost complex** when $dF\circ J = J'\circ dF$.

**Proposition (the eigenprojections).** On the complexified tangent bundle the operator $J$ has the eigenvalues $\pm i$, and the projections onto the eigenbundles are
$$
\pi^{1,0} = \tfrac12(\mathrm{id} - iJ), \qquad \pi^{0,1} = \tfrac12(\mathrm{id} + iJ),
$$
which satisfy
$$
(\pi^{1,0})^2 = \pi^{1,0}, \qquad (\pi^{0,1})^2 = \pi^{0,1}, \qquad \pi^{1,0}\pi^{0,1} = \pi^{0,1}\pi^{1,0} = 0, \qquad \pi^{1,0} + \pi^{0,1} = \mathrm{id} .
$$
They are conjugate, $\overline{\pi^{1,0}} = \pi^{0,1}$, and the complexified tangent space is their direct sum.

**Proof.** From $J^2 = -\mathrm{id}$ the polynomial $x^2+1 = (x-i)(x+i)$ annihilates $J$, and the two factors are coprime over $\mathbb{C}$, so $T_{\mathbb C}M$ is the direct sum of the kernels. The identities are the same computation as for a linear operator with minimal polynomial $x^2+1$: $\pi^{1,0}\pi^{0,1} = \tfrac14(\mathrm{id}-iJ)(\mathrm{id}+iJ) = \tfrac14(\mathrm{id}+J^2) = 0$, and $\pi^{1,0}+\pi^{0,1} = \mathrm{id}$; conjugation reverses the sign of $J$ in the definition.

**Remark (the operator and the reduction).** An almost complex operator is the same datum as a reduction of the structure group of $TM$ from $GL(2n,\mathbb R)$ to $GL(n,\mathbb C)$, and the eigenprojections are the operators by which that reduction is expressed: a complex-linear frame is one whose complexification lies in $T^{1,0}M$. The choice of an almost complex structure is a choice of a field of operators, and it is one of the two structures the geometry of the category reads on the tangent spaces.

## The Linear Model

**Definition.** On a complex vector space $V$ the structure of multiplication by $i$ is a real endomorphism $J$ with $J^2 = -\mathrm{id}$; the same construction with $V$ the tangent space at a point of $M$ gives the linear model of an almost complex structure, and on $M = \mathbb C^n$ with its standard coordinates the field $J$ is the constant operator of multiplication by $i$ on each tangent space.

**Proposition (the linear model is integrable).** On a complex vector space $V$, and on $\mathbb C^n$ with the standard structure, the almost complex operator $J$ satisfies $N_J = 0$ for the Nijenhuis operator of the next section, and $T^{1,0}V$ is the complex vector space $V$ itself, on which multiplication by $i$ acts as $J$ and the projections $\pi^{1,0},\pi^{0,1}$ are the two standard projections of the complexification $V\otimes\mathbb C = V \oplus \bar V$.

**Proof.** The Lie bracket on a vector space, read in constant coordinates, is zero; hence every term of $N_J$ vanishes. The identification $V\otimes_{\mathbb R}\mathbb C \cong V\oplus\bar V$ with the two projections is the standard form of the complexification, and multiplication by $i$ acts on $V$ by $J$ and on $\bar V$ by $-J$.

**Remark.** The linear model is the reason an almost complex structure is a "complex structure" at each point: the tangent space at every point is a complex vector space. Integrability is the separate question of whether these pointwise complex structures vary so as to come from a single holomorphic atlas; the local model $\mathbb C^n$ answers it affirmatively, and the obstruction for a general $J$ is the operator of the next section.

## The Nijenhuis Operator and the Integrability Criterion

**Definition.** The **Nijenhuis operator** of an almost complex structure $J$ is the tensor
$$
N_J(X, Y) = [JX, JY] - J[X, JY] - J[JX, Y] - [X, Y] \qquad (X, Y \in \mathfrak{X}(M)),
$$
with no scalar factor.

**Proposition (tensoriality and elementary symmetries).** $N_J$ is a tensor of type $(1,2)$, that is it is $C^\infty(M)$-bilinear, it is antisymmetric, $N_J(Y,X) = -N_J(X,Y)$, and it satisfies
$$
N_J(X, JX) = 0, \qquad N_J(JX, JY) = N_J(X, Y) .
$$
When $J$ is integrable the tensor vanishes.

**Proof.** The $C^\infty$-bilinearity is the verification that all the second derivatives cancel, exactly as for the analogous computation in *Hermitian Geometry and Almost Complex Structures*, and it uses $J^2 = -\mathrm{id}$ and the Jacobi identity; antisymmetry is read from the definition, and $N_J(X,JX) = [JX,J(JX)] - J[X,J(JX)] - J[JX,JX] - [X,JX] = [JX,-X]-J[X,-X]-0-[X,JX] = 0$, since the first two terms cancel the last. The transformation $X\to JX$, $Y\to JY$ leaves $N_J$ unchanged by substitution and $J^2=-\mathrm{id}$.

**Theorem (the integrability criterion).** For an almost complex structure $J$ on $M$ the following are equivalent: (i) $N_J = 0$; (ii) the eigenbundle $T^{1,0}M$ is closed under the Lie bracket; (iii) $M$ carries a holomorphic atlas whose induced almost complex structure is $J$. The equivalence of (i) and (iii) is the theorem of Newlander–Nijenhuis, quoted; an almost complex structure with $N_J = 0$ is **integrable** and $(M,J)$ is a complex manifold.

**Proof.** The equivalence of (i) and (ii) is the computation that the bracket of two sections of $T^{1,0}M$ has a $(0,1)$-component equal to the corresponding value of $N_J$, so that $T^{1,0}M$ is bracket-closed exactly when $N_J$ vanishes; this is the operator form of the Newlander–Nijenhuis vanishing. The theorem that bracket-closedness is equivalent to the existence of a holomorphic atlas is quoted from *Hermitian Geometry and Almost Complex Structures*, where the Nijenhuis tensor is introduced and the filtration of the proof is deferred.

**Example (an integrable and a non-integrable structure on $\mathbb R^4$).** On $\mathbb R^4$ with coordinates $(x,y,z,t)$ the standard complex structure $J\partial_x = \partial_y$, $J\partial_y = -\partial_x$, $J\partial_z = \partial_t$, $J\partial_t = -\partial_z$ has $J^2 = -\mathrm{id}$ and $N_J = 0$, being the linear model. The structure
$$
J\partial_x = \partial_y + z\,\partial_z, \quad J\partial_y = -\partial_x - z\,\partial_t, \quad J\partial_z = \partial_t, \quad J\partial_t = -\partial_z
$$
also has $J^2 = -\mathrm{id}$, and a direct computation gives
$$
N_J(\partial_x, \partial_z) = \partial_t \neq 0 ,
$$
so this almost complex structure is not integrable and $\mathbb R^4$ with it carries no holomorphic atlas compatible with $J$.

## The Compatibility with the Chosen Hermitian Metric

**Definition.** A Hermitian metric $g$ on an almost complex manifold $(M,J)$ is a Riemannian metric with
$$
g(JX, JY) = g(X, Y) \qquad (X, Y \in \mathfrak{X}(M));
$$
the pair $(J,g)$ is an **almost Hermitian structure**, and its **fundamental form** is $\Omega(X,Y) = g(JX,Y)$. The structure is **almost Kähler** when $\Omega$ is closed, **Kähler** when moreover $\nabla J = 0$ for the Levi-Civita connection.

**Proposition (the operator is an isometry of each tangent space).** When $g$ is Hermitian for $J$, the operator $J$ is orthogonal at every point, $J^{\mathsf T}J = \mathrm{id}$; the fundamental form is a real $(1,1)$-form, alternating, $\Omega(Y,X) = -\Omega(X,Y)$; and the complexified tangent bundle carries the positive-definite Hermitian form $g_{\mathbb C}(v,w) = g(v,\bar w)$ whose holomorphic part is the restriction to $T^{1,0}M$.

**Proof.** $g(JX,JY)=g(X,Y)$ is the orthogonality, and the transpose form $g(JX,Y)=g(JX,J(JY))... $ shows $\Omega$ is skew: $\Omega(Y,X)=g(JY,X)=g(JY,J(JX))=-g(Y,JX)=-\Omega(X,Y)$ using $g(J\cdot,J\cdot)=g$ and $g(JY,J(JX))=g(JY,-X)=-g(JY,X)$. The form $g_{\mathbb C}$ is Hermitian because $J$ is orthogonal, and its positivity is that of $g$; restricting to $T^{1,0}M$ gives the Hermitian form of the holomorphic tangent space. This is *Hermitian Geometry and Almost Complex Structures* and *Kähler Geometry*.

**Remark (what is chosen).** The almost complex operator $J$ is a choice and the Hermitian metric $g$ is a second, independent choice; the type, the eigenprojections and the Nijenhuis tensor depend on $J$ alone, while the isometry of $J$, the fundamental form and the comparison of $J$ with the Levi-Civita connection depend on the pair $(J,g)$. The existence of a $g$-compatible $J$ on a symplectic manifold, and the contractibility of the compatible almost complex structures, are *Symplectic Geometry*, earlier in this Part; the equality $N_J = 0$ is untouched by the metric, which is the sense in which integrability is a property of the operator $J$ alone.

## Summary

An almost complex operator is a field $J$ of endomorphisms of $TM$ with $J^2 = -\mathrm{id}$; it makes each tangent space a complex vector space, splits the complexified tangent bundle into the eigenbundles $T^{1,0}M$, $T^{0,1}M$ of $\pm i$, and gives the idempotent conjugate eigenprojections $\pi^{1,0} = \tfrac12(\mathrm{id}-iJ)$ and $\pi^{0,1} = \tfrac12(\mathrm{id}+iJ)$. On a complex vector space, and on $\mathbb C^n$ with the standard structure, $N_J = 0$ and the structure is the linear model; in general the obstruction to integrability is the Nijenhuis operator $N_J(X,Y) = [JX,JY] - J[X,JY] - J[JX,Y] - [X,Y]$, a $(1,2)$-tensor, antisymmetric, vanishing on $(X,JX)$ and invariant under $(X,Y)\mapsto(JX,JY)$, and $N_J = 0$ is equivalent to the bracket-closedness of $T^{1,0}M$ and, by Newlander–Nijenhuis, to the existence of a holomorphic atlas. The non-integrable example $J\partial_x = \partial_y + z\partial_z$, $J\partial_y = -\partial_x - z\partial_t$, $J\partial_z = \partial_t$, $J\partial_t = -\partial_z$ on $\mathbb R^4$ has $J^2 = -\mathrm{id}$ and $N_J(\partial_x,\partial_z) = \partial_t\neq0$. A chosen Hermitian metric $g$ with $g(JX,JY)=g(X,Y)$ makes $J$ an isometry and defines the fundamental form $\Omega(X,Y)=g(JX,Y)$; the pair $(J,g)$ is almost Hermitian, almost Kähler when $d\Omega = 0$ and Kähler when $\nabla J = 0$. The type decomposition, the Nijenhuis tensor and the integrability theory are *Hermitian Geometry and Almost Complex Structures*; the metric and the Kähler condition are *Kähler Geometry* and *Kähler Manifolds and the Hermitian Form*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $J$, $J^2 = -\mathrm{id}$ | the almost complex operator |
| $T^{1,0}M$, $T^{0,1}M$ | the $\pm i$ eigenbundles of $J$ |
| $\pi^{1,0}$, $\pi^{0,1}$ | eigenprojections, $\tfrac12(\mathrm{id}\mp iJ)$, idempotent and conjugate |
| $N_J(X,Y)$ | the Nijenhuis operator, $[JX,JY]-J[X,JY]-J[JX,Y]-[X,Y]$ |
| $g(JX,JY)=g(X,Y)$ | the Hermitian compatibility of the metric |
| $\Omega(X,Y)=g(JX,Y)$ | the fundamental form |
| $\nabla J = 0$ | the Kähler condition |

## Further Reading

- Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of Differential Geometry II* (Interscience, 1969), for the almost complex structure, the integrability and the Hermitian metrics.
- Newlander and Nirenberg, "Complex analytic coordinates in almost complex manifolds", *Annals of Mathematics* **65** (1957), 391–404, for the integrability theorem.
- Paul Gauduchon, "Hermitian connections and Dirac operators", *Bollettino dell'Unione Matematica Italiana* **11** (1997), 257–288, for the almost Hermitian structures and the fundamental form.
- Alfred Frölicher and Albert Nijenhuis, "Theory of vector-valued differential forms", *Koninklijke Nederlandse Akademie van Wetenschappen* **59** (1956), 338–359, for the Nijenhuis tensor and the Frölicher–Nijenhuis bracket.
